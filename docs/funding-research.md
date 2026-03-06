# AvarNLP Fonlama Arastirma Raporu

**Tarih:** 2026-03-06

---

## 1. GitHub Secure Open Source Fund

**Sonuc: UYGUN DEGIL**

| Kriter | Durum |
|--------|-------|
| Proje olgunlugu | Yeni proje, 0 star — FAIL |
| Topluluk destegi | Henuz yok — FAIL |
| Odak alani | Guvenlik, NLP degil — UYUMSUZ |
| Hibe miktari | $10,000 + $150,000 Azure kredisi |

### Neden Uygun Degil
- "Demonstrated community traction" gerektiriyor (yildiz, contributor, kullanici)
- Guvenlik odakli — kod denetimi, bagimlilk taramasi vb.
- Yeni/kucuk projeler icin degil, kurumsallassmis acik kaynak icin

### Daha Iyi Alternatifler

#### A. NLnet / NGI Zero Commons Fund
| Detay | Bilgi |
|-------|-------|
| Miktar | 5,000 - 50,000 EUR |
| Son basvuru | **1 Nisan 2026** (25 gun!) |
| Uygunluk | Erken asamadaki acik kaynak R&D |
| Odak | Dijital altyapi, dil teknolojileri |
| Basvuru | https://nlnet.nl/propose/ |

**Neden uygun:** Tehlike altindaki diller icin NLP araci, acik kaynak, erken asamada — tam NLnet'in profili.

#### B. Lacuna Fund
| Detay | Bilgi |
|-------|-------|
| Miktar | $5,000 - $50,000 |
| Odak | Dusuk kaynak dilleri icin NLP dataset |
| Basvuru | https://lacunafund.org/ |

**Neden uygun:** Avar dili tam olarak "dusuk kaynak dili" kategorisinde. Dataset olusturma projesi olarak basvuru yapilabilir.

#### C. GitHub Accelerator
| Detay | Bilgi |
|-------|-------|
| Donem | Yilda 2 donem |
| Odak | AI odakli acik kaynak projeler |
| Avantaj | Mentorluk + fonlama |

#### D. Mozilla Common Voice / MOSS Programi
- Dil koruma projeleri icin fonlama
- Topluluk odakli, kucuk projeler kabul edilir

---

## 2. TPU Research Cloud (TRC)

**Sonuc: GUCLU ADAY — BASVURU YAPILMALI**

| Detay | Bilgi |
|-------|-------|
| Basvuru URL | https://sites.research.google/trc/ |
| Maliyet | Ucretsiz |
| Donanim | TPU v2, v3, v4 |
| Sure | ~30 gun (uzatilabilir) |
| Akademik gereklilik | YOK — herkes basvurabilir |
| Kabul sansi | %40-60 (tahmini) |

### Basvuru Sureci
1. Basit online form (arastirma onerisi denemesi yok)
2. Proje aciklamasi (~200 kelime)
3. Beklenen kaynak kullanimi
4. Yayin/paylasim plani
5. Yanit suresi: 1-2 hafta

### AvarNLP icin TRC Kullanim Plani
- NLLB-600M fine-tuning (TPU v3-8 ile)
- Evrimsel egitim pipeline'i (200+ egitim calismasi)
- PyTorch/XLA uzerinden calismasi mumkun

### Teknik Notlar
- PyTorch TPU'da calisir (PyTorch/XLA kutuphanesi ile)
- LoRA + TPU kombinasyonunda bilinen bazi uyumluluk sorunlari var
- Cozum: `xla_fsdp` veya dogrudan full fine-tuning (TPU'da VRAM siniri olmadigi icin)
- Alternatif: JAX/Flax ile yeniden implementasyon (daha verimli ama ek is)

### Basvuru Mesaj Sablonu

```
Project: AvarNLP — Self-Evolving AI for Endangered Avar Language

We are building an open-source NLP system for the Avar language (UNESCO
severely endangered, ~800K speakers). The project uses evolutionary
algorithms to generate training data and optimize fine-tuning of Meta's
NLLB-600M translation model.

TPU access would enable:
- Running 200+ evolutionary training iterations for hyperparameter search
- Fine-tuning NLLB-600M with LoRA/full fine-tuning on evolved datasets
- Evaluating translation quality across generations

All models and datasets will be publicly released on Hugging Face Hub.
Research findings will be shared as a technical blog post / paper.

GitHub: https://github.com/Burtinsaw/AvarNLP
```

---

## 3. GitHub Pro + Student Developer Pack

Kullanici 2 ayri GitHub hesabina sahip:
- Hesap 1: GitHub Pro ($4/ay veya mevcut)
- Hesap 2: Student Developer Pack

### Student Developer Pack Avantajlari (AvarNLP icin)

| Avantaj | Deger |
|---------|-------|
| GitHub Pro | Ucretsiz (zaten var) |
| GitHub Copilot | Ucretsiz |
| Azure for Students | $100 kredi |
| DigitalOcean | $200 kredi |
| Heroku | $13/ay kredi |
| JetBrains IDE'ler | Ucretsiz |
| Namecheap domain | 1 yil ucretsiz .me |
| GitLens Pro | Ucretsiz |

### Strateji
- **Ana gelistirme**: Pro hesapta (Burtinsaw/AvarNLP)
- **Azure kredisi**: Student hesaptaki $100 ile Azure VM denemesi
- **Copilot**: Gelistirme hizini artirmak icin

---

## Oncelikli Aksiyon Plani

| # | Aksiyon | Aciliyet | Tahmini Etki |
|---|---------|----------|-------------|
| 1 | **NLnet basvurusu yap** | ACIL (1 Nisan!) | 5K-50K EUR |
| 2 | **TPU Research Cloud basvurusu** | Yuksek | Ucretsiz TPU ~30 gun |
| 3 | **Lacuna Fund takip et** | Orta | $5K-50K dataset fonlama |
| 4 | **HF Community GPU Grant** | Orta | Ucretsiz demo GPU |
| 5 | **Student Pack Azure kredisini kullan** | Dusuk | $100 Azure |
