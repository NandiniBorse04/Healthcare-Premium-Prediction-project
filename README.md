# 🏥 Healthcare Premium Prediction

This project implements a **Healthcare Premium Prediction Model** that estimates an individual's annual healthcare insurance premium based on demographic, financial, and lifestyle information.
The model is trained using Machine Learning regression techniques and deployed through an interactive **Streamlit Web Application**, allowing users to enter their information and receive an estimated premium instantly.

# 📖 1. Project Overview

Healthcare insurance premiums vary depending on several personal, medical, and financial factors such as age, annual income, BMI, smoking habits, employment status, and insurance plan.
This project provides an end-to-end Machine Learning solution that predicts annual healthcare insurance premiums using these attributes.

### 🎯 Applications

* Insurance companies for premium estimation
* Customers for insurance cost prediction
* Machine Learning regression demonstration
* Streamlit deployment project
* Portfolio project for Data Science & Machine Learning
* 
# 📂 2. Project Structure

```text
Healthcare-Premium-Prediction/
│
│── model.pkl
│── scaler.pkl
│── features.pkl
│
├── app.py
├── ml_premium_prediction.ipynb
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

# 📊 3. Features Used for Prediction

The model predicts healthcare insurance premiums using the following features.

| **Feature**               | **Description**                                                 |
| ------------------------- | --------------------------------------------------------------- |
| **Age**                   | Age of the applicant                                            |
| **Number of Dependants**  | Number of dependent family members                              |
| **Annual Income (Lakhs)** | Annual income in ₹ Lakhs                                        |
| **Gender**                | Male or Female                                                  |
| **Region**                | Residential region                                              |
| **Marital Status**        | Married or Single                                               |
| **BMI Category**          | Underweight, Normal, Overweight, Obesity                        |
| **Smoking Status**        | Smoker or Non-Smoker                                            |
| **Employment Status**     | Salaried, Self-employed, Freelancer, Business Owner, Unemployed |
| **Insurance Plan**        | Bronze, Silver, Gold                                            |
| **Income Level**          | Income category derived from annual income                      |


# ⚙️ 4. Installation Instructions

Follow the steps below to run the project locally.

### Clone the Repository

```bash
git clone https://github.com/NandiniBorse04/Healthcare-Premium-Prediction-project.git
```

### Navigate to the Project Folder

```bash
cd Healthcare-Premium-Prediction-project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

# 🤖 5. Modeling Approach

## Data Preprocessing

* Missing value handling
* Feature engineering
* Categorical variable encoding
* StandardScaler feature scaling
* Input validation

## Model

The project uses a trained Machine Learning Regression model for healthcare premium prediction.

The following serialized objects are used:

* **model.pkl** — Trained Regression Model
* **scaler.pkl** — StandardScaler object

# 📈 6. Results & Performance

The model predicts the **Estimated Annual Healthcare Insurance Premium** based on user-provided information.

### Key Output

* Estimated Annual Premium
* Real-Time Prediction
* Automatic Feature Scaling
* Fast Model Inference

# 🌐 7. Streamlit Web Application

The Streamlit application allows users to:

* Enter customer information
* Select Insurance Plan
* Choose BMI Category
* Select Smoking Status
* Select Employment Status
* Predict Healthcare Premium Instantly

### Workflow

1. Enter user details
2. Select lifestyle information
3. Click **Predict**
4. View the estimated healthcare insurance premium

# 🛠️ 8. Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib
* Jupyter Notebook

# 📦 9. Dependencies

Install all required packages using

```bash
pip install -r requirements.txt
```

Main libraries include:

* pandas
* numpy
* scikit-learn
* streamlit
* joblib
* matplotlib

# 📁 10. Dataset

**Note**

The original training dataset is **not included** in this repository.

Only the trained model, preprocessing files, and Streamlit application are provided.

# 🚀 11. Future Enhancements

* Advanced ensemble learning models
* Explainable AI using SHAP
* Hyperparameter optimization
* REST API using FastAPI
* Docker support
* Cloud deployment on AWS/Azure/GCP
* User authentication
* Database integration

# 📜 12. License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---
