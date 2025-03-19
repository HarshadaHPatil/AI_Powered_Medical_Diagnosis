import os
import streamlit as st
import joblib
import numpy as np

# Set page config
st.set_page_config(page_title="AI-Powered Medical Diagnosis", layout="centered")

# Background Image
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://www.publicdomainpictures.net/pictures/320000/velka/medical-background.jpg");
    background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("🩺 AI-Powered Medical Diagnosis")
st.markdown("### Project by Harshda Patil")
st.write("Select a disease and enter your details for prediction")

# Define model file paths
model_files = {
    "Liver Disease": "models/Liver_Disease_Random_Forest.pkl",
    "Cancer": "models/Cancer_Random_Forest.pkl",
}

# Load available models
models = {}
feature_counts = {}  # Store expected feature counts
available_diseases = []

for disease, path in model_files.items():
    if os.path.exists(path):
        model = joblib.load(path)
        models[disease] = model
        feature_counts[disease] = model.n_features_in_  # Get expected feature count
        available_diseases.append(disease)
    else:
        st.warning(f"⚠️ Model file not found - {path}")

# Disease Selection
disease = st.selectbox("Choose a disease to diagnose", available_diseases)

if disease:
    st.subheader(f"Enter your details for {disease} diagnosis")
    
    # User Input Fields
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    bp = st.number_input("Blood Pressure (Systolic/Diastolic)", min_value=50, max_value=200, step=1)
    sugar = st.number_input("Blood Sugar Level", min_value=50, max_value=500, step=1)
    temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, step=0.1)
    weight = st.number_input("Weight (kg)", min_value=10, max_value=200, step=1)
    height = st.number_input("Height (cm)", min_value=50, max_value=250, step=1)
    bmi = weight / ((height / 100) ** 2) if height > 0 else 0
    smoking = st.selectbox("Do you smoke?", ["Yes", "No"])
    alcohol = st.selectbox("Do you consume alcohol?", ["Yes", "No"])
    family_history = st.selectbox("Family history of disease?", ["Yes", "No"])
    symptoms = st.text_area("Describe your symptoms")

    # Encode categorical values
    gender_encoded = 1 if gender == "Male" else 0
    smoking_encoded = 1 if smoking == "Yes" else 0
    alcohol_encoded = 1 if alcohol == "Yes" else 0
    family_history_encoded = 1 if family_history == "Yes" else 0

    # Feature sets for different models
    features_dict = {
        "Liver Disease": [age, bp, sugar, temp, bmi, gender_encoded, smoking_encoded, alcohol_encoded, family_history_encoded, len(symptoms)],
        "Cancer": [age, bp, sugar, temp, gender_encoded, smoking_encoded, alcohol_encoded, family_history_encoded]  # Expected 8 features
    }

    # Predict Button
    if st.button("Predict"):
        if disease in models:
            model = models[disease]
            expected_features = feature_counts[disease]  # Get expected feature count
            input_data = np.array([features_dict[disease][:expected_features]])  # Pass correct feature count

            prediction = model.predict(input_data)[0]
            result = "Positive" if prediction == 1 else "Negative"
            st.success(f"Prediction: {result}")
        else:
            st.error("Model not available for this disease.")
