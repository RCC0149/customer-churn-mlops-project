import pandas as pd
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('models/churn_model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Define feature columns (match TCC_df without Churn)
feature_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
                'MultipleLines_No', 'MultipleLines_Yes', 'InternetService_DSL',
                'InternetService_Fiber optic', 'InternetService_No', 'OnlineSecurity_No',
                'OnlineSecurity_Yes', 'OnlineBackup_No', 'OnlineBackup_Yes',
                'DeviceProtection_No', 'DeviceProtection_Yes', 'TechSupport_No',
                'TechSupport_Yes', 'StreamingTV_No', 'StreamingTV_Yes',
                'StreamingMovies_No', 'StreamingMovies_Yes', 'Contract_Month-to-month',
                'Contract_One year', 'Contract_Two year', 'PaperlessBilling',
                'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)',
                'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check',
                'MonthlyCharges', 'TotalCharges', 'tenure_short', 'tenure_medium', 'tenure_long',
                'charge_per_month']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    input_data = {
        'gender': int(request.form['gender']),
        'SeniorCitizen': int(request.form['SeniorCitizen']),
        'Partner': int(request.form['Partner']),
        'Dependents': int(request.form['Dependents']),
        'tenure': float(request.form['tenure']),
        'PhoneService': int(request.form['PhoneService']),
        'MultipleLines': request.form['MultipleLines'],
        'InternetService': request.form['InternetService'],
        'OnlineSecurity': request.form['OnlineSecurity'],
        'OnlineBackup': request.form['OnlineBackup'],
        'DeviceProtection': request.form['DeviceProtection'],
        'TechSupport': request.form['TechSupport'],
        'StreamingTV': request.form['StreamingTV'],
        'StreamingMovies': request.form['StreamingMovies'],
        'Contract': request.form['Contract'],
        'PaperlessBilling': int(request.form['PaperlessBilling']),
        'PaymentMethod': request.form['PaymentMethod'],
        'MonthlyCharges': float(request.form['MonthlyCharges']),
        'TotalCharges': float(request.form['TotalCharges'])
    }

    # Create DataFrame and encode
    df = pd.DataFrame([input_data])
    df['charge_per_month'] = df['MonthlyCharges'] / (df['tenure'] + 1)
    df['tenure_short'] = (df['tenure'] <= 8).astype(int)
    df['tenure_medium'] = ((df['tenure'] > 8) & (df['tenure'] <= 55)).astype(int)
    df['tenure_long'] = (df['tenure'] > 55).astype(int)
    df = pd.get_dummies(df, columns=['MultipleLines', 'InternetService', 'OnlineSecurity',
                                     'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                     'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod'])
    
    # Align columns with training data
    for col in feature_cols:
        if col not in df.columns:
            df[col] = 0
    df = df[feature_cols]

    # Scale numerical features
    numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'charge_per_month']
    df[numerical_cols] = scaler.transform(df[numerical_cols])

    # Predict
    prediction = model.predict_proba(df)[0][1]  # Probability of Churn=1
    result = f"Churn Probability: {prediction:.2%}"
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)