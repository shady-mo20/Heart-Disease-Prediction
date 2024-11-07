import os
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def handle_missing_values(data):
    columns_to_fill = ['BP', 'Cholesterol', 'Max HR', 'ST depression']
    for column in columns_to_fill:
        if column in data.columns:
            if data[column].isnull().sum() > 0:
                mean_value = data[column].mean()
                data[column].fillna(mean_value, inplace=True)
    return data

def encode_categorical_variables(data, encoders_dir='encoders'):
    os.makedirs(encoders_dir, exist_ok=True)
    binary_mapping = {
        'Sex': {'Male': 1, 'Female': 0},
        'FBS over 120': {'Yes': 1, 'No': 0},
        'Exercise angina': {'Yes': 1, 'No': 0},
        'Heart Disease': {'Presence': 1, 'Absence': 0}
    }
    for col, mapping in binary_mapping.items():
        if col in data.columns:
            data[col] = data[col].map(mapping)
    multi_class_features = ['Chest pain type', 'EKG results', 'Slope of ST', 'Thallium']
    encoders = {}
    for col in multi_class_features:
        if col in data.columns:
            ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
            transformed = ohe.fit_transform(data[[col]])
            ohe_columns = [f"{col}_{category}" for category in ohe.categories_[0]]
            transformed_df = pd.DataFrame(transformed, columns=ohe_columns, index=data.index)
            data = pd.concat([data, transformed_df], axis=1).drop(col, axis=1)
            encoders[col] = ohe
            joblib.dump(ohe, os.path.join(encoders_dir, f"{col}_encoder.joblib"))
    return data, encoders

def normalize_numerical_columns(data, scaler_path='models/scaler.pkl'):
    numerical_columns = ['Age', 'BP', 'Cholesterol', 'Max HR', 'ST depression']
    scaler = MinMaxScaler()
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])
    os.makedirs(os.path.dirname(scaler_path), exist_ok=True)
    joblib.dump(scaler, scaler_path)
    return data

def save_preprocessed_data(data, output_path, feature_order_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    feature_order = data.drop('Heart Disease', axis=1).columns.tolist()
    joblib.dump(feature_order, feature_order_path)

def main():
    input_file = 'data/Heart_Disease_Prediction.csv'
    output_file = 'data/Heart_Disease_Prediction_Preprocessed.csv'
    feature_order_path = 'models/feature_order.pkl'
    models_dir = 'models'
    os.makedirs(models_dir, exist_ok=True)
    data = load_data(input_file)
    data = handle_missing_values(data)
    data, encoders = encode_categorical_variables(data)
    data = normalize_numerical_columns(data)
    save_preprocessed_data(data, output_file, feature_order_path)

if __name__ == "__main__":
    main()
