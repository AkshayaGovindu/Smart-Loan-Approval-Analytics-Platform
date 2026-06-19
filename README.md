# Smart-Loan-Approval-Analytics-Platform
A machine learning-powered loan approval system built using Flask, XGBoost, HTML, CSS, JavaScript, and Chart.js. The platform not only predicts loan approval but also provides real-time analytics, EMI-based eligibility evaluation, currency conversion, history tracking, and an interactive dashboard.

# Features
## Machine Learning Loan Prediction
- Trained using XGBoost Classifier.
- Predicts loan approval probability.
- Displays confidence score for each prediction.
- Uses applicant income, loan amount, dependents, loan term, and credit history as inputs.

## EMI-Based Loan Eligibility Analysis
### Unlike traditional student projects that only predict approval/rejection, this system also evaluates:

- Monthly EMI
- EMI-to-Income Ratio
- Loan affordability analysis
### Additional validation:

- Loans can be rejected if EMI exceeds acceptable income thresholds.
- Simulates real-world banking loan evaluation practices.
- Multi-Currency Support

## Users can switch between:

- INR (₹)
- USD ($)
- EUR (€)
- GBP (£)
### All financial values are dynamically converted and displayed according to the selected currency.

## Interactive Analytics Dashboard
Provides real-time visualization of prediction data:

## KPI Cards
- Total Predictions
- Approved Loans
- Rejected Loans
- Approval Rate
- Average EMI

## Charts
- Approval vs Rejection Bar Chart
- Approval Ratio Doughnut Chart
- Approval Trend Line Chart
- Confidence Analysis Chart
- EMI Trend Chart
- Income vs Loan Scatter Plot

## Prediction History Tracking
Stores prediction records including:

- Income
- Loan Amount
- Currency
- Approval Status
- Confidence Score
- EMI
- EMI Ratio

## History Control Settings
Users can choose whether to:

- Save prediction history
- Disable history tracking
  
## Modern Banking Dashboard UI
- Responsive layout
- Sidebar navigation
- Modern card design
- Interactive charts using Chart.js
- Professional banking-style interface

# Technology Stack
## Backend
- Python
- Flask
- XGBoost
- NumPy
- Pandas
- Pickle
  
## Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js
- Jinja2 Templates

## Machine Learning
- XGBoost Classifier
- Data Preprocessing
- Missing Value Handling
- Label Encoding

## Workflow
- User enters loan details.
- ML model predicts approval probability.
- EMI is calculated.
- EMI affordability is evaluated.
- Decision is displayed with confidence score.
- Prediction is stored in history (optional).
- Dashboard updates automatically.
- Charts reflect latest analytics.
