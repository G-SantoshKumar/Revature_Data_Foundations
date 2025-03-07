import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations():
    df = pd.read_csv("output/cleaned_data.csv")

    # Ensure output/visualizations directory exists
    os.makedirs("output/visualizations", exist_ok=True)

    # Bar Chart - Animal Type Distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df['animal_type'], hue=df['animal_type'], palette="viridis", legend=False)
    plt.title("Animal Type Distribution")
    plt.xlabel("Animal Type")
    plt.ylabel("Count")
    plt.savefig("output/visualizations/animal_type_distribution.png")
    print("Saved: Animal Type Distribution Plot")

    # Histogram - Age Distribution
    df['age_years'] = (pd.to_datetime("today") - pd.to_datetime(df['dob'])).dt.days / 365
    plt.figure(figsize=(8, 5))
    plt.hist(df['age_years'], bins=20, color='skyblue', edgecolor='black')
    plt.title("Age Distribution of Animals")
    plt.xlabel("Age (Years)")
    plt.ylabel("Count")
    plt.savefig("output/visualizations/age_distribution.png")
    print("Saved: Age Distribution Histogram")

    # Scatter Plot - Geographic Location of Intakes
    plt.figure(figsize=(8, 5))
    plt.scatter(df['longitude'], df['latitude'], alpha=0.5, c='red')
    plt.title("Geographic Distribution of Intakes")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.savefig("output/visualizations/geographic_intakes.png")
    print("Saved: Geographic Intake Scatter Plot")

if __name__ == "__main__":
    create_visualizations()
