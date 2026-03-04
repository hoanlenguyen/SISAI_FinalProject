# Heart Disease Prediction MVP ❤️

A machine learning web application designed to support the early detection of cardiovascular diseases. This Minimum Viable Product (MVP) uses a trained classification model to analyze clinical and lifestyle metadata, predicting whether a patient is at "High Risk" or "Low Risk" for heart disease.

## 🚀 Features
* **Predictive Machine Learning:** Utilizes a pre-trained model (`final_model.pkl`) to instantly evaluate patient data.
* **Interactive UI:** A simple, intuitive web interface built with Streamlit for easy data entry and instant risk assessment. 
* **Transparent Results:** Outputs a clear risk category (High/Low) alongside the model's exact calculated probability percentage.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Frontend/UI:** Streamlit
* **Data Manipulation:** Pandas
* **Machine Learning & Serialization:** Scikit-Learn, Joblib

## 📊 Model Details
The current prototype is designed to prioritize medical interpretability and ease of use. 
* **Input Features (10):** Age (years), Gender, Body Mass Index (BMI), Systolic Blood Pressure, Diastolic Blood Pressure, Cholesterol Level, Glucose Level, Smoking status, Alcohol intake, and Physical Activity.
* **Output:** A binary classification indicating High Risk or Low Risk, accompanied by a probability score.

## 💻 Installation and Setup

Follow these simple steps to run the application on your local machine.

**1. Clone the repository**

* git clone https://github.com/hoanlenguyen/SISAI_FinalProject
* cd SISAI_FinalProject

**2. Create a virtual environment**

python -m venv venv
source venv/bin/activate  
* # On Windows use: venv\Scripts\activate

**3. Install dependencies**

pip install -r requirements.txt

**4. Run the application**

streamlit run app.py

## 💡 Usage
Open the local URL provided by Streamlit in your terminal (usually http://localhost:8501).

Use the sliders and dropdown menus to enter the patient's general and clinical metadata.

Click the Predict button at the bottom of the form.

View the color-coded "Low Risk" (Green) or "High Risk" (Red) classification and the probability score directly on the screen.
