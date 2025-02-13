import duckdb
import os
import pandas as pd

def load_to_duckdb(cleaned_data_path: str, database_path: str, table_name: str):
    """
    Load processed e-commerce data into DuckDB.
    
    Parameters:
        cleaned_data_path (str): Path to the cleaned CSV file.
        database_path (str): Path to the DuckDB database file.
        table_name (str): Name of the table where data will be loaded.
    """
    try:
        # Ensure the cleaned data file exists
        if not os.path.exists(cleaned_data_path):
            raise FileNotFoundError(f"Cleaned data file not found: {cleaned_data_path}")

        # Load the cleaned data into a Pandas DataFrame
        print("Loading cleaned data from CSV...")
        df = pd.read_csv(cleaned_data_path)

        # Validate that the DataFrame is not empty
        if df.empty:
            raise ValueError("The cleaned dataset is empty. Please check your transformation step.")

        # Connect to DuckDB (creates a new database if it doesn't exist)
        print(f"Connecting to DuckDB at: {database_path}")
        conn = duckdb.connect(database_path)

        # Create or replace the table and load the data
        print(f"Loading data into DuckDB table: {table_name}...")
        conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")

        print(f"Data successfully loaded into the DuckDB table '{table_name}'.")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Validation Error: {e}")
    except duckdb.DatabaseError as e:
        print(f"DuckDB Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Clean up resources
        if 'conn' in locals() and conn is not None:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Paths and table configuration
    cleaned_data_path = "data\cleaned\cleaned_electronics_data.csv"  # Path to the cleaned CSV file
    database_path = "data/duckdb/ecommerce.db"                  # Path to DuckDB database file
    table_name = "ecommerce_data"                              # Table name

    # Ensure the database directory exists
    os.makedirs(os.path.dirname(database_path), exist_ok=True)

    # Load the data into DuckDB
    load_to_duckdb(cleaned_data_path, database_path, table_name)
