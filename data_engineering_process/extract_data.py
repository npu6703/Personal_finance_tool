import kagglehub
import pandas as pd

def extract_data():
    # Download the dataset
    path = kagglehub.dataset_download("ismetsemedov/personal-budget-transactions-dataset")
        # print("Path to dataset files:", path)
    
    # Load the dataset
    file_path = "data_engineering_process/dataset/cleaned_data.csv"
    data = pd.read_csv(file_path)
    
    return data
