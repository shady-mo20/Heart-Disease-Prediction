import joblib
import os
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import warnings
warnings.filterwarnings('ignore')

def save_model(model, model_name, path):
    models_path = os.path.join(path, 'Models') 
    if not os.path.exists(models_path):
        os.makedirs(models_path) 
    joblib.dump(model, os.path.join(models_path, f"{model_name}.pkl"))
    print(f"Model saved as {os.path.join(models_path, f'{model_name}.pkl')}")

def train_models(X_train, y_train, X_test, y_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model_path = "heart-disease-prediction" 
    
    save_model(scaler, "scaler", model_path)
    
    models = {
        "Logistic Regression": LogisticRegression(),
        "Random Forest": RandomForestClassifier(),
        "XGBoost": XGBClassifier(),
        "Support Vector Machine": SVC(kernel='linear')
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        results[name] = classification_report(y_test, y_pred)
    
    ann_model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    
    ann_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    history = ann_model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_data=(X_test_scaled, y_test), verbose=1)
    
    
    ann_model.save(os.path.join(model_path, "Models", "ann_model.h5"))  
    save_model(ann_model, "ann_model", model_path)  
    
    return results, ann_model
