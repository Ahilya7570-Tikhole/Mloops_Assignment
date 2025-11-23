import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train():
    train_df = pd.read_csv("traning_data.csv")

    X = train_df.drop("target", axis=1)
    y = train_df["target"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "model.pkl")

    return "Training done"
