# Heart Disease Prediction

## Overview
This project aims to predict the likelihood of heart disease based on various health indicators. Using machine learning models, including Logistic Regression, Random Forest, XGBoost, Support Vector Machine (SVM), and Artificial Neural Networks (ANN), we analyze patient data to provide insights into heart disease risks.

## Dataset
The dataset contains multiple health-related features such as BMI, smoking status, alcohol consumption, stroke history, and physical activity levels.

### Sample Data (First 10 Rows)
```python
import pandas as pd

# Load Data
file_path = "Heart Disease.xlsx"
data = pd.read_excel(file_path)

# Display First 10 Rows
data.head(10)
```
The dataset contains categorical and numerical features, including:
- **BMI**: Body Mass Index
- **Smoking**: Whether the person smokes or not
- **AlcoholDrinking**: Alcohol consumption status
- **Stroke**: History of stroke
- **PhysicalActivity**: Engagement in physical activity
- **AgeCategory**: Age group classification
- **Diabetic**: Diabetes status
- **HeartDisease**: Target variable (Yes/No)

## Exploratory Data Analysis (EDA)
The EDA process included:
1. **Data Distribution Analysis**: Examined the spread of features using histograms and box plots.
2. **Correlation Analysis**: Identified key relationships between features using heatmaps.
3. **Categorical Feature Analysis**: Compared categorical variables with heart disease incidence.
4. **Outlier Detection and Removal**: Used IQR to filter extreme values.

### Sample Graphs
#### Alcohol Consumption vs Heart Disease
```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
sns.countplot(x=data["AlcoholDrinking"], hue=data["HeartDisease"])
plt.title("Alcohol Drinking vs Heart Disease")
plt.xlabel("Alcohol Drinking")
plt.ylabel("Count")
plt.legend(title="Heart Disease")
plt.show()
```
This graph shows the relationship between alcohol consumption and heart disease, indicating a potential correlation.

More detailed EDA analysis can be found in the full **EDA Report**: [EDA Report](https://github.com/shady-mo20/Heart-Disease-Prediction/blob/main/Heart%20disease%20prediction%20EDA%20Report.docx)

## Feature Engineering & Selection
- **Categorical Encoding**: Used `LabelEncoder` to transform categorical values.
- **Balancing Data**: Applied `NearMiss` technique to address class imbalance.
- **Feature Importance Analysis**: Selected the most relevant features for model training.

## Machine Learning Models
### 1. Traditional Models
We trained the following models:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- Support Vector Machine (SVM)

Each model was evaluated using classification reports and accuracy metrics.

### 2. Artificial Neural Network (ANN)
An ANN was implemented using TensorFlow/Keras with the following architecture:
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])
```
The model was compiled with the Adam optimizer and trained for 50 epochs.

## Patient Symptom Analysis
A detailed **Patient Symptoms Table** is available: [Patient Symptoms Table](https://github.com/shady-mo20/Heart-Disease-Prediction/blob/main/Patient_Symptoms_Table.docx)

## Predictions
A function was implemented to predict heart disease for a new patient based on input features. Example:
```python
patient_data = {
    "BMI": 28,
    "Smoking": 1,
    "AlcoholDrinking": 0,
    "Stroke": 0,
    "PhysicalHealth": 5,
    "MentalHealth": 3,
    "DiffWalking": 0,
    "Sex": 1,
    "AgeCategory": 5,
    "Race": 2,
    "Diabetic": 0,
    "PhysicalActivity": 1,
    "GenHealth": 2,
    "SleepTime": 6,
    "Asthma": 0,
    "KidneyDisease": 0,
    "SkinCancer": 0
}
```
The model returns a **Heart Disease** or **No Heart Disease** prediction.

## Conclusion
This project successfully predicts heart disease using various machine learning models. Further improvements can be made by:
- Expanding the dataset for better generalization.
- Hyperparameter tuning for increased accuracy.
- Deploying the model as an API for real-world applications.

---
### Contributors
- **Shady Mohamed** (GitHub: [shady-mo20](https://github.com/shady-mo20))

For more details, refer to the project repository: [Heart Disease Prediction](https://github.com/shady-mo20/Heart-Disease-Prediction).
