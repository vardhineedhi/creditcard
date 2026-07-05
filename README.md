# 💳 Credit Card Approval Prediction using Machine Learning

## 📌 Project Overview

The **Credit Card Approval Prediction System** is a Machine Learning web application developed using **Python, Flask, and XGBoost**. It predicts whether a customer is eligible for a credit card based on financial and demographic information entered through a web interface.

The application uses a trained machine learning model to analyze customer details and instantly displays whether the credit card application is **Approved** or **Rejected**.

---

## 🚀 Features

- User-friendly web interface
- Customer information form
- Machine Learning prediction
- Flask backend integration
- Trained XGBoost model
- Fast and real-time prediction
- Responsive UI

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- HTML5
- CSS3
- Bootstrap
- Font Awesome

---

## 📂 Project Structure

```
CreditCardApproval/
│
├── app.py
├── model.pkl
├── encoders.pkl
├
│
├── static/
│   └── style.css
│
├── templates/
│   ├── home.html
│   ├── index.html
│   └── result.html
│
├── dataset/
│   ├── application_record.csv
│   └── credit_record.csv
│
└── README.md
```

---

# 📥 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/CreditCardApproval.git
```

Replace **YOUR_USERNAME** with your GitHub username.

---

## 2️⃣ Open the Project Folder

```bash
cd CreditCardApproval
```
---

## 3. Install Required Libraries

```bash
pip install flask
pip install pandas
pip install numpy
pip install scikit-learn
pip install xgboost
pip install joblib
```
---

# ▶️ Run the Application

```bash
python app.py
```

Flask Server starts successfully.

Example

```
* Running on http://127.0.0.1:5000/
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

# 📊 Dataset

Dataset used:

- application_record.csv
- credit_record.csv

Source:

https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction

---

# 🤖 Machine Learning Models Used

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost (Final Model)

The model with the best performance was selected and saved as **model.pkl**.

---

# 📈 Workflow

1. Load Dataset
2. Data Preprocessing
3. Handle Missing Values
4. Encode Categorical Features
5. Split Dataset
6. Train Machine Learning Models
7. Evaluate Models
8. Save Best Model
9. Build Flask Web Application
10. Predict Credit Card Approval

---

# 📷 Application Screens

- Home Page
- Prediction Form
- Result Page

---

# 📌 Future Improvements

- Database Integration
- User Login Authentication
- Admin Dashboard
- Cloud Deployment
- Improved Model Accuracy
- Better Business Rules

---

# 👨‍💻 Author

**Vardhineedi Raja**

B.Tech Information Technology

Aditya College of Engineering and Technology

---

# ⭐ If you like this project

Please give this repository a ⭐ on GitHub.
