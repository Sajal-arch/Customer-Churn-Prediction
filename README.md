# Customer Churn Prediction

An end-to-end machine learning project that predicts whether a telecom customer is likely to leave (churn) based on customer information.

## Project overview
- Dataset: Telco Customer Churn (7,043 rows and 21 columns in the working dataset).
- Target: `Churn` (`Yes` / `No`).
- Goal: build a classification model and provide predictions through a Streamlit web app.

## Project structure
```text
customer_churn_prediction/
├── app.py
├── customer_churn_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── README.md
└── models/
    └── README.md
```

## Run locally
1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Put your trained model file named `customer_churn_model.pkl` in the project root (or update the path in `app.py`).
5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Model and app
The trained model is saved as `customer_churn_model.pkl`. The Streamlit interface is in `app.py`. Make sure the app's input fields and preprocessing exactly match the features and preprocessing used during model training.

## Dataset
The dataset is not included in this repository by default. Add your dataset only if you have permission to share it. See `data/README.md`.

