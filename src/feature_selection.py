from imblearn.under_sampling import NearMiss
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')


def feature_selection(data):
    label_encoder = LabelEncoder()

    categorical_columns = ['HeartDisease', 'Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'Asthma', 'KidneyDisease', 'SkinCancer'] 

    for col in categorical_columns:
        data[col] = label_encoder.fit_transform(data[col])

    x = data.drop(columns=['HeartDisease'])
    y = data['HeartDisease']
    
    NearMiss_obj = NearMiss()
    new_x, new_y = NearMiss_obj.fit_resample(x, y)

    return new_x, new_y