import pandas as pd
from sqlalchemy import create_engine

def load_data_to_db(cleaned_data, db_url, table_name):
    """
    Saves the cleaned data to a SQL database.

    Parameters:
    - cleaned_data: pd.DataFrame, the transformed data to load into the database.
    - db_url: str, the connection URL for the SQL database.
    - table_name: str, the name of the table where the data will be loaded.
    """
    # Create the database engine
    engine = create_engine(db_url)

    # Save to SQL
    cleaned_data.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data successfully loaded to the '{table_name}' table in the database.")

    # Verify by reading back from the database
        # query = f"SELECT * FROM {table_name} LIMIT 5;"
        # result = pd.read_sql(query, con=engine)
        # print("Sample data from the database:")
        # print(result)
