import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess():
    # Example: load CSV
    df = pd.read_csv("training_data.csv")

    # Basic cleaning
    df = df.dropna()

    # Train/test split
    train, test = train_test_split(df, test_size=0.2, random_state=42)

    # Save preprocessed files
    train.to_csv("training_data.csv", index=False)
    test.to_csv("training_data.csv", index=False)

    return "Preprocessing done"
