import streamlit as st
import pandas as pd
import time
import numpy as np
import joblib

#load the trained model

artifact = joblib.load("models\churn_model.joblib")

#extract the artifact

model = artifact["model"]
threshold = artifact["threshold"]
feature_columns = artifact["feature_columns"]

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon= "📊",
    layout="centered"
)
# st.title("Customer Churn Prediction ")

# st.write(

#     "Predict weather a telecommunication customer "
#     "is likely to churn"
# )

# Sidebar
st.sidebar.title("Churn Analytics")
st.sidebar.caption("Telecommunications Intelligence")

st.sidebar.divider()

st.sidebar.subheader("Navigation")
st.sidebar.markdown("🔍 Customer Prediction")

st.sidebar.divider()

st.sidebar.caption("Machine Learning Project")
st.sidebar.caption("Random Forest Classifier")

# Main page header
st.title("Customer Churn Prediction")

st.markdown(
    "Analyze customer information and estimate "
    "the likelihood of customer churn."
)

st.divider()


#designing the form

st.header("Customer information")

with st.form("customer_form"):
    st.subheader("Personal information")
    gender = st.selectbox("Gender",["female", "male"])

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0,1],
        format_func= lambda x: "yes" if x == 1 else "No"

        )
    partner = st.selectbox("Has Partner?", ["Yes", "No"])
    dependents = st.selectbox("Has dependents?", ["Yes", "No"])

    st.subheader("Services")

    tenure = st.number_input("Tenure (months)",min_value=0,max_value=72,value=12)

    phone_service = st.selectbox("Phone Servicesm", ['Yes', 'No'])

    multiple_lines = st.selectbox(
        "Multiple lines",
        ["Yes", "No"," NO phone services"]
    )

    internet_service = st.selectbox(
        "Internet Services",
        ["DSL","Fiber optic", "No"]
    )
    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    st.subheader("Billing Information")

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0
    )

    submitted = st.form_submit_button("Predict Churn")


##lets connect to the models


if submitted:

    # Create a dictionary containing customer information
    customer_data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }
      # Convert dictionary into a DataFrame
    customer_df = pd.DataFrame([customer_data])

    # Ensure the columns match the training data
    customer_df = customer_df[feature_columns]

    st.write("Customer data prepared successfully!")

    st.write(customer_df)