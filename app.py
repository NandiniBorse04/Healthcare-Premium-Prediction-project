import streamlit as st
import pandas as pd
from joblib import load

# ------------------ Page Config ------------------ #
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🏥",
    layout="wide"
)

# ------------------ Load Model ------------------ #
model = load("model.pkl")
scaler = load("scaler.pkl")

# ------------------ Custom CSS ------------------ #
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:40px;
    color:#2E86C1;
    font-weight:bold;
}
.sub-title{
    text-align:center;
    color:gray;
    margin-bottom:25px;
}
.result-box{
    background-color:#E8F8F5;
    padding:20px;
    border-radius:12px;
    border-left:8px solid #28B463;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🏥 Insurance Premium Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Predict Annual Medical Insurance Premium using Machine Learning</div>", unsafe_allow_html=True)

# ------------------ Inputs ------------------ #

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 30)

    dependants = st.slider(
        "Number of Dependants",
        0,
        10,
        1
    )

    income_level = st.slider(
        "Income Level",
        1,
        10,
        5
    )

    income_lakhs = st.number_input(
        "Annual Income (Lakhs ₹)",
        1.0,
        100.0,
        10.0
    )

    insurance_plan = st.selectbox(
        "Insurance Plan",
        [1,2,3]
    )

    risk_score = st.slider(
        "Risk Score",
        0.0,
        1.0,
        0.50
    )

with col2:

    gender = st.radio(
        "Gender",
        ["Female","Male"]
    )

    region = st.selectbox(
        "Region",
        ["Northeast","Northwest","Southeast","Southwest"]
    )

    marital = st.selectbox(
        "Marital Status",
        ["Married","Unmarried"]
    )

    bmi = st.selectbox(
        "BMI Category",
        ["Normal","Underweight","Overweight","Obesity"]
    )

    smoking = st.selectbox(
        "Smoking Status",
        ["Non-Smoker","Occasional","Regular"]
    )

    employment = st.selectbox(
        "Employment Status",
        ["Unemployed","Salaried","Self-Employed"]
    )

st.divider()

# ------------------ Prediction ------------------ #

if st.button("🔍 Predict Premium", use_container_width=True):

    input_data = {

        "age": age,
        "number_of_dependants": dependants,
        "income_level": income_level,
        "income_lakhs": income_lakhs,
        "insurance_plan": insurance_plan,
        "normalized_risk_score": risk_score,

        "gender_Male": 1 if gender=="Male" else 0,

        "region_Northwest":1 if region=="Northwest" else 0,
        "region_Southeast":1 if region=="Southeast" else 0,
        "region_Southwest":1 if region=="Southwest" else 0,

        "marital_status_Unmarried":1 if marital=="Unmarried" else 0,

        "bmi_category_Obesity":1 if bmi=="Obesity" else 0,
        "bmi_category_Overweight":1 if bmi=="Overweight" else 0,
        "bmi_category_Underweight":1 if bmi=="Underweight" else 0,

        "smoking_status_Occasional":1 if smoking=="Occasional" else 0,
        "smoking_status_Regular":1 if smoking=="Regular" else 0,

        "employment_status_Salaried":1 if employment=="Salaried" else 0,
        "employment_status_Self-Employed":1 if employment=="Self-Employed" else 0
    }

    feature_order = [
        'age',
        'number_of_dependants',
        'income_level',
        'income_lakhs',
        'insurance_plan',
        'normalized_risk_score',
        'gender_Male',
        'region_Northwest',
        'region_Southeast',
        'region_Southwest',
        'marital_status_Unmarried',
        'bmi_category_Obesity',
        'bmi_category_Overweight',
        'bmi_category_Underweight',
        'smoking_status_Occasional',
        'smoking_status_Regular',
        'employment_status_Salaried',
        'employment_status_Self-Employed'
    ]

    df = pd.DataFrame([input_data])[feature_order]

    cols_to_scale = [
        "age",
        "number_of_dependants",
        "income_level",
        "income_lakhs",
        "insurance_plan"
    ]

    df_scaled = df.copy()
    df_scaled[cols_to_scale] = scaler.transform(df_scaled[cols_to_scale])

    prediction = model.predict(df_scaled)[0]

    st.markdown("---")

    st.markdown(
        f"""
        <div class="result-box">
            <h2 style="color:#1E8449;">💰 Predicted Annual Premium</h2>
            <h1 style="color:#117A65;">₹ {prediction:,.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )



st.sidebar.title("ℹ About")

st.sidebar.info("""
This application predicts the **Annual Insurance Premium**
using a trained **Linear Regression Model**.

### Features Used
- Age
- Dependants
- Income
- Insurance Plan
- Risk Score
- Gender
- Region
- BMI Category
- Smoking Status
- Employment Status

Built with ❤️ using Streamlit.
""")