# 🩺 Diabetes Prediction

A simple Machine Learning web application that predicts whether a person is likely to have diabetes based on health-related input values.

Built using **FastAPI**, **Scikit-learn**, **Joblib**, and **HTML**.

---

## 🚀 Features

- Predict diabetes risk instantly
- User-friendly web interface
- FastAPI backend
- Random Forest Machine Learning model
- Joblib model loading
- Simple HTML form

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- Jinja2
- HTML
- Uvicorn

---

## 📂 Project Structure

```
Diabetes-Prediction/
│
├── app.py
├── diabetes_model.pkl
├── diabetes.csv
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move to the project folder:

```bash
cd Diabetes-Prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

## 📊 Model

- Algorithm: Random Forest Classifier
- Library: Scikit-learn
- Model Format: Joblib

---

## 📥 Input Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## 📤 Output

- 🩺 Diabetic
- ✅ Not Diabetic

---

## 📄 License

This project is created for learning and educational purposes.

---

### 👨‍💻 Developed by

**Luna**