import pandas as pd

# Load Mesothelioma dataset
df_mesothelioma = pd.read_excel("datasets/Processed_Mesothelioma_Data.xlsx")

# Print column names
print("Mesothelioma Dataset Columns:")
print(df_mesothelioma.columns)
