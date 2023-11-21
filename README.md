# Stroke Prediction Project

This project utilizes the Stroke Prediction Dataset from Kaggle, available [here](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data).

**Project Overview:**
- Dataset predicts stroke likelihood based on patient parameters (gender, age, diseases, smoking).
- Objective: Create a machine learning model predicting patients at risk of stroke.

**Impact:**
- Aids doctors in advising high-risk patients and their families in case of emergencies.

**Key Questions:**
1. Distribution of features in the dataset.
2. Impact of age, hypertension, and BMI on stroke likelihood.
3. Influence of smoking on stroke risk.
4. Gender-based differences in stroke likelihood.
5. Relationship between heart problems and strokes.

**Modeling:**
- Developed classification model (Logistic Regression, Decision Tree, Random Forest and XGBoost).
- Logistic Regression Model achieved a recall of 80%, identifying 8 out of 10 patients at risk.
- Drawback: 27% False Positive rate.

**Points for Improvement:**
- Feature engineering on crucial features.
- Modeling try without SMOTE (Synthetic Minority Oversampling Technique).
- Deployment of the predictive model.

This analysis provides valuable insights for doctors to identify and inform patients at risk of stroke, with potential enhancements in feature engineering and model deployment.