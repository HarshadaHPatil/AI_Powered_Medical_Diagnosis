import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned datasets
df_liver = pd.read_csv("datasets/Cleaned_Liver_Disease.csv")
df_cancer = pd.read_csv("datasets/Cleaned_Cancer_Data.csv")
df_mesothelioma = pd.read_excel("datasets/Cleaned_Mesothelioma_Data.xlsx")
df_stroke = pd.read_csv("datasets/Cleaned_Stroke_Data.csv")

# Function to plot histograms
def plot_histograms(df, title):
    df.hist(figsize=(10, 6), bins=20)
    plt.suptitle(title, fontsize=14)
    plt.show()

# Function to plot correlation heatmap
def plot_correlation(df, title):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(title, fontsize=14)
    plt.show()

# Plot histograms
plot_histograms(df_liver, "Liver Disease Data Distribution")
plot_histograms(df_cancer, "Cancer Data Distribution")
plot_histograms(df_mesothelioma, "Mesothelioma Data Distribution")
plot_histograms(df_stroke, "Stroke Data Distribution")

# Plot correlation heatmaps
plot_correlation(df_liver, "Liver Disease Feature Correlation")
plot_correlation(df_cancer, "Cancer Feature Correlation")
plot_correlation(df_mesothelioma, "Mesothelioma Feature Correlation")
plot_correlation(df_stroke, "Stroke Feature Correlation")

print("EDA completed! Check the plots for insights.")
