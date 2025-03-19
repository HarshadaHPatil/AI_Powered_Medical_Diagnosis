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

# Display basic info
print("Liver Disease Dataset:\n", df_liver.info(), "\n")
print("Cancer Dataset:\n", df_cancer.info(), "\n")
print("Mesothelioma Dataset:\n", df_mesothelioma.info(), "\n")
print("Stroke Dataset:\n", df_stroke.info(), "\n")
