# Heart Disease Prediction Project

## Overview
This project utilizes machine learning techniques to predict the likelihood of heart disease based on various medical and lifestyle factors. Multiple models were trained and evaluated, with a focus on data exploration, feature selection, and predictive modeling using an Artificial Neural Network (ANN).

## Dataset
The dataset includes health indicators such as BMI, smoking status, alcohol consumption, stroke history, physical activity levels, and more.

### Sample Data (First 10 Rows)
| HeartDisease | BMI  | Smoking | AlcoholDrinking | Stroke | PhysicalHealth | MentalHealth | DiffWalking | Sex    | AgeCategory | Race  | Diabetic | PhysicalActivity | GenHealth | SleepTime | Asthma | KidneyDisease | SkinCancer |
|--------------|------|---------|-----------------|--------|----------------|--------------|-------------|--------|-------------|-------|----------|------------------|-----------|-----------|--------|---------------|------------|
| No           | 16.6 | Yes     | No              | No     | 3              | 30           | No          | Female | 55-59       | White | Yes      | Yes              | Very good | 5         | Yes    | No            | No         |
| No           | 24.21| No      | No              | No     | 0             | 0            | No          | Female | 75-79       | White | No       | No               | Good      | 6         | No     | No            | Yes        |
| No           | 24.21| No      | No              | No     | 0             | 0            | No          | Female | 75-79       | White | No       | No               | Good      | 6         | No     | No            | Yes        |
| No           | 31.64| Yes     | No              | No     | 5             | 0            | No          | Female | 80+         | White | No       | Yes              | Good      | 8         | No     | No            | No         |
| Yes          | 28.87| No      | No              | No     | 15            | 3            | Yes         | Male   | 70-74       | Black | Yes      | No               | Poor      | 5         | No     | No            | No         |
| Yes          | 32.98| Yes     | No              | Yes    | 10            | 15           | Yes         | Male   | 60-64       | Asian | Yes      | Yes              | Fair      | 8         | No     | No            | Yes        |
| No           | 21.63| No      | No              | No     | 15            | 0            | No          | Female | 70-74       | White | No       | Yes              | Fair      | 4         | Yes    | No            | Yes        |
| No           | 28.55| Yes     | No              | No     | 2             | 10           | Yes         | Male   | 60-64       | Asian | Yes      | Yes              | Good      | 8         | No     | No            | No         |
| No           | 26.78| No      | Yes             | No     | 3             | 0            | No          | Female | 65-69       | White | Yes      | Yes              | Good      | 7         | No     | Yes           | No         |
| No           | 21.63| No      | No              | No     | 15            | 0            | No          | Female | 70-74       | White | No       | Yes              | Fair      | 4         | Yes    | No            | Yes        |

This data contains various medical and lifestyle information relevant for predicting heart disease.

## Exploratory Data Analysis (EDA)
Exploratory Data Analysis included identifying key relationships through visualizations, correlation heatmaps, and statistical tests. Detailed analysis is available in the [EDA Report](https://github.com/shady-mo20/Heart-Disease-Prediction/blob/main/Heart%20disease%20prediction%20EDA%20Report.docx).

## Feature Engineering & Selection
Categorical features were encoded numerically, and the dataset was balanced using NearMiss. 

## Modeling
Several models were trained, with emphasis on an Artificial Neural Network (ANN):
- Logistic Regression
- Random Forest
- XGBoost
- Support Vector Machine (SVM)
- ANN (128 → Dropout → 64 → Dropout → 32 neurons)

## Prediction
Predictions for new patients utilize the ANN model:
```python
patient_data = {"BMI": 28, "Smoking": 1, "AlcoholDrinking": 0, ...}
prediction = predict_new_patient(ann_model, scaler, selected_features, patient_data)
```
See [Patient Symptoms Table](https://github.com/shady-mo20/Heart-Disease-Prediction/blob/main/Patient_Symptoms_Table.docx).

---

### Contributor
- **Shady Mohamed** ([shady-mo20](https://github.com/shady-mo20))

### Repository
[Heart Disease Prediction](https://github.com/shady-mo20/Heart-Disease-Prediction)
