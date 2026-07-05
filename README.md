## LIVE PREVIEW
----

https://creditcard-1-cc5p.onrender.com

-----

# 💳 Credit Card Approval Prediction using Machine Learning

##  Project Overview

The **Credit Card Approval Prediction System** is a Machine Learning web application developed using **Python, Flask, and XGBoost**. It predicts whether a customer is eligible for a credit card based on financial and demographic information entered through a web interface.

The application uses a trained machine learning model to analyze customer details and instantly displays whether the credit card application is **Approved** or **Rejected**.

---
## video link 

https://drive.google.com/file/d/1rkoIQdl9armYLtRRV_G1UKNIME-rYNAB/view?usp=drivesdk

## 📂 Project Structure

```
CreditCardApproval/
│
├── app.py
├── model.pkl
├── encoders.pkl
├---requiredment.txt
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
https://github.com/vardhineedhi/creditcard.git
```

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
<img width="1599" height="684" alt="Screenshot 2026-07-05 090506" src="https://github.com/user-attachments/assets/3444b858-f3d5-447c-9af4-709496238f7e" />



- Prediction Form

<img width="1599" height="755" alt="Screenshot 2026-07-05 090527" src="https://github.com/user-attachments/assets/385c847b-c461-4cbd-b73a-432f6dda4a2b" />


- Result Pages
  
<img width="1592" height="697" alt="Screenshot 2026-07-05 090627" src="https://github.com/user-attachments/assets/04551bbc-c842-418d-a710-12e44b6618b5" />

<img width="1599" height="700" alt="Screenshot 2026-07-05 090649" src="https://github.com/user-attachments/assets/b579c6f0-e322-41da-bf3c-9d5572892842" />


---


# ⭐ If you like this project

Please give this repository a ⭐ on GitHub.
