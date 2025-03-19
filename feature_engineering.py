import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load cleaned datasets
df_liver = pd.read_csv("datasets/Cleaned_Liver_Disease.csv")
df_cancer = pd.read_csv("datasets/Cleaned_Cancer_Data.csv")
df_mesothelioma = pd.read_excel("datasets/Cleaned_Mesothelioma_Data.xlsx")
df_stroke = pd.read_csv("datasets/Cleaned_Stroke_Data.csv")

# Function to normalize numerical features
def normalize_features(df, numerical_cols):
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df

# Function to encode categorical features
def encode_categorical(df, categorical_cols):
    encoder = LabelEncoder()
    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col])
    return df

# Liver Disease Data
numerical_cols = ["Age", "BMI", "AlcoholConsumption", "PhysicalActivity", "LiverFunctionTest"]
df_liver = normalize_features(df_liver, numerical_cols)

# Cancer Data
numerical_cols = ["Age", "BMI", "AlcoholIntake", "PhysicalActivity"]
df_cancer = normalize_features(df_cancer, numerical_cols)

# Mesothelioma Data
numerical_cols = ["age", "duration of asbestos exposure", "duration of symptoms", "platelet count (PLT)", "total protein"]
df_mesothelioma = normalize_features(df_mesothelioma, numerical_cols)

# Stroke Data
numerical_cols = ["age", "avg_glucose_level", "bmi"]
categorical_cols = ["gender", "ever_married", "work_type", "Residence_type", "smoking_status"]
df_stroke = normalize_features(df_stroke, numerical_cols)
df_stroke = encode_categorical(df_stroke, categorical_cols)

# Save processed datasets
df_liver.to_csv("datasets/Processed_Liver_Disease.csv", index=False)
df_cancer.to_csv("datasets/Processed_Cancer_Data.csv", index=False)
df_mesothelioma.to_excel("datasets/Processed_Mesothelioma_Data.xlsx", index=False)
df_stroke.to_csv("datasets/Processed_Stroke_Data.csv", index=False)

print("Feature engineering completed! Processed files saved.")
