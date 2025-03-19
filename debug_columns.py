import pandas as pd

# Load the Mesothelioma dataset
df_mesothelioma = pd.read_excel("E:/AI_Medical_Diagnosis/datasets/Mesothelioma data set.xlsx")

# Print all column names to check for typos
print(df_mesothelioma.columns.tolist())
