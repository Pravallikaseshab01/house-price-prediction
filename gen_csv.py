import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("indian_housing_data.csv")

# Set Seaborn style
sns.set_style("whitegrid")
plt.figure(figsize=(15, 12))

# 🎨 Define color palette
colors = ["blue", "red", "green", "purple", "orange", "black"]

# 🔹 1. Family Income Distribution
plt.subplot(2, 3, 1)
sns.histplot(df["FamilyIncome"], bins=30, kde=True, color=colors[0])
plt.axvline(df["FamilyIncome"].mean(), color='r', linestyle="--", label="Mean")
plt.title("Family Income Distribution")
plt.xlabel("Family Income (INR)")
plt.ylabel("Count")
plt.legend()

# 🔹 2. House Age Distribution
plt.subplot(2, 3, 2)
sns.histplot(df["HouseAge"], bins=30, kde=True, color=colors[1])
plt.axvline(df["HouseAge"].mean(), color='b', linestyle="--", label="Mean")
plt.title("House Age Distribution")
plt.xlabel("House Age (Years)")
plt.ylabel("Count")
plt.legend()

# 🔹 3. Rooms per Household Distribution
plt.subplot(2, 3, 3)
sns.histplot(df["AveRooms"], bins=5, discrete=True, color=colors[2])
plt.axvline(df["AveRooms"].mean(), color='k', linestyle="--", label="Mean")
plt.title("Rooms per Household Distribution")
plt.xlabel("Average Rooms")
plt.ylabel("Count")
plt.legend()

# 🔹 4. Bedrooms per Household Distribution
plt.subplot(2, 3, 4)
sns.histplot(df["AveBedrms"], bins=5, discrete=True, kde=True, color=colors[3])
plt.axvline(df["AveBedrms"].mean(), color='k', linestyle="--", label="Mean")
plt.title("Bedrooms per Household Distribution")
plt.xlabel("Average Bedrooms")
plt.ylabel("Count")
plt.legend()

# 🔹 5. Occupancy per Household Distribution
plt.subplot(2, 3, 5)
sns.histplot(df["AveOccup"], bins=15, kde=True, color=colors[4])
plt.axvline(df["AveOccup"].mean(), color='k', linestyle="--", label="Mean")
plt.title("Occupancy per Household Distribution")
plt.xlabel("Average Occupancy")
plt.ylabel("Count")
plt.legend()

# 🔹 6. Predicted Price Distribution
plt.subplot(2, 3, 6)
sns.histplot(df["Price"], bins=50, kde=True, color=colors[5])
plt.axvline(df["Price"].mean(), color='b', linestyle="--", label="Mean")
plt.title("Predicted House Price Distribution")
plt.xlabel("Predicted Price (INR)")
plt.ylabel("Count")
plt.legend()

plt.tight_layout()
plt.show()

# 🔹 7. Relationship Between Features & House Price
plt.figure(figsize=(15, 5))

# 🔸 Family Income vs. Predicted Price
plt.subplot(1, 3, 1)
sns.scatterplot(x=df["FamilyIncome"], y=df["Price"], color='red', alpha=0.6)
plt.title("Family Income vs Predicted Price")
plt.xlabel("Family Income (INR)")
plt.ylabel("Predicted Price (INR)")

# 🔸 House Age vs. Predicted Price
plt.subplot(1, 3, 2)
sns.scatterplot(x=df["HouseAge"], y=df["Price"], color='blue', alpha=0.6)
plt.title("House Age vs Predicted Price")
plt.xlabel("House Age (Years)")
plt.ylabel("Predicted Price (INR)")

# 🔸 Rooms per Household vs. Predicted Price
plt.subplot(1, 3, 3)
sns.scatterplot(x=df["AveRooms"], y=df["Price"], color='green', alpha=0.6)
plt.title("Rooms per Household vs Predicted Price")
plt.xlabel("Average Rooms")
plt.ylabel("Predicted Price (INR)")

plt.tight_layout()
plt.show()
