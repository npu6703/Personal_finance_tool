import pandas as pd

def transform_data(data):
    # 1. Convert 'date' to datetime format
    data['date'] = pd.to_datetime(data['date'])

    # 2. Check for missing values
    if data.isnull().sum().any():
        print("Missing values found. Handling missing data...")
        # Drop rows with missing values in important columns
        data = data.dropna(subset=['date', 'category', 'amount'])

    # 3. Standardize 'category' names
    data['category'] = data['category'].str.title()
    data['category'] = data['category'].replace({'Restuarant': 'Restaurant', 'Coffe': 'Coffee'}) 

    # 4. Check for negative amounts and drop invalid records
    data = data[data['amount'] >= 0]

    # 5. Remove duplicates
    data = data.drop_duplicates()

    # 6. Ensure there are no missing or incorrect values in critical columns
        # print(data.isnull().sum())
        # print(data.head())

    return data
