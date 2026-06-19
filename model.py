import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import pickle

print("Loading dataset...")
data = pd.read_csv("loan_data.csv")

print("Columns in dataset:", data.columns)

for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = data[col].fillna(data[col].mode()[0])
    else:
        data[col] = data[col].fillna(data[col].mean())

print("Missing values handled")

for col in data.columns:
    if data[col].dtype == 'object':
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])

print("Encoding done")

X = data[
[
"ApplicantIncome",
"LoanAmount",
"Dependents",
"Loan_Amount_Term",
"Credit_History"
]
]

y = data["Credit_History"]

y = y.astype(int)
print("Features selected")
model = XGBClassifier(eval_metric='logloss')
model.fit(X, y)
print("Model trained")
pickle.dump(model, open("model.pkl", "wb"))
print("✅ model.pkl created successfully!")