# Spying-On-Cows 🐄
## About
This project builds a machine learning pipeline to detect lameness in dairy cows using both individual and herd-level behavioral and health sensor data. It explores how changes in the modeling strategy (individual vs. herd) affect performance and interpretability, using Explainable AI techniques.

## High-Level Overview

Modern dairy farms generate large volumes of behavioral and health for cows. This project addresses the challenges of handling and interpreting this big data by:

- Creating a robust, clean, and consistent dataset from heterogeneous real-world sensor logs
- Creating new attributes from aggregations, min, max and std to find new KPI
- Building two parallel ML pipelines: one using **individual cow models**, and the other using **herd-level model**
- Applying **oversampling**, **grid search**, **cross-validation**, and **XAI (LIME)** to explore model performance
- Conducted Data Mining to continually improve feature seclection with visulisations
- Comparing the strengths and limitations of each approach from both herd and individual perspectives.
- Skills in MySQL, Python, Java, Pandas, PyTorch, Scikit-learn.


## Key Results

- **Oversampling improved** individual cow model performance but **degraded** herd model performance
- LIME revealed **distinct feature importance** patterns across individual vs. herd models
- Demonstrated potential for **stacked ensemble models** or **hierarchical modeling** to combine both perspectives
- Identified new key performacne indicators predictive features(watertrough intake at certain times) and confirmed existing ones(number of steps). 

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
