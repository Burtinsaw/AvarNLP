# NLnet / NGI Zero Commons Fund — AvarNLP Basvuru

> **DURUM: GONDERILDI — 6 Mart 2026**
> **Basvuru kodu: 2026-04-0dd**
> **Fon: NGI Zero Commons Fund**
> **Talep edilen miktar: 20,000 EUR**
> **Beklenen yanit suresi: 2-3 ay (Mayis-Haziran 2026)**

---

## Basvuru Formu Alanlari ve Taslak Yanitlar

### 1. Contact Information

| Alan | Deger |
|------|-------|
| Name | Arif AKGUN |
| Email | admin@magarulaw.com |
| Phone | +905444343210 |
| Organisation | Individual (MagaruLaw.com founder) |
| Country | Turkey |

> **Not:** Bireysel basvuru kabul ediliyor. Organizasyon sart degil.

---

### 2. Proposal Name

```
AvarNLP: Self-Evolving AI for the Endangered Avar Language
```

---

### 3. Website / Wiki URL

```
https://github.com/Burtinsaw/AvarNLP
```

---

### 4. Abstract (EN ONEMLI KISIM)

> Degerlendirme agirliklarini hatirla:
> - Teknik Mukemmellik: %30
> - Etki ve Strateji: %40 (en yuksek!)
> - Maliyet Verimliligi: %30

```
AvarNLP is an open-source project to build the first dedicated NLP system
for the Avar language — a Northeast Caucasian language spoken by
approximately 800,000 people, classified as "definitely endangered" by
UNESCO. Despite having a literary tradition dating back to the 15th
century, Avar has virtually zero digital language technology: no machine
translation, no spell checkers, no text-to-speech systems.

THE PROBLEM:
Modern NLP requires large parallel corpora (millions of sentence pairs),
but Avar has fewer than 1,000 digitally available translated sentences.
Traditional data collection is too slow and expensive for a language with
limited online presence. This "data poverty trap" means Avar speakers
are excluded from the AI revolution that benefits major languages.

OUR APPROACH — EVOLUTIONARY DATA GENERATION:
Instead of waiting for manual data collection, AvarNLP uses genetic
algorithms to evolve its own training data. The system:

1. Starts with a small seed corpus (~500-1,000 sentence pairs) collected
   from existing Avar-Turkish bilingual sources
2. Deploys evolutionary agents that mutate, recombine, and generate new
   sentence variations using linguistic rules specific to Avar morphology
3. Evaluates generated data quality using automated fitness functions
   (language validity, diversity, translation consistency)
4. Selects the best-performing data through natural selection across
   generations
5. Fine-tunes Meta's NLLB-600M multilingual translation model using the
   evolved dataset with Parameter-Efficient Fine-Tuning (LoRA)
6. Uses a second evolutionary loop to optimize training hyperparameters

This approach is novel: instead of building a static dataset, we build a
system that continuously improves its own training data through evolution.

EXPECTED OUTCOMES:
- First Avar-Turkish and Avar-Russian machine translation system
- Open-source evolutionary data generation framework replicable for other
  endangered languages (Lezgin, Tabasaran, Tsez, etc.)
- Publicly available Avar parallel corpus on Hugging Face Hub
- Research publication documenting the evolutionary approach
- Web-based translation demo accessible to Avar speakers

EUROPEAN DIMENSION:
Avar is spoken primarily in Dagestan (Russia) and by diaspora communities
in Turkey and across Europe. The project directly serves European language
diversity goals. The methodology is designed to be replicated for dozens
of other endangered Caucasian, Uralic, and minority European languages
that face the same data poverty problem.

OPEN SOURCE COMMITMENT:
All code (MIT license), models (Apache 2.0), and datasets (CC-BY-SA 4.0)
will be publicly released. The evolutionary framework is language-agnostic
and designed for community adoption.
```

---

### 5. Have you been involved with projects or organizations relevant to this project before?

```
I am Arif Akgun, the founder and developer of MagaruLaw.com — an Avar
cultural platform that publishes content in Avar, Turkish, Russian, and
English. Through this work, I have direct experience with the challenges
of digitizing Avar language content and understand the community's needs
firsthand.

I am connected to the Avar-speaking community and have deep familiarity
with Avar linguistics, morphology, and the cultural context necessary to
evaluate translation quality.

The project has the advisory support of:
- Prof. Akhmed M. Murtazaliev (Doctor of Philological Sciences, Chief
  Research Fellow at the Institute of Language, Literature and Art named
  after Gamzat Tsadasa, Dagestan Scientific Center of the Russian Academy
  of Sciences) — specialist in Avar literary heritage and the Dagestani
  diaspora in Turkey.
- Cafer Barlas (Researcher, Writer & Lexicographer, Turkey) — author of
  the 640-page Turkish-Avar-Russian Dictionary, one of the most
  comprehensive Avar lexicographic works. Ethnic Avar from Dagestan,
  founding member of the Shamil Foundation.

This project grows directly from practical needs encountered while
building MagaruLaw — the absence of any digital language tools for Avar
speakers.
```

---

### 6. Requested Amount (EUR)

**Onerilen miktar: 15,000 EUR**

> Neden 15K: Ilk basvuru icin max 50K ama gercekci ve maliyet-etkin
> bir butce daha iyi puan alir. 15K ile tum hedefler karsilanabilir.

---

### 7. Budget Breakdown

```
Total requested: 15,000 EUR

PHASE 1 — Data Collection & Corpus Building (2,500 EUR)
- Web scraping infrastructure and data pipeline development: 40 hours
- Manual verification of seed corpus quality: 20 hours
- Integration with Hugging Face datasets: 10 hours
Rate: ~36 EUR/hour

PHASE 2 — Evolutionary Data Generation System (4,500 EUR)
- Genetic algorithm framework (DEAP integration): 40 hours
- Fitness function development (language validity, diversity): 30 hours
- Evolutionary agent implementation and testing: 30 hours
- Data quality evaluation pipeline: 25 hours
Rate: ~36 EUR/hour

PHASE 3 — Model Training & Optimization (4,000 EUR)
- NLLB-600M fine-tuning with LoRA: 30 hours development
- Evolutionary hyperparameter optimization: 25 hours
- GPU compute costs (HuggingFace Jobs / Cloud): 500 EUR
- Evaluation benchmarking (BLEU, chrF++): 20 hours
Rate: ~36 EUR/hour (dev) + compute

PHASE 4 — Demo, Documentation & Dissemination (2,500 EUR)
- Gradio web demo on HuggingFace Spaces: 20 hours
- API development (FastAPI): 15 hours
- Research writeup / technical blog post: 20 hours
- Documentation and replication guide: 15 hours
Rate: ~36 EUR/hour

PHASE 5 — Community & Sustainability (1,500 EUR)
- Community outreach to Avar diaspora: 15 hours
- Integration with MagaruLaw.com platform: 15 hours
- Framework adaptation guide for other languages: 10 hours
Rate: ~36 EUR/hour

TOTAL HOURS: ~380 hours over 6 months
COMPUTE COSTS: ~500 EUR
EFFECTIVE RATE: ~38 EUR/hour (including compute)
```

---

### 8. Comparison with Existing Efforts

```
EXISTING APPROACHES:

1. Meta NLLB (No Language Left Behind): Covers 200 languages but does NOT
   include Avar. The NLLB-200 model is our base, but it has no Avar
   capability out of the box.

2. Google Translate: Does not support Avar. Supports only 2 of the 40+
   Northeast Caucasian languages (none of them Avar).

3. Academic work on low-resource NLP: Most approaches (data augmentation,
   transfer learning, few-shot) assume at least 10,000+ parallel
   sentences exist. Avar has fewer than 1,000.

4. Masakhane project (African languages): Inspiring community model, but
   focused on African languages with different linguistic challenges.
   Their approach requires existing bilingual speakers as annotators.

OUR DIFFERENTIATION:

- Evolutionary approach: No existing system uses genetic algorithms to
  evolve training corpora for endangered languages
- Extreme low-resource focus: Designed to work with <1,000 seed pairs
  (most methods need 10,000+)
- Self-improving: The system gets better over generations without human
  intervention
- Replicable: Framework is language-agnostic; same approach works for
  Lezgin, Tabasaran, Tsez, and dozens of other languages
- Community-connected: Built by someone embedded in the Avar community
  (MagaruLaw.com), not by outside researchers
```

---

### 9. Significant Technical Challenges

```
1. EXTREME DATA SCARCITY
   Avar has <1,000 digitally available parallel sentences. Our
   evolutionary approach must generate meaningful training data from
   this minimal seed. Risk: generated data could drift from authentic
   Avar usage.
   Mitigation: Fitness functions enforce Avar orthographic rules,
   morphological patterns, and vocabulary constraints. Manual spot-checks
   by native speakers at each evolution milestone.

2. MORPHOLOGICAL COMPLEXITY
   Avar is highly agglutinative with ~20 noun cases and complex verb
   conjugation (ergative-absolutive alignment). Standard NLP tokenizers
   underperform on such morphology.
   Mitigation: Using SentencePiece (from NLLB) which handles
   agglutinative languages well. Custom fitness functions penalize
   morphologically invalid generations.

3. EVALUATION WITHOUT GROUND TRUTH
   With no existing Avar MT system, there's no baseline to compare
   against. Standard BLEU scores are less meaningful.
   Mitigation: Multi-metric evaluation (BLEU, chrF++, manual human
   evaluation). Creating a held-out test set verified by native speakers.

4. EVOLUTIONARY CONVERGENCE
   Genetic algorithms can converge to local optima, producing repetitive
   or low-diversity data.
   Mitigation: Diversity-weighted fitness function, immigration
   operators, adaptive mutation rates across generations.
```

---

### 10. Ecosystem and Engagement

```
RELEVANT ACTORS:
- Avar diaspora communities (Turkey, Europe): Primary users and
  evaluators. Engaged through MagaruLaw.com platform (existing audience).
- Project advisors:
  * Prof. Akhmed M. Murtazaliev (Dagestan Academy of Sciences, IYALI) —
    Avar literary heritage, diaspora research, linguistic validation.
  * Cafer Barlas (Turkey) — Avar lexicography, author of Turkish-Avar-
    Russian Dictionary (640 pages), community bridge to Avar diaspora.
- Hugging Face: Model and dataset hosting, community visibility.
  AvarNLP will be published as public model + dataset repos.
- Masakhane community: Methodological inspiration; potential collaboration
  on cross-applying evolutionary approach to other language families.
- UNESCO/Endangered Languages Project: Alignment with preservation goals.
- Institute of Language, Literature and Art (IYALI), Dagestan: Academic
  collaboration for linguistic validation through Prof. Murtazaliev.

ENGAGEMENT STRATEGY:
- Open-source everything from day one (GitHub + HuggingFace)
- Publish research findings as technical blog + potential workshop paper
- Release framework as reusable toolkit for other endangered languages
- Community testing through MagaruLaw.com integration
- Leverage advisor network for quality validation and diaspora outreach
- Engage with HuggingFace's language diversity initiatives
```

---

### 11. AI Usage Disclosure

```
This proposal was drafted with assistance from Claude (Anthropic),
used for:
- Structuring the application text
- Researching comparable projects
- Technical architecture planning

The core ideas, linguistic knowledge, community connections, and project
vision are entirely human-originated. All AI-generated text was reviewed,
edited, and validated by the applicant.
```

---

## Basvuru Oncesi Kontrol Listesi

- [x] GitHub repo'yu duzenle (README, LICENSE ekle)
- [x] Danismanlari README'ye ekle
- [x] Kisisel bilgileri taslaga ekle
- [x] Abstract'i son kez gozden gecir
- [x] Butceyi kontrol et (20,000 EUR)
- [x] Formu doldur: https://nlnet.nl/propose/
- [x] **GONDERILDI — 6 Mart 2026, Kod: 2026-04-0dd**
- [ ] HuggingFace'te model repo olustur: `burtinsaw/avarnlp-nllb-600m`
- [ ] HuggingFace'te dataset repo olustur: `burtinsaw/avar-turkish-parallel`
- [ ] MagaruLaw.com'a AvarNLP hakkinda bir sayfa ekle (opsiyonel)
- [ ] Yanit bekleniyor (Mayis-Haziran 2026)

---

## Onemli Notlar

1. **Dil:** Tum form INGILIZCE doldurulmali
2. **Bireysel basvuru:** Organizasyon sart degil, bireysel basvuru kabul ediliyor
3. **Turkiye'den basvuru:** "Countries associated to Horizon Europe" listesinde Turkiye VAR (associated country) — bu cok iyi, oncelikli kategoridasin
4. **Minimum puan:** 5.0/7.0 ustu gerekli
5. **Degerlendirme:** Birden fazla uzman bagimsiz olarak degerlendiriyor
6. **Sonuc suresi:** Genellikle 2-3 ay icinde yanit gelir
7. **Ek dosya:** Max 50 MB, PDF/HTML/ODT kabul ediliyor
