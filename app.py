from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# -----------------------------
# GLOBAL DATA
# -----------------------------
history_data = []

user_settings = {
    "currency": "INR"
}

currency_rates = {
    "INR": 1,
    "USD": 0.012,
    "EUR": 0.011,
    "GBP": 0.0095
}

currency_symbols = {
    "INR": "₹",
    "USD": "$",
    "EUR": "€",
    "GBP": "£"
}

history_settings = {
    "save_history": True
}

# -----------------------------
# LOAD MODEL
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))

data = pd.read_csv("loan_data.csv")

# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def home():
    return render_template("home.html")


# -----------------------------
# DASHBOARD
# -----------------------------
@app.route("/dashboard")
def dashboard():

    total_predictions = len(history_data)

    approved = sum(
        1 for h in history_data
        if h["result"] == "Approved"
    )

    rejected = total_predictions - approved

    # Line chart data
    prediction_numbers = list(range(1, total_predictions + 1))

    approval_counts = []
    count = 0

    for h in history_data:
        if h["result"] == "Approved":
            count += 1
        approval_counts.append(count)

    return render_template(
        "dashboard.html",
        approved=approved,
        rejected=rejected,
        total_predictions=total_predictions,
        prediction_numbers=prediction_numbers,
        approval_counts=approval_counts
    )


# -----------------------------
# PREDICT
# -----------------------------
@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        try:

            income = float(request.form["income"])
            loan = float(request.form["loan"])
            dependents = float(request.form["dependents"])
            term = float(request.form["term"])
            credit_history = float(request.form.get("credit_history"))

            features = [income, loan, dependents, term, credit_history]

            final = np.array(features).reshape(1, -1)

            prob = model.predict_proba(final)[0][1]
            monthly_income = income / 12

            principal = loan * 1000

            annual_rate = 10

            monthly_rate = annual_rate / (12*100)

            months = int(term)

            emi = (
            principal
            * monthly_rate
            * ((1 + monthly_rate)**months)
            ) / (
            ((1 + monthly_rate)**months)-1
            )

            emi = round(emi,2)

            emi_ratio = round(
            (emi/monthly_income)*100,
            2
            )

            if emi_ratio > 40:
                result = "Rejected"

            if prob >= 0.6:
                result = "Approved"
                confidence = round(prob * 100, 2)
            else:
                result = "Rejected"
                confidence = round((1 - prob) * 100, 2)

            currency = user_settings["currency"]

            rate = currency_rates[currency]
            symbol = currency_symbols[currency]

            display_income = round(income * rate, 2)
            display_loan = round(loan * rate, 2)

            if history_settings["save_history"]:

                history_data.append({
                    "raw_income": income,
                    "raw_loan": loan,
                    "income": display_income,
                    "loan": display_loan,
                    "currency": currency,
                    "result": result,
                    "prob": confidence,
                    "emi": emi,
                    "emi_ratio": emi_ratio
                })

            return render_template(
                "predict.html",
                result=result,
                prob=confidence,
                currency=currency,
                symbol=symbol,
                display_income=display_income,
                display_loan=display_loan
            )

        except Exception as e:
            return render_template(
                "predict.html",
                result="Error",
                prob=str(e)
            )

    return render_template("predict.html")


# -----------------------------
# HISTORY
# -----------------------------
@app.route("/history")
def history():
    return render_template(
        "history.html",
        history=history_data
    )


# -----------------------------
# SETTINGS
# -----------------------------
@app.route("/settings", methods=["GET", "POST"])
def settings():

    if request.method == "POST":

        user_settings["currency"] = request.form["currency"]

        history_settings["save_history"] = (
            "save_history" in request.form
        )
        return render_template(
            "settings.html",
            msg="✅ Currency Updated!"
        )

    return render_template("settings.html")


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)