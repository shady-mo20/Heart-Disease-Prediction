import joblib
import warnings
warnings.filterwarnings('ignore')



def save_scaler(scaler, scaler_name):

    joblib.dump(scaler, f"{scaler_name}.pkl")
    print(f"Scaler saved as {scaler_name}.pkl")