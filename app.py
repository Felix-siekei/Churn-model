
import streamlit as st
import joblib
import pandas as pd


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# 2. LOAD TRAINED MODEL
# --------------------------------------------------

artifact = joblib.load("models/churn_model.joblib")

model = artifact["model"]
threshold = artifact["threshold"]
feature_columns = artifact["feature_columns"]


# --------------------------------------------------
# 3. SESSION STATE INITIALIZATION
# --------------------------------------------------

if "current_step" not in st.session_state:
    st.session_state.current_step = 1

if "form_completed" not in st.session_state:
    st.session_state.form_completed = False

if "customer_data" not in st.session_state:
    st.session_state.customer_data = None


# --------------------------------------------------
# 4. HELPER FUNCTIONS
# --------------------------------------------------


def restore_form_state(fields):

    for field in fields:

        saved_key = f"saved_{field}"

        # Restore only if the widget has no existing state
        if (
            field not in st.session_state
            and saved_key in st.session_state
        ):

            st.session_state[field] = (
                st.session_state[saved_key]
            )


def save_form_state(fields):

    for field in fields:

        saved_key = f"saved_{field}"

        st.session_state[saved_key] = (
            st.session_state[field]
        )


def navigate_to(step):

    st.session_state.current_step = step
    st.session_state.form_completed = False

    st.rerun()



# --------------------------------------------------
# 5. SIDEBAR
# --------------------------------------------------

st.sidebar.title("Churn Analytics",)

st.sidebar.caption(
    "Telecommunications Customer Intelligence"
)

st.sidebar.divider()

st.sidebar.subheader("Navigation")

st.sidebar.markdown("🔍 Customer Prediction")

st.sidebar.divider()

st.sidebar.subheader("Model Information")

st.sidebar.write("Algorithm: Random Forest")

st.sidebar.write(f"Decision Threshold: {threshold}")

st.sidebar.caption("Machine Learning Project")


# --------------------------------------------------
# 6. MAIN PAGE HEADER
# --------------------------------------------------

st.title("Customer Churn Prediction")

st.markdown(
    "Enter customer information to prepare a "
    "churn prediction."
)

st.divider()


# --------------------------------------------------
# 7. PROGRESS INDICATOR
# --------------------------------------------------

step = st.session_state.current_step

step_names = {
    1: "Services",
    2: "Billing",
    3: "Account Information"
}

st.subheader(
    f"Step {step} of 3: {step_names[step]}"
)

st.progress(step / 3)

st.divider()


# ==================================================
# 8. STEP 1 - SERVICES
# ==================================================

if step == 1:

    service_fields = [
        "phone_service",
        "multiple_lines",
        "internet_service",
        "online_security",
        "online_backup",
        "device_protection",
        "tech_support",
        "streaming_tv",
        "streaming_movies"
    ]

    restore_form_state(service_fields)

    with st.form("services_form"):

        st.subheader("Phone Services")

        col1, col2 = st.columns(2)

        with col1:

            phone_service = st.selectbox(
                "Phone Service",
                ["Yes", "No"],
                key="phone_service"
            )

        with col2:

            multiple_lines = st.selectbox(
                "Multiple Lines",
                ["Yes", "No", "No phone service"],
                key="multiple_lines"
            )

        st.divider()

        st.subheader("Internet Services")

        col1, col2 = st.columns(2)

        with col1:

            internet_service = st.selectbox(
                "Internet Service",
                ["DSL", "Fiber optic", "No"],
                key="internet_service"
            )

            online_security = st.selectbox(
                "Online Security",
                ["Yes", "No", "No internet service"],
                key="online_security"
            )

            online_backup = st.selectbox(
                "Online Backup",
                ["Yes", "No", "No internet service"],
                key="online_backup"
            )

            device_protection = st.selectbox(
                "Device Protection",
                ["Yes", "No", "No internet service"],
                key="device_protection"
            )

        with col2:

            tech_support = st.selectbox(
                "Tech Support",
                ["Yes", "No", "No internet service"],
                key="tech_support"
            )

            streaming_tv = st.selectbox(
                "Streaming TV",
                ["Yes", "No", "No internet service"],
                key="streaming_tv"
            )

            streaming_movies = st.selectbox(
                "Streaming Movies",
                ["Yes", "No", "No internet service"],
                key="streaming_movies"
            )

        st.divider()

        next_clicked = st.form_submit_button(
            "Next: Billing →",
            use_container_width=True
        )

    if next_clicked:

        save_form_state(service_fields)

        navigate_to(2)


# ==================================================
# 9. STEP 2 - BILLING
# ==================================================

elif step == 2:

    billing_fields = [
        "payment_method",
        "paperless_billing",
        "monthly_charges",
        "total_charges"
    ]

    restore_form_state(billing_fields)

    with st.form("billing_form"):

        st.subheader("Billing Information")

        col1, col2 = st.columns(2)

        with col1:

            payment_method = st.selectbox(
                "Payment Method",
                [
                    "Electronic check",
                    "Mailed check",
                    "Bank transfer (automatic)",
                    "Credit card (automatic)"
                ],
                key="payment_method"
            )

        with col2:

            paperless_billing = st.selectbox(
                "Paperless Billing",
                ["Yes", "No"],
                key="paperless_billing"
            )

        st.divider()

        st.subheader("Customer Charges")

        monthly_charges = st.slider(
            "Monthly Charges ($)",
            min_value=18.25,
            max_value=118.75,
            value=70.0,
            step=0.25,
            key="monthly_charges"
        )

        total_charges = st.slider(
            "Total Charges ($)",
            min_value=0.0,
            max_value=8684.80,
            value=840.0,
            step=10.0,
            key="total_charges"
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            previous_clicked = st.form_submit_button(
                "← Previous: Services",
                use_container_width=True
            )

        with col2:

            next_clicked = st.form_submit_button(
                "Next: Account Info →",
                use_container_width=True
            )

    if previous_clicked:

        save_form_state(billing_fields)

        navigate_to(1)

    if next_clicked:

        save_form_state(billing_fields)

        navigate_to(3)


# ==================================================
# 10. STEP 3 - ACCOUNT INFORMATION
# ==================================================

elif step == 3:

    account_fields = [
        "gender",
        "senior_citizen",
        "partner",
        "dependents",
        "tenure",
        "contract"
    ]

    restore_form_state(account_fields)

    with st.form("account_form"):

        st.subheader("Customer Demographics")

        col1, col2 = st.columns(2)

        with col1:

            gender = st.selectbox(
                "Gender",
                ["Female", "Male"],
                key="gender"
            )

            senior_citizen = st.selectbox(
                "Senior Citizen",
                [0, 1],
                format_func=lambda x: (
                    "Yes" if x == 1 else "No"
                ),
                key="senior_citizen"
            )

        with col2:

            partner = st.selectbox(
                "Partner",
                ["Yes", "No"],
                key="partner"
            )

            dependents = st.selectbox(
                "Dependents",
                ["Yes", "No"],
                key="dependents"
            )

        st.divider()

        st.subheader("Account Details")

        tenure = st.slider(
            "Customer Tenure (Months)",
            min_value=0,
            max_value=72,
            value=12,
            step=1,
            key="tenure"
        )

        contract = st.selectbox(
            "Contract Type",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ],
            key="contract"
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            previous_clicked = st.form_submit_button(
                "← Previous: Billing",
                use_container_width=True
            )

        with col2:

            finish_clicked = st.form_submit_button(
                "Complete Customer Information",
                use_container_width=True
            )

    if previous_clicked:

        save_form_state(account_fields)

        navigate_to(2)

    if finish_clicked:

        save_form_state(account_fields)

        # Collect all 19 customer features

        customer_data = {

            "gender": st.session_state.saved_gender,

            "SeniorCitizen": (
                st.session_state.saved_senior_citizen
            ),

            "Partner": st.session_state.saved_partner,

            "Dependents": st.session_state.saved_dependents,

            "tenure": st.session_state.saved_tenure,

            "PhoneService": st.session_state.saved_phone_service,

            "MultipleLines": st.session_state.saved_multiple_lines,

            "InternetService": st.session_state.saved_internet_service,

            "OnlineSecurity": st.session_state.saved_online_security,

            "OnlineBackup": st.session_state.saved_online_backup,

            "DeviceProtection": st.session_state.saved_device_protection,

            "TechSupport": st.session_state.saved_tech_support,

            "StreamingTV": st.session_state.saved_streaming_tv,

            "StreamingMovies": st.session_state.saved_streaming_movies,

            "Contract": st.session_state.saved_contract,

            "PaperlessBilling": st.session_state.saved_paperless_billing,

            "PaymentMethod": st.session_state.saved_payment_method,

            "MonthlyCharges": st.session_state.saved_monthly_charges,

            "TotalCharges": st.session_state.saved_total_charges

        }

        # Store customer information

        st.session_state.customer_data = customer_data

        st.session_state.form_completed = True

        st.success(
            "Customer information collected successfully!"
        )


# ==================================================
# 11. CUSTOMER DATA SUMMARY
# ==================================================

if st.session_state.form_completed:

    st.divider()

    st.header("Customer Information Summary")

    customer_df = pd.DataFrame(
        [st.session_state.customer_data]
    )

    # Preserve original training feature order

    customer_df = customer_df[feature_columns]

    st.dataframe(
        customer_df,
        use_container_width=True
    )

    st.write(
        f"Number of features: {customer_df.shape[1]}"
    )

    st.write(
        f"Number of customers: {customer_df.shape[0]}"
    )

    
    if customer_df.shape[1] == 19:

        st.success(
            "All 19 customer features are ready."
        )

        st.divider()

        st.header("Churn Prediction")

        if st.button(
            "Predict Customer Churn",
            use_container_width=True
        ):

            # Get prediction probabilities
            probabilities = model.predict_proba(customer_df)[0]

            # Identify the probability belonging to Yes
            yes_index = list(model.classes_).index("Yes")

            churn_probability = probabilities[yes_index]

            # Apply the selected threshold
            prediction = (
                "Yes"
                if churn_probability >= threshold
                else "No"
            )

            st.subheader("Prediction Result")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Churn Probability",
                    f"{churn_probability:.2%}"
                )

            with col2:
                st.metric(
                    "Prediction",
                    "Likely to Churn" if prediction == "Yes"
                    else "Unlikely to Churn"
                )

            st.progress(float(churn_probability))

            if prediction == "Yes":

                st.warning(
                    "This customer has been classified "
                    "as having elevated churn risk."
                )

            else:

                st.success(
                    "This customer has been classified "
                    "as unlikely to churn."
                )

            st.caption(
                f"Classification threshold: {threshold:.2f}"
            )
