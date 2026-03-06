"""Fine-tune NLLB-600M with LoRA for Avar-Turkish translation."""

import random
from datasets import Dataset, DatasetDict
from peft import LoraConfig, TaskType, get_peft_model
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForSeq2Seq,
)
from src.data_types import SentencePair

MODEL_NAME = "facebook/nllb-200-distilled-600M"

# Use Turkish NLLB code; Avar doesn't exist so we'll use a placeholder
SRC_LANG = "ava_Cyrl"  # We'll register this
TGT_LANG = "tur_Latn"


def create_lora_config(rank: int = 16, alpha: int = 32) -> LoraConfig:
    return LoraConfig(
        r=rank,
        lora_alpha=alpha,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type=TaskType.SEQ_2_SEQ_LM,
    )


def prepare_dataset(pairs: list[SentencePair], test_ratio: float = 0.1) -> DatasetDict:
    """Split pairs into train/test datasets."""
    shuffled = list(pairs)
    random.shuffle(shuffled)
    split_idx = max(1, int(len(shuffled) * (1 - test_ratio)))

    train_data = [{"av": p.av, "tr": p.tr, "quality": p.quality} for p in shuffled[:split_idx]]
    test_data = [{"av": p.av, "tr": p.tr, "quality": p.quality} for p in shuffled[split_idx:]]

    return DatasetDict({
        "train": Dataset.from_list(train_data),
        "test": Dataset.from_list(test_data),
    })


def load_model_and_tokenizer(lora_config: LoraConfig):
    """Load NLLB model with LoRA adapters."""
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    return model, tokenizer


def tokenize_pairs(examples, tokenizer, max_length: int = 128):
    """Tokenize Avar->Turkish pairs for NLLB."""
    inputs = tokenizer(
        examples["av"],
        max_length=max_length,
        truncation=True,
        padding="max_length",
    )
    targets = tokenizer(
        text_target=examples["tr"],
        max_length=max_length,
        truncation=True,
        padding="max_length",
    )
    inputs["labels"] = targets["input_ids"]
    return inputs


def train(
    pairs: list[SentencePair],
    output_dir: str = "checkpoints/nllb-avar",
    lora_rank: int = 16,
    learning_rate: float = 5e-4,
    batch_size: int = 16,
    epochs: int = 5,
    warmup_ratio: float = 0.1,
):
    """Full training pipeline."""
    lora_config = create_lora_config(rank=lora_rank)
    model, tokenizer = load_model_and_tokenizer(lora_config)
    dataset = prepare_dataset(pairs)

    tokenized = dataset.map(
        lambda ex: tokenize_pairs(ex, tokenizer),
        batched=True,
        remove_columns=dataset["train"].column_names,
    )

    training_args = Seq2SeqTrainingArguments(
        output_dir=output_dir,
        num_train_epochs=epochs,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        learning_rate=learning_rate,
        warmup_ratio=warmup_ratio,
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_steps=10,
        fp16=True,
        predict_with_generate=True,
        load_best_model_at_end=True,
        report_to="wandb",
    )

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["test"],
        data_collator=DataCollatorForSeq2Seq(tokenizer, model=model),
    )

    trainer.train()
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    return model, tokenizer
