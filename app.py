import streamlit as st
import pickle
import numpy as np

# ---------- App Config ----------
st.set_page_config(page_title="Uber Ride Fare Prediction", page_icon="🚕", layout="centered")

# ---------- Simple Background + Font ----------
st.markdown("""
    <style>
        /* Light blue background */
        .stApp {
            background-color: #e6f0ff; /* soft light blue */
        }
        
        /* Font styling */
        html, body, [class*="css"] {
            font-family: "Poppins", sans-serif;
            font-size: 16px;
            color: #000000 !important;  /* black text */
        }

        /* Headings */
        h1, h2, h3 {
            font-family: "Poppins", sans-serif;
            font-weight: 700;
            color: #000000 !important;  /* black headings */
        }
            
         /* Force all headings and text black */
        h1, h2, h3, h4, h5, h6, p, span, label {
            color: #000000 !important;
        }
        /* Style for number input labels (Pickup/Dropoff text) */
        .stNumberInput label {
            font-family: "Courier New", monospace !important;  /* Change font */
            font-size: 15px !important;                       /* Adjust size */
            font-weight: 600 !important;                      /* Make bold */
            color: #003366 !important;                        /* Dark blue text */
        }

        /* Number input styling */
        .stNumberInput > div > div input {
            background: #ffffff !important;  /* white input */
            color: #000000 !important;       /* black text */
            border-radius: 8px !important;
            border: 1px solid #99bbff !important; /* soft blue border */
        }

        /* Button styling */
        .stButton > button {
            background: #3399ff;
            color: white;
            border-radius: 8px;
            padding: 0.6rem 1rem;
            font-weight: 600;
            border: none;
        }
        .stButton > button:hover {
            background: #2673cc;
            transition: 0.2s;
        }

        /* Success box */
        .stSuccess {
            background-color: #d9f2d9 !important;
            color: #000000 !important;  /* black text */
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)


# ---------- Load Model ----------
model = pickle.load(open("trained_model.sav", "rb"))

mse = 19.4611
r2 = 0.7523

# ---------- Title ----------
st.title("🚕Uber Ride Fare Prediction App")

# ---------- Model Performance ----------
st.write("### Model Performance")
st.write("**Model used K-Nearest Neighbours**")
st.write(f"**MSE:** {mse:.4f}")
st.write(f"**R² Score:** {r2:.4f}")
st.write("---")

# ---------- Inputs ----------
st.write("### Try Prediction Yourself")

pickup_longitude = st.number_input("Pickup Longitude:", value=-73.985, format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude:", value=40.758, format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude:", value=-73.981, format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude:", value=40.768, format="%.6f")
passenger_count = st.number_input("Passenger Count:", min_value=1, max_value=10, value=1)

features = np.array([[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count]])

# ---------- Predict ----------
if st.button("Predict Fare"):
    prediction = model.predict(features)
    st.success(f"Estimated Taxi Fare: ${prediction[0]:.2f}")
