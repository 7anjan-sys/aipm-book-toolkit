<<<<<<< HEAD
📘 AIPM Book Toolkit

This repository hosts the companion toolkit for the upcoming book “AI Program Manager: How AI-Augmented Scrum & Agile Deliver 10× Value.”

It provides hands-on labs, prompts, flashcards, and quizzes to help readers prepare for the AI-Driven Project Manager (AIPM) certification.

📂 Repository Structure
aipm-book-toolkit/
│
├── labs/                  # Jupyter/Colab notebooks
│   ├── lab1_backlog_classifier.ipynb
│   ├── lab2_velocity_forecast.ipynb
│   └── lab3_bias_audit.ipynb
│
├── prompts/               # Prompt library
│   └── prompts.json
│
├── flashcards/            # Study flashcards
│   └── flashcards.csv
│
├── quizzes/               # Practice MCQs
│   └── chapter_quiz.yaml
│
├── LICENSE-MIT            # License for code
├── LICENSE-CC-BY-NC       # License for content
└── README.md              # This file

🚀 Getting Started

Clone the repo

git clone https://github.com/your-username/aipm-book-toolkit.git
cd aipm-book-toolkit


Run the labs

Open /labs/*.ipynb in Google Colab or Jupyter.

Each notebook is linked to a skill in the AIPM exam.

Use the prompts

Explore /prompts/prompts.json.

Ready-to-use in ChatGPT, Claude, or NovelCrafter.

Study with flashcards

Import /flashcards/flashcards.csv into Anki.

Test yourself

/quizzes/chapter_quiz.yaml contains sample exam-style questions.

Online auto-graded quizzes coming soon.

🎯 Exam Alignment

AI Fundamentals → Chapters 1–2

AI Project Life-Cycle → Chapters 4 & 7

Data & Model Governance → Chapter 8

Risk & Ethics → Chapter 9

Strategic Integration → Chapter 10 & Toolkit

Each resource is tagged by domain for easy study navigation.

🤝 Contributing

We welcome improvements and community contributions.

Fork the repo

Create a feature branch (git checkout -b feature-name)

Commit your changes (git commit -m "Added Lab 4")

Push to your branch (git push origin feature-name)

Open a Pull Request

Check the Issues tab for open tasks.

📜 License

Code and notebooks → MIT License

Content (prompts, flashcards, quizzes) → CC-BY-NC 4.0

👉 Use the code freely, but don’t monetize or resell the content.


=======
# AI PM Book – Toolkit

This repository contains scaffolding for all operational assets referenced in the book:
prompts, cheat-sheets, labs (Colab-ready), quizzes, study plans, vendor map, and diagram briefs.

> NOTE: These are *stubs* to get your repo real on day one. Replace TODOs as you draft.


## Scripts Quickstart

```bash
# 1) Monte Carlo velocity (outputs JSON + optional histogram)
python scripts/monte_carlo_velocity.py --velocities 18,22,20,19 --sprints 10000 --plot

# 2) Convert chapter quiz from YAML to JSON
python scripts/quiz_convert.py --in toolkit/quizzes/chapter_quiz.yaml --out toolkit/quizzes/chapter_quiz.json

# 3) Train a simple backlog classifier baseline
python scripts/backlog_classifier_baseline.py --csv sample_backlog.csv --text_col title --label_col label

# 4) Compute fairness metrics by group
python scripts/fairness_metrics.py --csv preds.csv --y_true y --y_pred yhat --group sensitive_attr

# 5) Generate Anki import file from CSV
python scripts/generate_anki_from_csv.py --csv toolkit/anki/flashcards_template.csv --out anki_import.txt
```
>>>>>>> 3b81779 (chore: initial toolkit scaffold (labs, quizzes, prompts, study plan))
