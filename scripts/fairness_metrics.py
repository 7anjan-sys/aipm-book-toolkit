#!/usr/bin/env python3
"""
Simple Fairness Metrics

Usage:
  python scripts/fairness_metrics.py --csv preds.csv --y_true y --y_pred yhat --group sensitive_attr
CSV must include columns: y (0/1), yhat (0/1), sensitive_attr.
"""
import argparse, pandas as pd

def rate(df, col):
    return df[col].mean()

def tpr(df, y_true="y", y_pred="yhat"):
    tp = ((df[y_true]==1) & (df[y_pred]==1)).sum()
    pos = (df[y_true]==1).sum()
    return tp/pos if pos else 0.0

def fpr(df, y_true="y", y_pred="yhat"):
    fp = ((df[y_true]==0) & (df[y_pred]==1)).sum()
    neg = (df[y_true]==0).sum()
    return fp/neg if neg else 0.0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--y_true", default="y")
    ap.add_argument("--y_pred", default="yhat")
    ap.add_argument("--group", default="group")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    print("Groups:", df[args.group].unique().tolist())
    for g, sub in df.groupby(args.group):
        print(f"\n== Group: {g} ==")
        print("TPR:", round(tpr(sub, args.y_true, args.y_pred), 3))
        print("FPR:", round(fpr(sub, args.y_true, args.y_pred), 3))

if __name__ == "__main__":
    main()
