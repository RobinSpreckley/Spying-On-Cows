# Spying-On-Cows 🐄
## About

Modern dairy farms generate large volumes of behavioral and health for cows. This project explains and explores the current problems and solutions to using big data with ML and how it is being dealt with in the dairy industry.

## High-Level Overview
 
- Creates a robust, clean, and consistent dataset from heterogeneous real-world sensor logs
- Creates new attributes from aggregations, min, max and std to find new KPI(key performacne indicators)
- Builds two parallel ML pipelines: one using **individual cow models**, and the other using **herd-level model**
- Applies **oversampling**, **grid search**, **cross-validation**, and **XAI (LIME)** to explore model performance
- Conducts Data Mining to continually improve feature seclection with visulisations
- Compares the strengths and limitations of each approach from both herd and individual perspectives.

## Key Results

- **Oversampling improved** individual cow model performance but **degraded** herd model performance
- LIME revealed **distinct feature importance** patterns across individual vs. herd models
- This shows potential for **stacked ensemble models** or **hierarchical modeling** to combine both perspectives
- Identified new KPI predictive features(standard deviation in watertrough drinkiing in the evenings) and confirmed existing ones(number of steps). 

## Tools & Techniques

- Deep Learning (ANN/DNN)
- Oversampling (SMOTE)
- Ensemble Learning / Bagging-inspired strategies
- Explainable AI (LIME) for ANN/DNN
- Data Cleaning, Aggregation & Wrangling
- Tools: Python, Java, MySQL, Excel(VBA),  Pandas, Scikit-learn, PyTorch, Seaborn, Matplotlib

 
 
## Project Structure

```bash
├── Python-ML/ # Pipeline code, pre-processing, model training, explanations evaluation
├── SQL-Files/ # MySQL scripts for Cleaning, Aggregation, Joins & Integrations
├── assets/ # Visual diagrams and screenshots
├── uploaders/ # MySQL conversion from Excel, and Data Cleaning
``` 
