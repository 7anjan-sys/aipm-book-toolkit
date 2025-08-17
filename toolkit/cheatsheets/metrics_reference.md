# Metrics Reference

| Metric | What it means | When to use | Pitfalls |
|---|---|---|---|
| Precision | Of predicted positives, how many were correct | High-cost false positives | Can ignore false negatives |
| Recall | Of actual positives, how many were found | High-cost false negatives | Can inflate with many positives |
| F1 | Balance of precision/recall | Imbalanced classes | Hides class-wise issues |
