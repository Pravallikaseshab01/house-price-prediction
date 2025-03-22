**Indian House Price Prediction** project includes an overview, installation guide, usage instructions, dataset details, model training, and contributing guidelines.

---

### **📌 README.md**

# 🏡 Indian House Price Prediction App

## 📌 Overview
This project predicts house prices in various Indian cities based on factors such as **family income, house age, number of rooms, and geographical location**. It leverages **machine learning** to provide accurate price estimates, making it a valuable tool for buyers, sellers, and real estate analysts.

The **web application** is built using **Streamlit**, and the model is trained using **Scikit-Learn (Random Forest Regressor)**.

## 🚀 Features
✔️ Predicts **house prices** based on multiple factors  
✔️ **User-friendly interface** built with Streamlit  
✔️ **Interactive data visualizations** for insights  
✔️ Supports **custom user inputs**  
✔️ Uses **Indian real estate trends** for model training  

## 🛠️ Tech Stack
- **Frontend & Backend**: [Streamlit](https://streamlit.io/)
- **Machine Learning Model**: Scikit-Learn (`RandomForestRegressor`)
- **Data Visualization**: Matplotlib & Seaborn
- **Data Handling**: Pandas & NumPy
- **Dataset**: Synthetic Indian housing dataset (5000 samples)


## 📂 Project Structure
```
📁 Indian-House-Price-Prediction/
│── 📄 app.py              # Streamlit app for user interface
│── 📄 train_model.py      # Model training script
│── 📄 indian_housing_data.csv  # Synthetic dataset
│── 📄 house_price_model.pkl  # Trained ML model
│── 📄 requirements.txt    # Dependencies
│── 📄 README.md           # Project documentation
```

---

## 📦 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Indian-House-Price-Prediction.git
cd Indian-House-Price-Prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Generate Dataset (if missing)
```bash
python generate_dataset.py
```

### 4️⃣ Train the Model (if needed)
```bash
python train_model.py
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🎮 Usage
1. **Enter the house details** (family income, rooms, occupancy, etc.).
2. Click **"Predict Price 💰"**.
3. The app will **display the estimated house price**.
4. Explore **interactive data visualizations**.

---

## 📊 Dataset Details
The dataset is **synthetically generated** using Indian housing trends:
- **Cities Covered**: Mumbai, Delhi, Bangalore, Hyderabad, Chennai, Kolkata, Pune, Ahmedabad, Jaipur, Lucknow
- **Features**:
  - 🏠 `FamilyIncome` - Annual income of the family (INR)
  - 📏 `HouseAge` - Age of the house (years)
  - 🛏️ `AveRooms` - Average rooms per household
  - 🛌 `AveBedrms` - Average bedrooms per household
  - 👨‍👩‍👧‍👦 `NumMembers` - Number of family members
  - 🏢 `AveOccup` - Average occupancy per household
  - 🌍 `Latitude` & `Longitude` - Location coordinates
  - 💰 `Price` - House price in INR

---

## 🤖 Model Training
- The **Random Forest Regressor** is trained using `train_model.py`.
- The dataset is split into **80% training and 20% testing**.
- Model achieves **high accuracy with low RMSE**.

To retrain the model, run:
```bash
python train_model.py
```

---

## 📈 Visualizations in the App
- **Histograms** for **Family Income, House Age, Rooms, Bedrooms, Occupancy, and Price**.
- **User input is highlighted** with a red/blue dashed line for better insights.

---

## 🤝 Contributing:

Please feel free to make contributions if needed.

🔹 Fork the repository  
🔹 Create a feature branch (`git checkout -b feature-name`)  
🔹 Commit changes (`git commit -m "Add new feature"`)  
🔹 Push to your branch (`git push origin feature-name`)  
🔹 Create a Pull Request  

---

💡 **Developed by:** _Your Name_  
📧 **Contact:** pravallikaseshabhattar08@gmail.com  
🌍 **GitHub:** Pravallikaseshab01(https://github.com/yourusername)  
