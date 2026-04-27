import pandas as pd
import numpy as np
import os

from data_collection import load_data, save_data


def fill_missing_with_median(df):
    try:
        for column in df.columns:
            if df[column].isnull().any():
                median_value = df[column].median()
                df[column].fillna(median_value, inplace=True)
        return df
    except Exception as e:
        raise Exception(f"Error filling missing values : {e}")


def main():
    raw_data_path = "./data/raw"
    processed_data_path = "./data/processed"
    os.makedirs(processed_data_path)
    try:
        train_data = load_data(os.path.join(raw_data_path, "train.csv"))
        test_data = load_data(os.path.join(raw_data_path, "test.csv"))

        train_processed_data = fill_missing_with_median(train_data)
        test_processed_data = fill_missing_with_median(test_data)

        save_data(train_processed_data, os.path.join(processed_data_path, "train_processed.csv"))
        save_data(test_processed_data, os.path.join(processed_data_path, "test_processed.csv"))
    except Exception as e:
        raise Exception(f"")


if __name__=="__main__":
    main()