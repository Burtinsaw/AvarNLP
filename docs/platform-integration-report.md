# AvarNLP Platform Entegrasyon Raporu

## Genel Bakis

Bu rapor, AvarNLP projesi icin kullanilabilecek tum platform seceneklerini, fiyatlandirmayi ve entegrasyon stratejisini icerir.

---

## 1. GitHub (Free Plan — Yeterli)

| Ozellik | Free | Pro ($4/ay) |
|---------|------|-------------|
| Public repo Actions | Sinirsiz | Sinirsiz |
| LFS storage | 1 GB | 1 GB |
| Packages (GHCR) | Ucretsiz (public) | Ucretsiz (public) |
| Codespaces | 120 saat/ay | 180 saat/ay |
| Releases (dosya basina) | 2 GB max | 2 GB max |

**Karar:** Pro almaya gerek yok. Public repo oldugu icin Actions sinirsiz. Model dosyalari icin GitHub LFS yerine HuggingFace Hub kullanilacak (ucretsiz, sinirsiz).

**GPU Runners:** T4 mevcut ama sadece Team/Enterprise planlarda ($3.12/saat). Egitim icin uygun degil.

**Firsatlar:**
- GitHub Secure Open Source Fund — $10,000 + $150,000 Azure kredisi
- GitHub Sponsors — Topluluk fonlama, %0 komisyon
- Student Developer Pack — Free Pro + Free Copilot (ogrenci ise)

---

## 2. Hugging Face (PRO $9/ay)

### PRO Plan Ozellikleri

| Ozellik | Free | PRO |
|---------|------|-----|
| Private storage | 100 GB | 1 TB |
| Inference kredisi | 100K unit/ay | 2M unit/ay (20x) |
| ZeroGPU (H200) | 3.5 dk/gun | 25 dk/gun |
| ZeroGPU Spaces | Yok | 10 Space |
| HF Jobs | Yok | Var |
| Dev Mode (SSH) | Yok | Var |

### GPU Spaces Fiyatlari

| GPU | VRAM | $/saat | Aylik (24/7) |
|-----|------|--------|-------------|
| T4 small | 16 GB | $0.40 | $288 |
| L4 | 24 GB | $0.80 | $576 |
| A10G small | 24 GB | $1.00 | $730 |
| A100 | 80 GB | $2.50 | $1,825 |

### HF Jobs (Egitim icin)

| GPU | $/saat | 10 saatlik egitim |
|-----|--------|-------------------|
| T4 | $0.40 | $4 |
| L4 | $0.80 | $8 |
| A10G | $1.00 | $10 |
| A100 | $2.50 | $25 |

### Entegrasyon Plani:
- Demo Space: ZeroGPU ile ucretsiz (H200, 25dk/gun)
- Model hosting: `burtinsaw/avarnlp-nllb-600m` public repo
- Dataset hosting: `burtinsaw/avar-turkish-parallel` versiyonlu dataset
- HF Jobs: L4 ile egitim ($0.80/saat)
- Community GPU Grant: Basvuru yapilacak
- Inference Endpoint: Production API icin T4 $0.50/saat (auto-scale to zero)

---

## 3. Kaggle (Tamamen Ucretsiz)

| Kaynak | Limit |
|--------|-------|
| GPU (P100/T4) | 30 saat/hafta |
| T4 x2 (cift GPU) | 30 saat/hafta |
| TPU v3-8 | 20 saat/hafta |
| RAM (GPU modu) | 29 GB |
| Disk (output) | 20 GB |
| Input data | 100 GB |
| Session suresi | 12 saat max |

Kaggle Pro diye bir sey yok — her sey ucretsiz, kota dahilinde.

### AvarNLP icin Kaggle Stratejisi:
- NLLB-600M + LoRA = ~4-9 GB VRAM, T4'e rahat sigar
- 30 GPU saat/hafta = haftada 7-30 LoRA egitim denemesi
- Dataset versiyonlama — her evrim nesli icin yeni versiyon
- `kagglehub` API ile otomasyon
- Sinir: 12 saat session limiti, GA'yi checkpoint/resume ile parcala

---

## 4. Google Colab (Pro+ $49.99/ay)

### Plan Ozellikleri

| Ozellik | Deger |
|---------|-------|
| Compute Units | 500 CU/ay |
| GPU'lar | T4, L4, A100 (oncelikli) |
| RAM | 52 GB |
| Session | 24 saat (arka plan calismasi) |
| Terminal | Var |

### CU Tuketim Oranlari

| GPU | CU/saat | 500 CU = kac saat |
|-----|---------|-------------------|
| T4 | 1.58 | ~316 saat |
| L4 | 3.00 | ~167 saat |
| A100 | 10.59 | ~47 saat |

### Genetik Algoritma Maliyet Hesabi (200 egitim, 1 epoch)

| GPU | Saat | CU tuketimi | Burcenin %'si |
|-----|------|-------------|---------------|
| T4 | ~50 saat | ~79 CU | %16 |
| L4 | ~16.7 saat | ~50 CU | %10 |
| A100 | ~5 saat | ~53 CU | %11 |

500 CU ile pipeline'i ayda 5-8 kez calistirmak mumkun.

---

## 5. Google Cloud

### GPU Spot Fiyatlari

| GPU | On-Demand $/saat | Spot $/saat | 50 saat spot |
|-----|------------------|-------------|-------------|
| T4 | $0.54 | $0.16-0.22 | $8-11 |
| L4 | $0.70 | $0.21-0.28 | $10-14 |
| A100 40GB | $4.05 | $1.15-1.62 | $57-81 |

### Ucretsiz Firsatlar

| Program | Ne verir | Uygunluk |
|---------|----------|----------|
| $300 deneme kredisi | 90 gun, GPU yok | Herkes |
| TPU Research Cloud | Ucretsiz TPU v2/v3/v4, 30+ gun | Arastirmacilar |
| Research Credits | $1,000+ | PhD/fakulte |
| Google for Startups | $350,000 kredi | Kayitli startup |
| Google.org AI Accelerator | $30M havuzdan pay | Sosyal etki projeleri |

---

## Entegrasyon Mimarisi

```
                    GitHub (kod)
                        |
                        v
    +-------------------------------------------+
    |           AvarNLP Pipeline                |
    |-------------------------------------------|
    |                                           |
    |  Faz 1: Veri Toplama                     |
    |  +- Kaggle Notebook (CPU, ucretsiz)      |
    |  +- Output -> HF Dataset                 |
    |                                           |
    |  Faz 2: Evrimsel Veri Uretimi            |
    |  +- Colab Pro+ (T4, 1.58 CU/saat)       |
    |  +- Output -> HF Dataset (v2, v3...)     |
    |                                           |
    |  Faz 3: Evrimsel Fine-Tuning             |
    |  +- Colab Pro+ (A100)            VEYA    |
    |  +- HF Jobs (L4, $0.80/saat)    VEYA    |
    |  +- Kaggle (T4x2, ucretsiz)     VEYA    |
    |  +- TPU Research Cloud (ucretsiz!)       |
    |                                           |
    |  Deploy:                                  |
    |  +- HF Space (ZeroGPU, ucretsiz)        |
    |  +- HF Inference Endpoint (prod)         |
    |  +- MagaruLaw API entegrasyonu           |
    +-------------------------------------------+
```

## Oncelikli Aksiyonlar

| # | Aksiyon | Maliyet | Etki |
|---|---------|---------|------|
| 1 | TPU Research Cloud'a basvur | $0 | Ucretsiz TPU |
| 2 | HF Community GPU Grant basvurusu | $0 | Ucretsiz demo GPU |
| 3 | HF'de model + dataset repo olustur | $0 | Topluluk gorunurlugu |
| 4 | Kaggle'da dataset + notebook yayinla | $0 | Ek dagitim kanali |
| 5 | GitHub Secure Open Source Fund basvurusu | $0 | $10K + $150K Azure |
| 6 | Colab Pro+ ile Faz 2-3 gelistir | $49.99/ay (mevcut) | Ana egitim ortami |
| 7 | HF Jobs ile production egitim | ~$8-25/run | Kesintisiz egitim |

**Toplam ek maliyet: $0/ay** (mevcut aboneliklerle). Basvurular kabul edilirse yuz binlerce dolarlik kaynak kazanilabilir.
