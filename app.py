import numpy as np
import pickle
import streamlit as st
import sqlite3
import os

# Define model path and Drive file ID
model_path = "trained_model_rf_new.sav"
hf_url =  = "https://huggingface.co/kush246/Diabetes_prediction_rfc/resolve/main/trained_model_rf_new.sav"  

if not os.path.exists(model_path):
    with requests.get(hf_url, stream=True) as r:
        r.raise_for_status()
        with open(model_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                
# Load the saved model
with open(model_path, 'rb') as f:
    loaded_model = pickle.load(f)
    
# Prediction function
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return '🟢 The person is not diabetic ✅' if prediction[0] == 0 else '🔴 The person is diabetic ⚠️'

def init_db():
    conn = sqlite3.connect('diabetes_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gender TEXT,
            age INTEGER,
            hypertension TEXT,
            heart_disease TEXT,
            smoking_history TEXT,
            bmi REAL,
            hba1c_level REAL,
            blood_glucose_level INTEGER,
            prediction TEXT
        )
    ''')
    conn.commit()
    conn.close()
def insert_data(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c, glucose, prediction):
    conn = sqlite3.connect('diabetes_data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO predictions (
            gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level, prediction
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c, glucose, prediction))
    conn.commit()
    conn.close()

# Main function
def main():
    init_db()
    st.set_page_config(page_title="🩺 Diabetes Predictor", layout="centered")

    st.markdown("<h1 style='text-align: center; color: teal;'>🩺 Diabetes Prediction Web App</h1>", unsafe_allow_html=True)
    st.markdown("📋 Fill in the health information below to predict diabetes risk.", unsafe_allow_html=True)
    

    # Layout in columns
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox('👤 Gender', ['Female', 'Male', 'Other'])
        age = st.number_input('🎂 Age (years)', min_value=1, max_value=120, step=1)
        hypertension = st.selectbox('💓 Hypertension', ['No', 'Yes'])
        heart_disease = st.selectbox('❤️ Heart Disease', ['No', 'Yes'])

    with col2:
        smoking_history = st.selectbox('🚬 Smoking History', ['never', 'No Info', 'current', 'former', 'ever', 'not current'])
        bmi = st.number_input('⚖️ BMI (kg/m²)', min_value=10.0, max_value=60.0, format="%.2f")
        HbA1c_level = st.number_input('🧪 HbA1c Level (%)', min_value=3.0, max_value=15.0, format="%.1f")
        blood_glucose_level = st.number_input('🩸 Blood Glucose Level (mg/dL)', min_value=50, max_value=500)

    st.write("---")

    # Map categorical inputs
    gender_map = {'Female': 0, 'Male': 1, 'Other': 2}
    hypertension_map = {'No': 0, 'Yes': 1}
    heart_disease_map = {'No': 0, 'Yes': 1}
    smoking_map = {'never': 0, 'No Info': 1, 'current': 2, 'former': 3, 'ever': 4, 'not current': 5}

    input_list = [
        gender_map[gender],
        age,
        hypertension_map[hypertension],
        heart_disease_map[heart_disease],
        smoking_map[smoking_history],
        bmi,
        HbA1c_level,
        blood_glucose_level
    ]

    if st.button('📊 Get Diabetes Test Result'):
     with st.spinner('🔍 Analyzing your data...'):
        result = diabetes_prediction(input_list)
        st.success(result)

        # Store in DB
        insert_data(gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level, result)
    if st.checkbox("📂 Show Prediction History"):
        conn = sqlite3.connect('diabetes_data.db')
        c = conn.cursor()
        c.execute("SELECT gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level, prediction FROM predictions ORDER BY id DESC")
        rows = c.fetchall()
        conn.close()

        st.write("### 📜 Past Predictions")
        st.dataframe(rows, use_container_width=True)

    st.markdown("""
        <style>
        div.stButton > button {
            background-color: teal;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1.5em;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
