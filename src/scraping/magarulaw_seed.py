"""Extract seed parallel data from MagaruLaw dictionary."""

from src.data_types import SentencePair

# Hardcoded from magarulaw/src/seed/dictionary.ts
SEED_DATA = [
    {"av": "Росдал", "tr": "Koy", "ex_av": "Дир росдал гъоркьаб рукъ буго", "ex_tr": "Benim koyumde guzel bir ev var"},
    {"av": "Эбел", "tr": "Anne", "ex_av": "Дир эбел цIуяб нуж йиго", "ex_tr": "Annem genc bir kadindir"},
    {"av": "Эмен", "tr": "Baba", "ex_av": "Дир эмен хъвараб чи вуго", "ex_tr": "Babam guclu bir insandir"},
    {"av": "Рукъ", "tr": "Ev", "ex_av": "Гьаб рукъ бакIараб буго", "ex_tr": "Bu ev buyuktur"},
    {"av": "ЛъикI", "tr": "Iyi", "ex_av": "ЛъикI буго", "ex_tr": "Iyidir"},
    {"av": "Хiинкъал", "tr": "Hinkal", "ex_av": "Эбелалъ хiинкъал гьабуна", "ex_tr": "Annem hinkal yapti"},
    {"av": "МацI", "tr": "Dil", "ex_av": "Авар мацI гIемераб мацI буго", "ex_tr": "Avarca zengin bir dildir"},
    {"av": "Гъуниб", "tr": "Gunib", "ex_av": "Гъуниб гъоркьаб мина буго", "ex_tr": "Gunib guzel bir yerdir"},
    {"av": "Салам", "tr": "Merhaba", "ex_av": "Салам алейкум!", "ex_tr": "Selam aleykum!"},
    {"av": "Баркала", "tr": "Tesekkurler", "ex_av": "Баркала дуе!", "ex_tr": "Sana tesekkurler!"},
]


def extract_seed_pairs() -> list[SentencePair]:
    pairs = []
    for item in SEED_DATA:
        # Word-level pair
        pairs.append(SentencePair(av=item["av"], tr=item["tr"], source="magarulaw_seed", quality=1.0))
        # Sentence-level pair (example)
        if item.get("ex_av") and item.get("ex_tr"):
            pairs.append(SentencePair(av=item["ex_av"], tr=item["ex_tr"], source="magarulaw_seed", quality=1.0))
    return pairs
