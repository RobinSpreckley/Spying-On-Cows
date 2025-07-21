# Spying-On-Cows 
The project also aims to make an effective machine learning predictive model from a herd and cow perspective and explains what attributes are used in both.
 
This project implements databases, machine learning models, and Explainable artificial intelligence, to detect lameness effectively while showing how it classifies lameness. It looks at this problem from data of the individual cows and the herd data as a whole, to compare how these models predict lameness. It also sees how changes will affect both strategies.

## 🎯 Project Overview

Modern dairy farms generate large volumes of behavioral and health data from individual cows. This project addresses the challenges of handling and interpreting this big data by:

- Creating a robust, clean, and consistent dataset from heterogeneous real-world sensor logs
- Building two parallel ML pipelines: one using **individual cow models**, and the other using **herd-level aggregation**
- Applying **oversampling**, **grid search**, **cross-validation**, and **XAI (LIME)** to explore model performance
- Comparing the strengths and limitations of each approach from both herd and individual perspectives
- 
## 🔍 What This Project Demonstrates

- Development of a custom ML pipeline for predictive health monitoring.
- Data integration from multiple sources and timeframes.
- Use of ensemble learning and hierarchical modeling techniques.
- Interpretability of model predictions using LIME.
- Skills in MySQL, Python, Java, Pandas, PyTorch, Scikit-learn.


## 📌 Key Results

- **Oversampling improved** individual cow model performance but **degraded** herd model performance
- LIME revealed **distinct feature importance** patterns across individual vs. herd models
- Demonstrated potential for **stacked ensemble models** or **hierarchical modeling** to combine both perspectives
- Identified novel predictive features and confirmed domain-specific ones (e.g., cow movement, water trough behavior)

# Skills Used
Deep learning, ANN/DNN. 
A unique implementation inspired by bagging and hierchal modeling to develop an ml system that takes into the cow and herd data. 
Oversampling
Extensive use of Excel, Pandas, Java, MySQL, to data clean, aggregate
Creation of dataset
Exten
Created explain ai with Lime, Pytorch, Sklearn

# Features
(Put technolgoies used here - e.g. what type of database, what coding languages were used, what machine learning algorithms, etc.)
Database Systems (MySQL)
Python and Java Data Cleaning, Wrangling Aggregating, pipeline
Excel formatting
XAI(Lime) 
Artifiial Bagging inspired split strategy

#   Spying On Cows Dataset
Data

<p align="center">
  <img src="assets/simpleoutline.JPG" alt="On-Orbit ML diagram" width="400"/>
  <br>
  <b>Figure:</b> Took in data from many sources of sensor recording and formatted to work in a consistent time frame for prediction  .
</p> 

<p align="center">
  <img src="assets/aggregation and integration (2).png" alt="On-Orbit ML diagram" width="400"/>
  <br>
  <b>Figure:</b> Left – challenges with traditional satellite data collection; Right – benefits of On-Orbit processing using edge ML.
</p>

# ML Pipeline

<p align="center">
  <img src="assets/splitdata.JPG" alt="On-Orbit ML diagram" width="400"/>
  <br>
  <b>Figure:</b> Left – challenges with traditional satellite data collection; Right – benefits of On-Orbit processing using edge ML.
</p>

Creation of Dataset pipeline, Sklearn, Pytorch, 


# add XAI with a screen shot

<p align="center">
  <img src="assets/pipeline.JPG" alt="On-Orbit ML diagram" width="400"/>
  <br>
  <b>Figure:</b> Left – challenges with traditional satellite data collection; Right – benefits of On-Orbit processing using edge ML.
</p>
<p align="center">
  <img src="assets/modelflow.JPG" alt="On-Orbit ML diagram" width="400"/>
  <br>
  <b>Figure:</b> Left – challenges with traditional satellite data collection; Right – benefits of On-Orbit processing using edge ML.
</p>


 
## 📁 Project Structure

```bash
├── Python-ML/ # Pipeline code, model training, evaluation
├── SQL-Files/ # MySQL scripts for data aggregation
├── assets/ # Visual diagrams and screenshots
├── uploaders/ # Data handling scripts
``` 

 
## Model Evaluation

- Measured metrics include mAP50, Recall, and feature importance.
- Comparison between individual vs herd-based prediction strategies.
- Visualised explanations with LIME to show model trust and reliability.
