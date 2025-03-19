import pandas as pd
import os

# Define dataset folder path
dataset_path = r"E:\AI_Medical_Diagnosis\datasets"

# List all files in the dataset directory
print("Available files in dataset folder:", os.listdir(dataset_path))

# Load datasets with correct file names and extensions
df_liver = pd.read_csv(os.path.join(dataset_path, "Cleaned_Liver_Disease.csv"))
df_cancer = pd.read_csv(os.path.join(dataset_path, "Cleaned_Cancer_Data.csv"))
df_mesothelioma = pd.read_excel(os.path.join(dataset_path, "Cleaned_Mesothelioma_Data.xlsx"))  # This remains .xlsx
df_stroke = pd.read_csv(os.path.join(dataset_path, "Cleaned_Stroke_Data.csv"))

# Display dataset information
print("Liver Disease Dataset Shape:", df_liver.shape)
print("Cancer Dataset Shape:", df_cancer.shape)
print("Mesothelioma Dataset Shape:", df_mesothelioma.shape)
print("Stroke Dataset Shape:", df_stroke.shape)

# Proceed with data preprocessing and model training...
# Add your model training code here
