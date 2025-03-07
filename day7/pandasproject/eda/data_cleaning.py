import pandas as pd
import os

def clean_data():
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-03-04/longbeach.csv"

    df = pd.read_csv(url)
    print(df)

    df['animal_name'] = df['animal_name'].fillna('Unknown')
    df = df.dropna(subset=['dob', 'intake_date'])  

    df = df.drop_duplicates()

    df['dob'] = pd.to_datetime(df['dob'], errors='coerce')
    df['intake_date'] = pd.to_datetime(df['intake_date'], errors='coerce')
    df['outcome_date'] = pd.to_datetime(df['outcome_date'], errors='coerce')

    os.makedirs("output", exist_ok=True)

    df.to_csv("output/cleaned_data.csv", index=False)
    print("✅ Data cleaning complete. Cleaned dataset saved.")

    return df 

if __name__ == "__main__":
    clean_data()
