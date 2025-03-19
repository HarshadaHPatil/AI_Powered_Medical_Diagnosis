import pandas as pd

# Define file paths
liver_data = "datasets/Liver_disease_data.csv"
cancer_data = "datasets/The_Cancer_data_1500_V2.csv"
mesothelioma_data = "datasets/Mesothelioma data set.xlsx"
stroke_data = "datasets/healthcare-dataset-stroke-data.csv"

# Load datasets
df_liver = pd.read_csv(liver_data)
df_cancer = pd.read_csv(cancer_data)
df_mesothelioma = pd.read_excel(mesothelioma_data)
df_stroke = pd.read_csv(stroke_data)

# Handling missing values
df_liver = df_liver.dropna()
df_cancer = df_cancer.dropna()
df_mesothelioma = df_mesothelioma.dropna()
df_stroke = df_stroke.dropna()

# Convert categorical columns in stroke dataset
df_stroke["gender"] = df_stroke["gender"].astype("category").cat.codes
df_stroke["ever_married"] = df_stroke["ever_married"].astype("category").cat.codes
df_stroke["work_type"] = df_stroke["work_type"].astype("category").cat.codes
df_stroke["Residence_type"] = df_stroke["Residence_type"].astype("category").cat.codes
df_stroke["smoking_status"] = df_stroke["smoking_status"].astype("category").cat.codes

# Save cleaned datasets
df_liver.to_csv("datasets/Cleaned_Liver_Disease.csv", index=False)
df_cancer.to_csv("datasets/Cleaned_Cancer_Data.csv", index=False)
df_mesothelioma.to_excel("datasets/Cleaned_Mesothelioma_Data.xlsx", index=False)
df_stroke.to_csv("datasets/Cleaned_Stroke_Data.csv", index=False)

print("Data cleaning complete! Cleaned files saved in 'datasets' folder.")
