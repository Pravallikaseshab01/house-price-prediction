import pickle
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the trained model
with open("house_price_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load dataset properly
try:
    sample_data = pd.read_csv("indian_housing_data.csv")
except FileNotFoundError:
    st.error("Dataset 'indian_housing_data.csv' not found! Please generate it first.")
    sample_data = None  # Prevent crashes

# Streamlit App UI
st.title("Indian House Price Prediction App 🏡")
st.write("Enter the house details to predict the price in Indian Rupees.")

# Layout to align input fields
col1, col2 = st.columns(2)

with col1:
    FamilyIncome = st.number_input("Family Income (in INR)", value=1000000.0, min_value=200000.0, max_value=5000000.0, step=10000.0)
    HouseAge = st.number_input("House Age (years)", value=5, min_value=1, max_value=50, step=1)
    AveRooms = st.number_input("Average Rooms per Household", value=3, min_value=1, max_value=6, step=1)
    AveBedrms = st.number_input("Average Bedrooms per Household", value=1, min_value=1, max_value=5, step=1)

with col2:
    NumMembers = st.number_input("Number of Members in Family", value=3, min_value=1, max_value=10, step=1)
    AveOccup = st.number_input("Average Occupancy per Household", value=1.0, min_value=1.0, max_value=5.0, step=0.1)
    Latitude = st.number_input("Latitude", value=19.0, min_value=6.0, max_value=38.0, step=0.1)
    Longitude = st.number_input("Longitude", value=78.0, min_value=65.0, max_value=98.0, step=0.1)

if st.button("Predict Price 💰"):
    input_data = np.array([[FamilyIncome, HouseAge, AveRooms, AveBedrms, NumMembers, AveOccup, Latitude, Longitude]])
    raw_prediction = model.predict(input_data)[0]
    prediction = max(0, raw_prediction * 1000000)  # Convert to INR

    st.success(f"Estimated House Price: ₹{prediction:,.2f}")

    # Ensure dataset exists before visualization
    if sample_data is not None:
        st.subheader("📊 Data Visualizations")
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))

        # Check column names match dataset
        column_map = {
            "FamilyIncome": "Family Income",
            "HouseAge": "House Age",
            "AveRooms": "Average Rooms per Household",
            "AveBedrms": "Average Bedrooms per Household",
            "AveOccup": "Average Occupancy per Household",
            "Price": "Predicted Price"
        }

        # Rename columns to prevent KeyErrors
        sample_data.rename(columns=column_map, inplace=True)

        # Histograms
        sns.histplot(sample_data["Family Income"], ax=axes[0, 0], kde=True, color="blue")
        axes[0, 0].axvline(FamilyIncome, color='red', linestyle='dashed', linewidth=2)
        axes[0, 0].set_title("Family Income Distribution")

        sns.histplot(sample_data["House Age"], ax=axes[0, 1], kde=True, color="red")
        axes[0, 1].axvline(HouseAge, color='blue', linestyle='dashed', linewidth=2)
        axes[0, 1].set_title("House Age Distribution")

        sns.histplot(sample_data["Average Rooms per Household"], ax=axes[0, 2], kde=True, color="green")
        axes[0, 2].axvline(AveRooms, color='black', linestyle='dashed', linewidth=2)
        axes[0, 2].set_title("Rooms per Household Distribution")

        sns.histplot(sample_data["Average Bedrooms per Household"], ax=axes[1, 0], kde=True, color="purple")
        axes[1, 0].axvline(AveBedrms, color='black', linestyle='dashed', linewidth=2)
        axes[1, 0].set_title("Bedrooms per Household Distribution")

        sns.histplot(sample_data["Average Occupancy per Household"], ax=axes[1, 1], kde=True, color="orange")
        axes[1, 1].axvline(AveOccup, color='black', linestyle='dashed', linewidth=2)
        axes[1, 1].set_title("Occupancy per Household Distribution")

        sns.histplot(sample_data["Predicted Price"], ax=axes[1, 2], kde=True, color="black")
        axes[1, 2].axvline(prediction, color='blue', linestyle='dashed', linewidth=2)
        axes[1, 2].set_title("Predicted House Price Distribution")

        plt.tight_layout()
        st.pyplot(fig)
