#!/usr/bin/env python3
"""
Quiz YAML → JSON Converter

Input YAML schema:
questions:
  - q: "What is precision?"
    options: ["A","B","C","D"]
    answer: "A"
    rationale: "because ..."

Usage:
  python scripts/quiz_convert.py --in toolkit/quizzes/chapter_quiz.yaml --out toolkit/quizzes/chapter_quiz.json
"""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--out", dest="out_path", required=True)
    args = ap.parse_args()

    try:
        import yaml  # PyYAML
    except Exception:
        print("Please install pyyaml: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    with open(args.in_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    out = {
        "schema": "aipm.quiz.v1",
        "chapter": data.get("chapter", "X"),
        "questions": data.get("questions", [])
    }
    with open(args.out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {args.out_path}")

if __name__ == "__main__":
    main()
