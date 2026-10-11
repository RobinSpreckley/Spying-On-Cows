# Spying on Cow(s) 🐄

**BSc dissertation, University of Glasgow · with the Langhill dairy herd · top mark in the year**

Can machine learning detect lameness in dairy cows from the data farms already collect, and does a model for each cow see things a whole-herd model misses?

Langhill records water-trough visits, milkings, weights, body condition and lactation history for every cow. This project turns six years of those records into a lameness dataset. It then trains explainable neural networks for each cow and for the herd, and compares what each one learns.

> The farm data is not included, under the data-sharing agreement.

## Pipeline

<p align="center">
  <img src="https://raw.githubusercontent.com/RobinSpreckley/Spying-On-Cows/main/assets/aggregation%20and%20integration%20(2).png" alt="Aggregation and integration steps" width="700"/>
</p>

1. **Clean and load.** Excel and Python regular expressions fix typos, hidden spaces, conflicting date formats and constant columns. Java uploaders (`uploaders/`) then load each file into its own MySQL table, with types and keys.
2. **Clean in SQL** (`SQL Files/`):
   - Remove duplicates and impossible values, such as negative water intake caused by troughs refilling mid-drink.
   - Remove the feed groups and cows the herd asked to exclude.
   - Keep only cows with at least 80 records, within 2011–2017, when all files overlap.
3. **Feature engineering.** For every lameness (locomotion) score:
   - **No future data:** every sensor stream is summarised over the 7 days before the score (count, mean, std, min, max, sum), never using later readings. Scores are taken on weekdays, so a 7-day window is built for every possible end day.
   - **Zeros handled case by case:** a milking slot that never happened is left out, but a trough visit with no drinking is kept.
   - **Derived features:** days into lactation, age, season and time spent drinking.
4. **Integrate.** Weekly data is left-joined to the scores, then joined to lactation and pedigree data. The result is 100+ features over 24,500 rows.
5. **Model** (`Python-ML/`):
   - Scores 1–2 are labelled healthy and 3–5 lame.
   - Imputation, scaling and one-hot encoding run inside a scikit-learn pipeline.
   - An MLP neural network is tuned with grid search and cross-validation.
   - This is run per cow and for the whole herd on the same train/test split, with and without SMOTE-NC oversampling.
6. **Explain.**
   - LIME submodular pick on every model.
   - Three iterations of feature-importance charts.
   - Word clouds counting which features matter across all the per-cow models.

## Results

| Model | F1 | Precision | Recall | Accuracy |
|---|---|---|---|---|
| Per-cow | 0.546 | 0.559 | 0.533 | 0.711 |
| Per-cow + SMOTE | 0.552 | 0.561 | 0.542 | 0.713 |
| Herd | 0.571 | 0.614 | 0.533 | 0.739 |
| Herd + SMOTE | 0.567 | 0.610 | 0.530 | 0.736 |

<sub>Scores on all the test data combined.</sub>

- **The herd model scores best overall, but drops the most when judged cow by cow.** Its high accuracy partly comes from predicting "healthy" for most cows.
- **Oversampling helps the per-cow models but hurts the herd model overall.** This suggests each cow's patterns differ, and synthetic data blurs them when the cows are pooled.
- **The two approaches use different signals.**
  - Per-cow models lean on how *consistent* a cow is, especially the standard deviation of its milking times. The herd model misses this.
  - The herd model relies more on averages, such as milking duration and days since birth.
- **Explainability caught bad shortcuts.** Some high-scoring models were relying on the calendar year, the day of the week or who did the scoring. Removing day of the week improved the weaker models.
- **Next step:** combine per-cow and herd models (stacking or hierarchical modelling).

## Repository layout

```
├── Python-ML/     Pipelines (per-cow / herd, with / without SMOTE), LIME, correlation analysis
├── SQL Files/     Cleaning, weekly aggregation and join queries
├── uploaders/     Java Excel-to-MySQL uploaders, one per source file
└── assets/        Diagrams
```

## Tools

Python · scikit-learn · imbalanced-learn (SMOTE-NC) · LIME · Pandas · NumPy · Matplotlib · Seaborn · MySQL · Java · Excel

## Acknowledgements

Supervised by Dr Lito Michala. Data provided by the Langhill herd (SRUC).
