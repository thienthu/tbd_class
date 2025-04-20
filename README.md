# 🧬 Protein Localization Challenge  
*Machine Learning for Life Sciences – Project 2 (2023–2024)*  
Ghent University

## 🧠 Overview

This project is part of the *Machine Learning for Life Sciences* course at Ghent University. The goal is to develop a machine learning model to solve a **multi-label classification** task: predicting the **localization of proteins** across **10 different classes**.

Each protein may belong to **one or more** localization classes, making this a non-trivial problem with challenges in both prediction performance and calibration.

## 🎯 Objectives

- Build a model that predicts one or more protein localization classes.
- Evaluate the model using **macro F1 score**.
- Perform **model calibration analysis** (optional but recommended).
- Provide a well-documented Jupyter notebook for project defense.

## 📊 Data & Task

The dataset and competition details are hosted on Kaggle:  
🔗 [Join the competition here](https://www.kaggle.com/t/1f0d7c03c7994f55a63662e4e4496a90)

- **Labels**: Multi-label (10 possible protein localization classes)  
- **Evaluation metric**: Macro F1 score

## 🧪 Key Steps

1. **Exploratory Data Analysis (EDA)**  
   Understand data distribution, label frequency, correlations, and class imbalance.

2. **Feature Engineering & Preprocessing**  
   - Encode features as needed (e.g. categorical → one-hot or embeddings).
   - Handle missing data and standardize inputs.

3. **Model Training**  
   Explore and compare various classification models such as:
   - Logistic Regression (baseline)
   - Random Forest / XGBoost
   - Multi-label Neural Networks

4. **Model Evaluation**  
   - Use **macro F1 score** to assess performance.
   - Apply proper cross-validation strategies suitable for multi-label classification.

5. **Model Calibration (Optional Task)**  
   - Generate **calibration curves** per label.
   - Calculate **Expected Calibration Error (ECE)** per class.
   - Analyze how confidence scores reflect true likelihoods.

6. **Discussion & Reporting**  
   - Document what worked and what didn’t.
   - Provide reasoning for modeling decisions.
   - Highlight limitations and potential improvements.

## 📊 Model
Model is store in 🔗[google_drive_link](https://drive.google.com/drive/folders/1pJ9gTCvN_JPkg0XLqHmT_oSMTSKMGfIq?usp=sharing)

## 📝 Author
- **Author**: Thu Nguyen.
- **Disclaimer**: This project was developed as part of the Machine Learning for Life Sciences course at Ghent University.

