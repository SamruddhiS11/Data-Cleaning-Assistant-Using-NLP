import pandas as pd
import numpy as np
from scipy import stats

def detect_column_types(df):
    types = {}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            types[col] = "Numeric"
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            types[col] = "Datetime"
        elif pd.api.types.is_string_dtype(df[col]):
            types[col] = "Categorical/Text"
        else:
            types[col] = "Unknown"
    return types

def detect_missing_values(df):
    return df.isnull().sum().to_dict()

def detect_duplicates(df):
    return df.duplicated().sum()

def detect_outliers(df):
    outliers = {}
    for col in df.select_dtypes(include=np.number).columns:
        z_scores = np.abs(stats.zscore(df[col].dropna()))
        outliers[col] = (z_scores > 3).sum()
    return outliers

def fill_missing_values(df, method, column):
    if method == "mean":
        df[column].fillna(df[column].mean(), inplace=True)
    elif method == "median":
        df[column].fillna(df[column].median(), inplace=True)
    elif method == "mode":
        df[column].fillna(df[column].mode()[0], inplace=True)
    elif method == "drop":
        df.dropna(subset=[column], inplace=True)
    return df

def remove_duplicates(df):
    return df.drop_duplicates()