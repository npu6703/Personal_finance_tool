from data_engineering_process.extract_data import extract_data
from data_engineering_process.transform_data import transform_data
from data_engineering_process.load_data import load_data_to_db

# Step 1: Extract data
data = extract_data()

# Step 2: Transform data
cleaned_data = transform_data(data)

# Step 3: Load data
db_url = 'mysql+mysqlconnector://personal:project@localhost/finance_db'
table_name = 'transactions'
load_data_to_db(cleaned_data, db_url, table_name)
