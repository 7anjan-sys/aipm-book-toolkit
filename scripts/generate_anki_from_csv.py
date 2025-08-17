#!/usr/bin/env python3
"""
Generate Anki .txt from CSV

Usage:
  python scripts/generate_anki_from_csv.py --csv toolkit/anki/flashcards_template.csv --out anki_import.txt

Output format: 'Front\tBack\tTags' per line (tab-separated).
"""
import argparse, csv

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with open(args.csv, "r", encoding="utf-8") as f, open(args.out, "w", encoding="utf-8") as out:
        reader = csv.DictReader(f)
        for row in reader:
            out.write(f"{row['Front']}\t{row['Back']}\t{row.get('Tags','')}\n")
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
