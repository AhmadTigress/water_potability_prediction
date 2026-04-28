import pandas as pd
import numpy as np
import pickle
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from dvclive import Live
import yaml

#from data_collection import load_data
#from model_building import prepare_data

#test_data = pd.read_csv("./data/processed/test_processed.csv")

#X_test = test_data.iloc[:, 0:-1].values
#y_test = test_data.iloc[:, -1].values

#model = pickle.load(open("model.pkl", "rb"))

def load_data(filepath : str) -> pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Errors loading data from {filepath}: {e}")


def prepare_data(data: pd.DataFrame):
    try:
        X = data.drop(['Potability'], axis=1)
        y = data['Potability']
        return X,y
    except Exception as e:
        raise Exception(f"Error preparing data : {e}")

def load_model(filepath: str):
    try:
        with open(filepath, "rb") as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        raise Exception(f"Error loading model from {filepath}: {e}")

def evaluation_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    try:
        params = yaml.safe_load(open("params.yaml", "r"))
        test_size = params["data_collection"]["test_size"]
        n_estimators = params["model_building"]["n_estimators"]
        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        with Live(save_dvc_exp=True) as live:
            live.log_metric("accuracy:", accuracy)
            live.log_metric("precision:", precision)
            live.log_metric("recall_score:", recall)
            live.log_metric("f1_score:", f1)

            live.log_param("test_size:", test_size)
            live.log_param("n_estimators:", n_estimators)

        metrics_dict = {
            "accuracy": accuracy,
            "precision": precision,
            "recall_score": recall,
            "f1_score": f1
        }
        return metrics_dict
    except Exception as e:
        raise Exception(f"Error evaluating a model: {e}")

def save_metrics(metrics_dict: dict, filepath: str) -> None:
    try:
        with open(filepath, 'w') as file:
            json.dump(metrics_dict, file, indent=4)
        print(f"Metrics successfully saved to {filepath}")
    except Exception as e:
        raise Exception(f"Error saving metrics to filepath: {e}")


def main():
    try:
        test_data_path = "./data/processed/test_processed.csv"
        model_path = "models/model.pkl"
        metrics_path = "reports/metrics.json"

        test_data = load_data(test_data_path)
        X_test, y_test = prepare_data(test_data)
        model = load_model(model_path)
        metrics = evaluation_model(model, X_test, y_test)
        save_metrics(metrics, metrics_path)
    except Exception as e:
        raise Exception(f"An error occured: {e}")

if __name__=="__main__":
    main()