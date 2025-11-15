# 🩺 Diabetes Prediction Web App

A machine learning-based web application to **predict diabetes risk** using health metrics such as age, BMI, HbA1c levels, blood glucose, and lifestyle factors. Built with **Python, Streamlit, and SVM/Random Forest models**, this project also logs predictions into a local SQLite database.

---

## 🔹 Features

* Predict whether a person is **diabetic or non-diabetic** based on multiple health parameters.
* Real-time interactive **web interface** using Streamlit.
* Visualizes **past predictions history** stored in a database.
* **User-friendly design** with input validation and guidance.
* **Lightweight model deployment** using a pre-trained SVM/Random Forest model.

---

## 🔹 Tech Stack

* Python 3.x
* Machine Learning: **Scikit-learn (SVM / Random Forest)**
* Data Processing: **Pandas, Numpy**
* Visualization: **Matplotlib, Seaborn**
* Web Framework: **Streamlit**
* Database: **SQLite**
* Model Persistence: **Pickle**

---

## 🔹 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/diabetes-predictor.git
   cd diabetes-predictor
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   > Example dependencies include: `streamlit`, `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `requests`.

3. **Run the web app:**

   ```bash
   streamlit run app.py
   ```

---

## 🔹 How to Use

1. Open the app in your browser (Streamlit will provide the local URL).
2. Fill in the health information:

   * Gender, Age, Hypertension, Heart Disease
   * Smoking History, BMI, HbA1c Level, Blood Glucose Level
3. Click **“Get Diabetes Test Result”** to see the prediction.
4. Optionally, check **“Show Prediction History”** to view past predictions.

---

## 🔹 Model Details

* **Trained on:** Diabetes Prediction Dataset (100,000 records)
* **Algorithms Used:** SVM with linear kernel (balanced class weights) or Random Forest Classifier
* **Metrics:**

  * Accuracy: ~96%
  * Precision: ~88%
  * F1 Score: ~88%

---

## 🔹 Database Logging

* Predictions are stored in **SQLite** (`diabetes_data.db`).
* Table `predictions` contains:

  * `gender`, `age`, `hypertension`, `heart_disease`, `smoking_history`, `bmi`, `hba1c_level`, `blood_glucose_level`, `prediction`

---

## 🔹 Screenshots

*(Add screenshots of your app here for visual appeal)*

---

## 🔹 Notes

* This app is for **educational purposes only** and should **not be used for medical diagnosis**.
* Ensure you have a valid Python environment and required libraries installed.

---

---

If you want, I can also **write a short `requirements.txt`** and a **GitHub-ready folder structure** for this project so it’s fully ready to push. Do you want me to do that?
