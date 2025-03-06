# **Heart Disease Prediction**

This project aims to develop a predictive model to assess the likelihood of heart disease in patients using **Artificial Neural Networks (ANN)**. The dataset contains medical records with key health indicators. The project includes **Exploratory Data Analysis (EDA)**, data visualization, and model training to make accurate predictions.

---

## **Project Structure**

- `data/`: Contains the dataset used for training and testing.
- `src/`: Includes scripts for **EDA**, preprocessing, and model training.
- `models/`: Stores trained models.
- `main.py`: The main script to execute the project.
- `requirements.txt`: Lists the dependencies required to run the project.

---

## **Dataset Overview**

The dataset contains medical records of patients, with features that can be used to predict heart disease.

### **Sample Data (First 10 Rows)**

| Age | Sex | BP  | Cholesterol | Blood Sugar | ECG | Max HR | Angina | ST Depression | Vessels | Thal | Target |
|----|----|----|------------|------------|----|------|------|------------|--------|----|--------|
| 63 | 1  | 145 | 233        | 1          | 2  | 150  | 0    | 2.3        | 0      | 6  | 1      |
| 37 | 1  | 130 | 250        | 0          | 0  | 187  | 0    | 3.5        | 0      | 3  | 0      |
| 41 | 0  | 130 | 204        | 0          | 2  | 172  | 0    | 1.4        | 0      | 3  | 0      |
| 56 | 1  | 120 | 236        | 0          | 0  | 178  | 0    | 0.8        | 0      | 3  | 0      |
| 57 | 0  | 120 | 354        | 0          | 0  | 163  | 1    | 0.6        | 0      | 3  | 1      |
| 57 | 1  | 140 | 192        | 0          | 0  | 148  | 0    | 0.4        | 0      | 1  | 0      |
| 56 | 0  | 140 | 294        | 0          | 2  | 153  | 0    | 1.3        | 0      | 2  | 0      |
| 44 | 1  | 120 | 263        | 0          | 0  | 173  | 0    | 0.0        | 0      | 7  | 0      |
| 52 | 1  | 172 | 199        | 1          | 0  | 162  | 0    | 0.5        | 0      | 7  | 0      |
| 57 | 1  | 150 | 168        | 0          | 0  | 174  | 0    | 1.6        | 0      | 3  | 0      |

### **Feature Explanation:**
- **Age**: Patient's age.
- **Sex**: 1 = Male, 0 = Female.
- **BP (Blood Pressure)**: Systolic blood pressure (mmHg).
- **Cholesterol**: Cholesterol level (mg/dL).
- **Blood Sugar**: 1 = Fasting blood sugar > 120 mg/dL, 0 = Otherwise.
- **ECG**: Electrocardiogram results.
- **Max HR**: Maximum heart rate achieved.
- **Angina**: 1 = Exercise-induced angina, 0 = No angina.
- **ST Depression**: Depression of ST segment during exercise.
- **Vessels**: Number of major vessels colored by fluoroscopy (0-3).
- **Thal**: Thallium stress test results.
- **Target**: 1 = Presence of heart disease, 0 = Absence.

---

## **Exploratory Data Analysis (EDA)**

- Performed statistical analysis to understand the data distribution.
- Visualized correlations between different features using heatmaps.
- Identified potential patterns in heart disease occurrence.

📄 **EDA Report:** [Heart Disease EDA Report](https://github.com/shady-mo20/Heart-Disease-Prediction/blob/main/Heart%20disease%20prediction%20EDA%20Report.docx)

📄 **Patient Symptoms Table:** [Patient Symptoms Table](https://github.com/shady-mo20/Heart-Disease-Prediction/blob/main/Patient_Symptoms_Table.docx)

---

## **Model Training**

- Used **Artificial Neural Networks (ANN)** with multiple hidden layers.
- Optimized using **Adam optimizer**.
- Applied **ReLU activation** in hidden layers and **Sigmoid activation** in the output layer.
- Evaluated the model using accuracy, precision, recall, and F1-score.

---

## **How to Run the Project**

### **1. Clone the Repository**
```bash
git clone https://github.com/shady-mo20/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

### **2. Set Up Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
```bash
python main.py
```

---
