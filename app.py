import streamlit as st
import pandas as pd
import joblib

# Load the trained machine learning model
model = joblib.load("customer_churn_model.pkl")

# Page settings
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊"
)

st.title("Customer Churn Prediction")
st.write("Enter customer details to predict whether they may leave the company.")

with st.form("customer_form"):

    st.subheader("Customer Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
        Partner = st.selectbox("Partner", ["Yes", "No"])
        Dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (months)", 0, 72, 12)
        PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
        MultipleLines = st.selectbox(
            "Multiple Lines",
            ["No phone service", "No", "Yes"]
        )
        InternetService = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )
        OnlineSecurity = st.selectbox(
            "Online Security",
            ["No", "Yes", "No internet service"]
        )

    with col2:
        OnlineBackup = st.selectbox(
            "Online Backup",
            ["No", "Yes", "No internet service"]
        )
        DeviceProtection = st.selectbox(
            "Device Protection",
            ["No", "Yes", "No internet service"]
        )
        TechSupport = st.selectbox(
            "Tech Support",
            ["No", "Yes", "No internet service"]
        )
        StreamingTV = st.selectbox(
            "Streaming TV",
            ["No", "Yes", "No internet service"]
        )
        StreamingMovies = st.selectbox(
            "Streaming Movies",
            ["No", "Yes", "No internet service"]
        )
        Contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )
        PaperlessBilling = st.selectbox(
            "Paperless Billing", ["Yes", "No"]
        )
        PaymentMethod = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )
        MonthlyCharges = st.number_input(
            "Monthly Charges", min_value=0.0, value=50.0
        )
        TotalCharges = st.number_input(
            "Total Charges", min_value=0.0, value=500.0
        )

    submitted = st.form_submit_button("Predict Churn")

if submitted:

    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }])

    prediction = model.predict(customer)[0]

    yes_index = list(model.classes_).index("Yes")
    probability = model.predict_proba(customer)[0][yes_index]

    st.subheader("Prediction Result")

    if prediction == "Yes":
        st.error("This customer is likely to churn.")
    else:
        st.success("This customer is unlikely to churn.")

    st.metric("Churn Probability", f"{probability:.2%}")
    
