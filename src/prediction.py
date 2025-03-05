import joblib
import numpy as np
from tensorflow.keras.models import load_model

import warnings
warnings.filterwarnings('ignore')


def predict_new_patient(ann_model, scaler, selected_features, patient_data):
    patient_selected = np.array([[patient_data[feature] for feature in selected_features]])
    patient_scaled = scaler.transform(patient_selected)
    ann_pred = (ann_model.predict(patient_scaled) > 0.5).astype(int)[0][0]
    
    return ann_pred
