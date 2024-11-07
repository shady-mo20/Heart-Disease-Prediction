import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_preprocessed_data(file_path):
    data = pd.read_csv(file_path)
    return data

def train_model(X_train, y_train):
    model = XGBClassifier(eval_metric='logloss')
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")

def save_model(model, file_path):
    joblib.dump(model, file_path)

def main():
    preprocessed_data_file = 'data/Heart_Disease_Prediction_Preprocessed.csv'
    model_file = 'models/best_xgb_model.pkl'
    data = load_preprocessed_data(preprocessed_data_file)
    if 'Heart Disease' not in data.columns:
        raise Exception("Target column 'Heart Disease' is missing from the data.")
    X = data.drop('Heart Disease', axis=1)
    y = data['Heart Disease']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model, model_file)

if __name__ == "__main__":
    main()
