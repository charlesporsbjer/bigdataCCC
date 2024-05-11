import pandas as pd
import sqlite3

# Specify the path to your CSV file
csv_file_path = 'data/annual-number-of-deaths-by-cause.csv'

# Specify the path to your SQLite database
db_file_path = 'deathdata.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_file_path)

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Drop the table if it already exists
    conn.execute('DROP TABLE IF EXISTS death_causes')

    # Write the data to a SQLite table
    df.to_sql('death_causes', conn, index=False, if_exists='replace')

    # Check if the table was created
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the connection
    conn.close()
