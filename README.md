# Intent-Preserving Language Translation System
📌 Project Overview

Traditional language translation systems primarily focus on lexical accuracy and grammatical correctness. While these systems often produce fluent translations, they may fail to preserve the speaker’s intent, emotional tone, or confidence level, which are critical in real-world conversational contexts.
This project presents an Intent-Preserving Language Translation System that explicitly models and preserves speaker intent during translation. Instead of generating a single translation output, the system follows a multi-stage pipeline that extracts intent attributes, generates multiple translation candidates, and selects the translation that best aligns with the original intent.
The system is designed as a research-oriented and explainable prototype, suitable for academic exploration of human-centric and intent-aware machine translation.

🎯 Key Objectives

Preserve speaker intent beyond word-level meaning
Maintain emotional tone and confidence level during translation
Introduce an explicit and transparent intent-based selection mechanism
Demonstrate a human-centric alternative to traditional translation pipelines

🧠 Key Features

Explicit intent extraction (speech act, emotion, confidence)
Multiple translation candidate generation
Intent-based selection of the best translation
Explainable and modular architecture
Suitable for conversational and sensitive communication scenarios

🏗️ System Architecture

The system follows a four-stage pipeline:
Intent Extraction
Extracts intent attributes (speech act, emotion, confidence level) from the source sentence.

Candidate Generation
Generates multiple plausible translations of the input sentence.

Intent Re-Evaluation
Evaluates each candidate translation for intent alignment.

Intent-Based Selection
Selects the translation that best preserves the original intent.

🧪 Example Output

Input (Hindi):

मुझे बहुत गुस्सा आ रहा है


Detected Intent:

Speech Act: Expression  
Emotion: Anger  
Confidence: High


Candidate Translations:

I am really angry.
I'm feeling very frustrated.
I'm quite furious right now.
Final Selected Translation:
I am really angry.

📊 Evaluation Strategy
Qualitative evaluation based on intent preservation

Comparison of:
Speech act consistency
Emotional tone alignment
Confidence level retention
Manual inspection of translation suitability in conversational contexts

🔮 Future Improvements
Quantitative intent similarity scoring
Support for additional languages
Integration with conversational agents
Human evaluation studies
Lightweight fine-tuned intent classifiers

🛠️ Tools & Technologies
Python
Large Language Models (via API)
Jupyter Notebook (.ipynb)
VS Code (development)
Git & GitHub

📂 Repository Structure
intent_translation_project/
│
├── intent_translation.ipynb   # Primary evaluation notebook
├── main.py                    # Core pipeline execution
├── intent_extractor.py        # Intent extraction logic
├── candidate_generator.py     # Translation generation
├── evaluator.py               # Intent-based selection
├── requirements.txt
├── README.md
└── .env                       # API keys (not committed)

▶️ How to Run

Clone the repository

Create and activate a virtual environment

Install dependencies:
pip install -r requirements.txt
Add API keys to .env

Run:
python main.py
or open and run all cells in intent_translation.ipynb

📘 Academic Context

This project was developed as part of an academic AI course project.
The Jupyter Notebook (.ipynb) serves as the primary evaluation artifact, with reports, slides, and demo videos as supporting materials.

🤖 AI Usage Disclosure

AI tools, including large language models, were used to assist in:
Code development
Prompt design
Documentation drafting
All architectural decisions, evaluations, and interpretations were performed by the author.
