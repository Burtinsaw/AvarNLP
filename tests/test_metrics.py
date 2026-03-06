from src.evaluation.metrics import compute_bleu, compute_chrf, evaluate_model_on_pairs

def test_compute_bleu_identical():
    score = compute_bleu(["Merhaba dunya"], ["Merhaba dunya"])
    assert score > 90.0

def test_compute_bleu_different():
    score = compute_bleu(["Merhaba dunya"], ["Gule gule evren"])
    assert score < 30.0

def test_compute_chrf_identical():
    score = compute_chrf(["Merhaba dunya"], ["Merhaba dunya"])
    assert score > 90.0

def test_evaluate_model_returns_dict():
    predictions = ["Merhaba", "Tesekkurler"]
    references = ["Merhaba", "Tesekkur ederim"]
    result = evaluate_model_on_pairs(predictions, references)
    assert "bleu" in result
    assert "chrf" in result
    assert 0.0 <= result["bleu"] <= 100.0
