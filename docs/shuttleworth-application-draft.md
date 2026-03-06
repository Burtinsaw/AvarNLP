# Shuttleworth Foundation Fellowship — AvarNLP Basvuru Taslagi

> **Deadline:** 1 Mayis 2026 (Eylul 2026 intake icin)
> **Miktar:** ~$275,000/yil (maas + proje fonu)
> **URL:** https://www.shuttleworthfoundation.org/apply/
> **Gerekli:** Form + 5 dakika video + CV

---

## FORM CEVAPLARI

### Q1: Tell us about the world as you see it.

```
There are approximately 7,000 languages spoken in the world today.
AI-powered language technology — translation, voice assistants, search
— works well for maybe 100 of them. The remaining 6,900 languages,
spoken by billions of people, are invisible to the digital world.

The Avar language is a stark example. Spoken by 800,000 people across
Dagestan, Turkey, and Europe, Avar has a literary tradition dating to
the 15th century. Yet in 2026, there is no machine translation for
Avar, no spell checker, no voice assistant, no digital dictionary —
nothing. An Avar speaker cannot use Google Translate, cannot ask Siri
a question, cannot even type their language on most keyboards without
workarounds.

This is not just a technology gap — it is a cycle of erasure. Without
digital tools, young Avar speakers default to Russian or Turkish
online. Without online presence, tech companies see no market for Avar
tools. Without tools, the language retreats further from digital life.
UNESCO classifies Avar as "definitely endangered."

The fundamental problem is data. Modern NLP requires millions of
translated sentence pairs to train a model. Avar has fewer than 1,000
available digitally. Traditional data collection — paying linguists
to manually translate — costs hundreds of thousands of dollars and
takes years. For a language with limited institutional support and
no commercial market, this path is essentially closed.

This is the reality for thousands of endangered languages worldwide.
Not a lack of speakers, not a lack of culture — but a lack of data
to feed the machines that increasingly mediate human communication.
```

### Q2: What change do you want to make in the world?

```
I want to prove that endangered languages don't need massive budgets
or institutional backing to enter the AI age. I'm building AvarNLP
— the world's first machine translation system for the Avar language
— using an approach that could work for any of the thousands of
languages currently locked out of digital technology.

The key insight: instead of waiting years to manually collect training
data, we can evolve it. AvarNLP uses genetic algorithms — inspired
by biological evolution — to start with a tiny seed of translated
sentences and grow them into a large, high-quality training corpus.
Each generation of data is tested for linguistic accuracy, diversity,
and translation quality. The fittest data survives and reproduces.
After many generations, we have enough data to train a real
translation model.

The immediate change: Avar speakers get a translation tool — the
first ever — accessible through a simple web interface. An Avar
grandmother in a Turkish village can translate a government document.
An Avar student in Moscow can read their ancestral poetry. A diaspora
community spread across three countries can communicate in their
own language digitally for the first time.

The systemic change: the evolutionary framework is open-source and
language-agnostic. If it works for Avar, it works for Lezgin
(800,000 speakers), Tabasaran (130,000), Tsez (13,000), and
hundreds of other languages in the Caucasus alone — and thousands
more worldwide. One successful proof of concept could unlock
digital language technology for the entire long tail of human
languages.
```

### Q3: What do you believe has prevented this change to date?

```
Three barriers have kept endangered languages out of AI:

1. THE DATA POVERTY TRAP
NLP models need data. Endangered languages have little data. Without
models, there's no incentive to create data. This circular trap has
no obvious entry point using conventional methods. The assumption
has been: first collect data (expensive, slow), then build models.
Nobody has seriously tried to generate the data computationally for
languages this small.

2. THE WRONG ACTORS
Big tech companies (Google, Meta, Microsoft) optimize for languages
with large user bases and commercial potential. Academic researchers
focus on languages with existing datasets and institutional support.
Neither group has strong incentive to work on Avar — a language with
no commercial market and almost no digital presence. The people who
care most about Avar — its speakers — typically lack the technical
skills to build NLP systems.

3. THE OPENNESS GAP
The few low-resource language projects that do exist often produce
closed models, proprietary datasets, or tools locked behind
institutional walls. Even Meta's NLLB project, which covers 200
languages, excluded Avar and hundreds of similar languages. Without
open, replicable frameworks, each language community must start from
scratch.

I am in a unique position to break through all three barriers: I am
one of the few Avar speakers who can both write the language fluently
AND build the technology. I don't need to hire linguists or partner
with institutions — I am the linguist and the engineer in one person.
And by building everything in the open, I ensure that my work doesn't
just help Avar — it creates a template for every endangered language.
```

### Q4: What are you going to do to get there?

```
AvarNLP is a three-phase pipeline, already architected and coded:

PHASE 1 — SEED DATA COLLECTION
Collect ~1,000 Avar-Turkish parallel sentence pairs from existing
sources: my own MagaruLaw.com platform, online dictionaries, Avar
Wikipedia, and Cafer Barlas's 640-page Turkish-Avar-Russian
Dictionary (our project advisor, one of the only comprehensive Avar
lexicographic works in existence).

PHASE 2 — EVOLUTIONARY DATA GENERATION
Use genetic algorithms to evolve the seed corpus into 50,000+ pairs.
Evolutionary agents apply mutations (word swap, morphological
variation, template filling) and a fitness function evaluates each
generation for linguistic validity, diversity, and translation
consistency. Natural selection keeps only the best data. This is the
novel core of the project.

PHASE 3 — EVOLUTIONARY MODEL TRAINING
Fine-tune Meta's NLLB-600M translation model using LoRA (parameter-
efficient fine-tuning) on the evolved dataset. A second genetic
algorithm optimizes training hyperparameters across 200+ runs,
finding the best configuration automatically.

DEPLOYMENT
- Free web demo on Hugging Face Spaces
- Translation API integrated into MagaruLaw.com
- All code (MIT), models (Apache 2.0), datasets (CC-BY-SA 4.0)
  publicly released

The code is written, the architecture is designed, and the GitHub
repo is live: github.com/Burtinsaw/AvarNLP

What I need is time. The fellowship would let me work on this
full-time for a year instead of squeezing it between other work.
```

### Q5: What challenges or uncertainties do you expect to face?

```
1. QUALITY OF EVOLVED DATA
The biggest risk: evolutionary data generation might produce
grammatically correct but unnatural sentences, or translations that
are technically accurate but miss cultural nuance. Mitigation: my
own native-level Avar competence for evaluation, plus two advisors
— Prof. Murtazaliev (Dagestan Academy of Sciences, Avar literary
specialist) and Cafer Barlas (author of the Avar-Turkish dictionary).

2. MORPHOLOGICAL COMPLEXITY
Avar has ~20 noun cases and ergative-absolutive verb alignment —
far more complex than the languages NLLB was primarily trained on.
The model may struggle with Avar grammar even after fine-tuning.
Mitigation: LoRA targets specific model layers, and evolutionary
hyperparameter search finds the optimal configuration.

3. EVALUATION DIFFICULTY
With no existing Avar MT system, there's no baseline to compare
against. How do we know if the model is "good enough"?
Mitigation: multi-metric evaluation (BLEU, chrF++), human evaluation
by native speakers, and real-world testing through MagaruLaw.com.

4. COMMUNITY ADOPTION
Building the technology is necessary but not sufficient — Avar
speakers need to actually use it. Mitigation: I already run
MagaruLaw.com, an active Avar cultural platform. I have a direct
channel to the community and understand their needs because I am
part of that community.

5. SCALING TO OTHER LANGUAGES
The framework is designed to be language-agnostic, but each language
has unique morphological challenges. Mitigation: extensive
documentation, modular design, and actively seeking collaborators
from other language communities.
```

### Q6: What part does openness play in your idea?

```
Openness is not a feature of AvarNLP — it is the entire point.

CODE: Everything is MIT-licensed on GitHub. Anyone can fork it,
adapt it, improve it. The evolutionary data generation framework
is designed to be reused by other language communities without
needing to understand the internals.

MODELS: Released on Hugging Face Hub under Apache 2.0. Any developer
can download, fine-tune further, or deploy the Avar translation
model. No API keys, no rate limits, no corporate gatekeeping.

DATA: The evolved Avar-Turkish parallel corpus is released under
CC-BY-SA 4.0 on Hugging Face. This is potentially the first
publicly available Avar parallel corpus of significant size.

METHODOLOGY: The evolutionary approach to corpus generation will be
documented in a detailed technical blog post / research paper,
so that other communities can replicate it without starting from
zero.

PROCESS: All development happens in public on GitHub. Research
findings, failed experiments, and lessons learned are shared openly.

WHY THIS MATTERS:
The reason endangered languages have no NLP tools is partly because
the few existing efforts are closed. Google doesn't publish its
internal language models for small languages. Academic papers
describe methods but don't release usable tools. AvarNLP breaks
this pattern. When the next person wants to build translation for
Lezgin or Tsez or any endangered language, they don't need to
reinvent everything — they fork AvarNLP, plug in their seed data,
and evolve.

Openness turns one language project into a platform for hundreds.
```

### Q7-15: Data Questions

| Soru | Cevap |
|------|-------|
| Does your idea have a name? | Yes — AvarNLP |
| Have you started implementing? | Yes |
| How funded in the past? | Self-funded / Bootstrapped |
| Key partners? | Prof. Akhmed Murtazaliev (Dagestan Academy of Sciences), Cafer Barlas (Lexicographer, Turkey), Hugging Face (platform) |
| For-profit or not-for-profit? | Not-for-profit |
| Where based during fellowship? | Turkey |
| Where will you implement? | Turkey, with global online reach |
| Online presence? | Yes — magarulaw.com |
| Project online presence? | Yes — github.com/Burtinsaw/AvarNLP |

### Q20: Have you applied previously?
No

### Q21: How did you hear about Shuttleworth?
Online research

---

## GEREKLI MATERYALLER

- [ ] 5 dakika video (EN ONEMLI — onlar once videoyu izliyor)
- [ ] CV/Resume (PDF)
- [ ] Form doldurma

## VIDEO ICIN NOTLAR

Video form cevaplarından ONCE degerlendiriliyor. Samimi, kisisel,
tutkulu olmali. Sablona gore degil, kalpten konusmali.

Onerilen yapi (5 dakika):
1. (30sn) Kendini tanit — Avar toplulugu, MagaruLaw
2. (60sn) Problem — Avar dilinin dijital yoklugu
3. (90sn) Cozum — Evrimsel veri uretimi, nasil calisiyor
4. (60sn) Neden sen — Hem muhendis hem Avarca bilen nadir kisi
5. (30sn) Aciklik — Neden open-source, nasil diger dillere yayilir
6. (30sn) Cagri — Fellowship ile ne degisir

Avarca birkaç cümle söylemek çok etkili olur — jüri için unutulmaz
bir an yaratır.
