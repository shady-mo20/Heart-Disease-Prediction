import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def load_data(filepath):
    data = pd.read_excel(filepath)
    return data

def remove_outliers(data):
    for column in data.columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            data = data.drop(data[(data[column] < lower_bound) | (data[column] > upper_bound)].index)
    return data
