from src.data_preprocessing import load_data, remove_outliers
from src.eda import perform_eda
from src.feature_selection import feature_selection
from src.model import train_models
from src.prediction import predict_new_patient
from sklearn.model_selection import train_test_split
import warnings
import joblib
import os

warnings.filterwarnings('ignore')

def main():
    data = load_data('/home/shosh/Desktop/NTI projects /heart-disease-prediction/data/Heart Disease.xlsx')
    data = remove_outliers(data)
    
    perform_eda(data)
    X_selected, y = feature_selection(data)
    
    X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.25, random_state=42)
    results, ann_model = train_models(X_train, y_train, X_test, y_test)
    
    scaler_path = "/home/shosh/Desktop/NTI projects/heart-disease-prediction/Models/scaler.pkl"
    
    if os.path.exists(scaler_path):
        scaler = joblib.load(scaler_path)
        print("Scaler loaded successfully")
    else:
        print(f"Scaler file not found at {scaler_path}")
        return  
    
    patient_data_sick = {
        "BMI": 60,
        "Smoking": 0,
        "AlcoholDrinking": 1,
        "Stroke": 1,
        "PhysicalHealth": 30,
        "MentalHealth": 30,
        "DiffWalking": 1,
        "Sex": 1,
        "AgeCategory": 9,
        "Race": 1,
        "Diabetic": 1,
        "PhysicalActivity": 0,
        "GenHealth": 0,
        "SleepTime": 4,
        "Asthma": 1,
        "KidneyDisease": 1,
        "SkinCancer": 1
    }
    
    prediction = predict_new_patient(ann_model, scaler, list(X_selected.columns), patient_data_sick)
    print(f"Prediction for patient: {'Heart Disease' if prediction else 'No Heart Disease'}")

if __name__ == "__main__":
    main()