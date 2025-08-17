#!/usr/bin/env python3
"""
Backlog Classifier Baseline (Logistic Regression)

Usage:
  python scripts/backlog_classifier_baseline.py --csv sample_backlog.csv --text_col title --label_col label
"""
import argparse, pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--text_col", default="title")
    ap.add_argument("--label_col", default="label")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    X_train, X_test, y_train, y_test = train_test_split(df[args.text_col], df[args.label_col], test_size=0.2, random_state=42)

    vec = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
    Xtr = vec.fit_transform(X_train)
    Xte = vec.transform(X_test)

    clf = LogisticRegression(max_iter=200)
    clf.fit(Xtr, y_train)
    ypred = clf.predict(Xte)

    print(classification_report(y_test, ypred))

if __name__ == "__main__":
    main()
