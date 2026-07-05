from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and encoders
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    try:

        data = {}

        # Categorical values
        data["CODE_GENDER"] = request.form.get("CODE_GENDER", "M")
        data["FLAG_OWN_CAR"] = request.form.get("FLAG_OWN_CAR", "N")
        data["FLAG_OWN_REALTY"] = request.form.get("FLAG_OWN_REALTY", "Y")

        # Numeric values
        data["CNT_CHILDREN"] = int(request.form.get("CNT_CHILDREN") or 0)
        data["AMT_INCOME_TOTAL"] = float(request.form.get("AMT_INCOME_TOTAL"))

        data["NAME_INCOME_TYPE"] = request.form.get("NAME_INCOME_TYPE", "Working")
        data["NAME_EDUCATION_TYPE"] = request.form.get("NAME_EDUCATION_TYPE", "Higher education")
        data["NAME_FAMILY_STATUS"] = request.form.get("NAME_FAMILY_STATUS", "Married")
        data["NAME_HOUSING_TYPE"] = request.form.get("NAME_HOUSING_TYPE", "House / apartment")
         
        age = int(request.form.get("AGE") or 25)
        employment_years = int(request.form.get("EMPLOYMENT_YEARS") or 1)
        data["DAYS_BIRTH"] = -(age * 365)
        data["DAYS_EMPLOYED"] = -(employment_years * 365)
        data["FLAG_MOBIL"] = int(request.form.get("FLAG_MOBIL") or 1)

        # data["DAYS_BIRTH"] = int(request.form.get("DAYS_BIRTH") or -12000)
        # data["DAYS_EMPLOYED"] = int(request.form.get("DAYS_EMPLOYED") or -1000)

        data["FLAG_MOBIL"] = int(request.form.get("FLAG_MOBIL") or 1)
        data["FLAG_WORK_PHONE"] = int(request.form.get("FLAG_WORK_PHONE") or 0)
        data["FLAG_PHONE"] = int(request.form.get("FLAG_PHONE") or 0)
        data["FLAG_EMAIL"] = int(request.form.get("FLAG_EMAIL") or 0)

        data["OCCUPATION_TYPE"] = request.form.get("OCCUPATION_TYPE", "Unknown")

        data["CNT_FAM_MEMBERS"] = float(request.form.get("CNT_FAM_MEMBERS") or 2)
        data["MONTHS_BALANCE"] = int(request.form.get("MONTHS_BALANCE") or 0)
         # Minimum income rule
        if data["AMT_INCOME_TOTAL"] < 10000:
             return render_template(
               "result.html",
             prediction="Credit Card Rejected ❌",
            message="Annual income is below the minimum requirement."
            )

# Age rule (if you are entering DAYS_BIRTH directly)
        if data["DAYS_BIRTH"] > -6570:   # Less than about 18 years old
               return render_template(
             "result.html",
            prediction="Credit Card Rejected ❌",
             message="Applicant must be at least 18 years old."
             )

# Family members rule
        if data["CNT_FAM_MEMBERS"] < 1:
            return render_template(
           "result.html",
           prediction="Invalid Input",
            message="Family members must be at least 1."
           )

        # Encode categorical values
        categorical_cols = [
            "CODE_GENDER",
            "FLAG_OWN_CAR",
            "FLAG_OWN_REALTY",
            "NAME_INCOME_TYPE",
            "NAME_EDUCATION_TYPE",
            "NAME_FAMILY_STATUS",
            "NAME_HOUSING_TYPE",
            "OCCUPATION_TYPE"
        ]

        for col in categorical_cols:
            try:
                data[col] = encoders[col].transform([data[col]])[0]
            except:
                data[col] = 0

        # Create DataFrame in same column order used for training
        features = pd.DataFrame([data])
        print("Input row:", features.to_dict(orient="records"))
        print("Predict proba:", model.predict_proba(features))
        print("Prediction:", model.predict(features))

        prediction = model.predict(features)[0]

        if prediction == 0:
            prediction_text = "Credit Card Approved ✅"
        else:
            prediction_text = "Credit Card Rejected ❌"

        return render_template(
            "result.html",
            prediction=prediction_text
        )
    

    except Exception as e:
        return render_template(
            "result.html",
            prediction=f"Error: {str(e)}"
        )
         



import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)