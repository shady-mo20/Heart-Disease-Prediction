import os
import time
import pandas as pd
import joblib
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Heart Disease Prediction",
    layout="wide",
    page_icon="❤️"
)

MODELS_DIR = 'models'
ENCODERS_DIR = 'encoders'
IMAGES_DIR = 'images'

@st.cache_resource(show_spinner=False)
def load_resources():
    progress_bar = st.progress(0)
    model_path = os.path.join(MODELS_DIR, 'best_xgb_model.pkl')
    scaler_path = os.path.join(MODELS_DIR, 'scaler.pkl')
    feature_order_path = os.path.join(MODELS_DIR, 'feature_order.pkl')
    
    model = joblib.load(model_path)
    progress_bar.progress(33)
    time.sleep(0.5)
    
    scaler = joblib.load(scaler_path)
    progress_bar.progress(66)
    time.sleep(0.5)
    
    feature_order = joblib.load(feature_order_path)
    progress_bar.progress(100)
    time.sleep(0.5)
    
    encoders = {}
    for filename in os.listdir(ENCODERS_DIR):
        if filename.endswith('_encoder.joblib'):
            feature_name = filename.replace('_encoder.joblib', '')
            encoder_path = os.path.join(ENCODERS_DIR, filename)
            encoders[feature_name] = joblib.load(encoder_path)
    
    return model, scaler, feature_order, encoders

model, scaler, feature_order, encoders = load_resources()
st.sidebar.success("All resources loaded successfully.")

for feature, encoder in encoders.items():
    st.sidebar.write(f"**{feature}** Categories: {list(encoder.categories_[0])}")

def encode_input(input_data, encoders):
    categorical_features = ['Chest pain type', 'EKG results', 'Slope of ST', 'Thallium']
    for feature in categorical_features:
        if feature in encoders:
            encoder = encoders[feature]
            transformed = encoder.transform(input_data[[feature]])
            ohe_columns = [f"{feature}_{category}" for category in encoder.categories_[0]]
            transformed_df = pd.DataFrame(transformed, columns=ohe_columns, index=input_data.index)
            input_data = pd.concat([input_data, transformed_df], axis=1).drop(feature, axis=1)
    return input_data

def preprocess_input(input_data, scaler, feature_order):
    numerical_features = ['Age', 'BP', 'Cholesterol', 'Max HR', 'ST depression']
    input_data[numerical_features] = scaler.transform(input_data[numerical_features])
    input_data = input_data.reindex(columns=feature_order, fill_value=0)
    return input_data

def predict_heart_disease(input_data):
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1]
    return prediction, prediction_proba

options = st.sidebar.radio("Navigation", ["Predict Heart Disease", "About"])

if options == "Predict Heart Disease":
    header_image_path = os.path.join(IMAGES_DIR, "Heart-Disease.jpg")
    if os.path.exists(header_image_path):
        st.image(Image.open(header_image_path), use_column_width=True)
    
    st.title("❤️ Heart Disease Prediction")
    st.write("### Get an instant assessment of your heart health by providing the following details.")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input(
                "Age",
                min_value=1,
                max_value=120,
                value=50,
                step=1,
                help="Please enter your current age in years."
            )
            sex_input = st.selectbox(
                "Sex",
                options=["Male", "Female"],
                help="Select your biological sex."
            )
            sex = 1 if sex_input == "Male" else 0
            cp = st.selectbox(
                "Chest Pain Type",
                options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"],
                help="Select the type of chest pain you experience."
            )
            bp = st.number_input(
                "Blood Pressure (BP)",
                min_value=50,
                max_value=300,
                value=120,
                step=1,
                help="Enter your systolic blood pressure in mm Hg."
            )
            chol = st.number_input(
                "Cholesterol",
                min_value=100,
                max_value=600,
                value=200,
                step=1,
                help="Enter your blood cholesterol level in mg/dL."
            )
        with col2:
            fbs_input = st.selectbox(
                "Fasting Blood Sugar > 120 mg/dl?",
                options=["Yes", "No"],
                help="Indicate if your fasting blood sugar is greater than 120 mg/dL."
            )
            fbs = 1 if fbs_input == "Yes" else 0
            ekg = st.selectbox(
                "EKG Results",
                options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"],
                help="Select the results of your EKG test."
            )
            max_hr = st.number_input(
                "Max Heart Rate (Max HR)",
                min_value=60,
                max_value=250,
                value=150,
                step=1,
                help="Enter the maximum heart rate achieved during physical activity."
            )
            exang_input = st.selectbox(
                "Exercise Induced Angina?",
                options=["Yes", "No"],
                help="Indicate if you experience angina during exercise."
            )
            exang = 1 if exang_input == "Yes" else 0
            st_depression = st.number_input(
                "ST Depression",
                min_value=0.0,
                max_value=10.0,
                value=1.0,
                step=0.1,
                help="Enter the amount of ST depression observed during the test."
            )
        slope = st.selectbox(
            "Slope of the Peak Exercise ST Segment",
            options=["Upsloping", "Flat", "Downsloping"],
            help="Select the slope of the ST segment during peak exercise."
        )
        slope_mapping = {"Upsloping": 1, "Flat": 2, "Downsloping": 3}
        slope_encoded = slope_mapping[slope]
        num_vessels = st.number_input(
            "Number of Major Vessels Colored by Fluoroscopy",
            min_value=0,
            max_value=3,
            value=0,
            step=1,
            help="Enter the number of major vessels colored by fluoroscopy."
        )
        thallium = st.selectbox(
            "Thallium Stress Test Result",
            options=["Normal", "Fixed Defect", "Reversible Defect"],
            help="Select the result of your Thallium stress test."
        )
        thallium_mapping = {"Normal": 3, "Fixed Defect": 6, "Reversible Defect": 7}
        thallium_encoded = thallium_mapping[thallium]
        
        submit_button = st.form_submit_button(label="Predict")
    
    if submit_button:
        with st.spinner('Processing your data...'):
            input_data = pd.DataFrame({
                'Age': [age],
                'BP': [bp],
                'Cholesterol': [chol],
                'Max HR': [max_hr],
                'ST depression': [st_depression],
                'Sex': [sex],
                'Chest pain type': [cp],
                'FBS over 120': [fbs],
                'EKG results': [ekg],
                'Exercise angina': [exang],
                'Slope of ST': [slope_encoded],
                'Number of vessels fluro': [num_vessels],
                'Thallium': [thallium_encoded]
            })

            st.write("### Your Input:")
            st.dataframe(input_data)

            input_data_encoded = encode_input(input_data, encoders)
            input_data_preprocessed = preprocess_input(input_data_encoded, scaler, feature_order)

            prediction, prediction_proba = predict_heart_disease(input_data_preprocessed)

            if prediction == 1:
                st.error(f"### 🛑 Heart Disease Detected (Probability: {prediction_proba:.2f})")
                detected_image_path = os.path.join(IMAGES_DIR, "heart_disease_detected.jpg")
                if os.path.exists(detected_image_path):
                    st.image(Image.open(detected_image_path), use_column_width=True)
            else:
                st.success(f"### 🎉 No Heart Disease Detected (Probability: {1 - prediction_proba:.2f})")
                st.balloons()
                no_disease_image_path = os.path.join(IMAGES_DIR, "no_heart_disease.jpg")
                if os.path.exists(no_disease_image_path):
                    st.image(Image.open(no_disease_image_path), use_column_width=True)
        
            st.markdown("""
            ---
            ### 📋 Interpretation of Results:
            - **Heart Disease Detected:** Based on your inputs, the results indicate potential risks for heart disease.
            - **No Heart Disease Detected:** Your inputs suggest that the risk of heart disease is low.
    
            **Note:** These predictions are based on a trained model and do not replace professional medical advice.
            """)

elif options == "About":
    st.header("🔍 About This Application")
    st.write("""
    ### Overview
    The Heart Disease Prediction application utilizes machine learning techniques to assess the risk of heart disease based on various health indicators. By inputting relevant health data, users can receive insights into their heart health and understand potential risk factors.
    """)
    st.write("""
    ### Features
    - **User-Friendly Interface:** Easily input your health metrics through intuitive forms.
    - **Real-Time Predictions:** Get instant predictions on your heart disease risk.
    - **Detailed Results:** Receive probability scores along with clear interpretations of the results.
    - **Educational Insights:** Learn about the factors contributing to heart disease risk.
    - **Visual Aids:** View relevant images that enhance understanding of the results.
    """)
    st.write("""
    ### How It Works
    1. **Data Input:** Provide your health metrics through the input fields.
    2. **Data Processing:** The application processes and scales the input data.
    3. **Prediction:** A trained machine learning model predicts the likelihood of heart disease.
    4. **Results:** Receive your prediction along with probability scores.
    """)
    st.write("""
    ### Model Details
    The application leverages the XGBoost algorithm, a powerful and efficient implementation of gradient boosting. The model has been trained on a comprehensive dataset containing various health indicators to ensure accurate predictions.
    """)
    st.write("""
    ### Project Components
    - **Data Collection:** Aggregated data from reputable health sources to train the model.
    - **Data Preprocessing:** Cleaned and scaled the data to enhance model performance.
    - **Model Training:** Utilized advanced machine learning techniques to develop a robust prediction model.
    - **Deployment:** Integrated the model into a Streamlit application for user accessibility.
    """)

    about_app_image_path = os.path.join(IMAGES_DIR, "about_heart_disease.jpg")
    if os.path.exists(about_app_image_path):
        st.image(Image.open(about_app_image_path), use_column_width=True)
    
    st.write("""
    ### ⚠️ Disclaimer
    This application is intended for educational purposes only and should not be used as a substitute for professional medical advice. Always consult your healthcare provider for any medical concerns.
    """)
    
    st.write("""
    ### Future Enhancements
    - **Integration with Wearable Devices:** Allow users to import data directly from health trackers.
    - **Personalized Health Tips:** Provide tailored recommendations based on prediction results.
    - **Historical Data Analysis:** Enable users to track their health metrics over time.
    - **Multi-language Support:** Expand the application's accessibility to a broader audience by supporting multiple languages.
    """)

    # Optional: Model Performance Metrics
    # st.write("""
    # ### 📈 Model Performance:
    # - **Accuracy:** 85%
    # - **Precision:** 80%
    # - **Recall:** 75%
    # - **F1 Score:** 77%
    # """)
