# 🚕 Uber Taxi Fare Prediction

This project predicts **New York City taxi fares** based on
pickup/dropoff coordinates, passenger count, and other trip details.

## 📌 Features Used

-   **pickup_longitude**
-   **pickup_latitude**
-   **dropoff_longitude**
-   **dropoff_latitude**
-   **passenger_count**

## ⚙️ Models Compared

-   **KNN Regressor** ✅ (Best)
-   Random Forest Regressor
-   Gradient Boosting Regressor
-   XGBoost Regressor

## 🏆 Best Model

-   **KNN Regressor (n_neighbors=3, weights='distance')**
-   **MSE:** 19.46\
-   **R² Score:** 0.75

## 🚀 Deployment

The model is deployed using **Streamlit**.\
👉 [Try the Live App
Here](https://uber-price-prediction-b5.streamlit.app/)

## 🖼️ App Screenshot

<img width="804" height="879" alt="image" src="https://github.com/user-attachments/assets/7a098af1-e208-462b-bcd6-2f4cdc880db7" />

##  Technologies Used

- Python  
- Streamlit  
- scikit-learn  
- NumPy  
- pickle (for model serialization)

---
##  Example Input & Output

**Input:**
- Pickup: **(-73.999817, 40.738354)**  
- Dropoff: **(-73.999512, 40.723217)**  
- Passengers: **1**  

**Output:**
Estimated Taxi Fare: $22.43

---

##  Author

**Boomika S**

---


