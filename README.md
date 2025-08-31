# Spying-On-Cows 🐄
This project builds a machine learning pipeline to detect lameness in dairy cows using both individual and herd-level behavioral and health sensor data. It explores how changes in the modeling strategy (individual vs. herd) affect performance and interpretability, using Explainable AI techniques.

## Project Overview

Modern dairy farms generate large volumes of behavioral and health for cows. This project addresses the challenges of handling and interpreting this big data by:

- Creating a robust, clean, and consistent dataset from heterogeneous real-world sensor logs
- Building two parallel ML pipelines: one using **individual cow models**, and the other using **herd-level model**
- Applying **oversampling**, **grid search**, **cross-validation**, and **XAI (LIME)** to explore model performance
- Comparing the strengths and limitations of each approach from both herd and individual perspectives.
- Skills in MySQL, Python, Java, Pandas, PyTorch, Scikit-learn.


## Key Results

- **Oversampling improved** individual cow model performance but **degraded** herd model performance
- LIME revealed **distinct feature importance** patterns across individual vs. herd models
- Demonstrated potential for **stacked ensemble models** or **hierarchical modeling** to combine both perspectives
- Identified novel key performacne indicators(water trough behavior at certain times) predictive features and confirmed existing ones(steps))

## Tools & Techniques

- Deep Learning (ANN/DNN)
- Oversampling (SMOTE)
- Ensemble Learning / Bagging-inspired strategies
- Explainable AI (LIME) for ANN/DNN
- Data Cleaning, Aggregation & Wrangling
- Tools: Python, Java, MySQL, Excel(VBA),  Pandas, Scikit-learn, PyTorch

 
 
## Project Structure

```bash
├── Python-ML/ # Pipeline code, pre-processing, model training, explanations evaluation
├── SQL-Files/ # MySQL scripts for Cleaning, Aggregation, Joins & Integrations
├── assets/ # Visual diagrams and screenshots
├── uploaders/ # MySQL conversion from Excel, and Data Cleaning
``` 
