import pandas as pd

def analyze_data():
    df = pd.read_csv("output/cleaned_data.csv")
    print("\nBasic Statistics:")
    print(df.describe())

    print("\nAnimal Type Distribution:")
    print(df['animal_type'].value_counts())

    df['age_years'] = (pd.to_datetime("today") - pd.to_datetime(df['dob'])).dt.days / 365
    print("\n Average Age of Animals:", df['age_years'].mean())

if __name__ == "__main__":
    analyze_data()
