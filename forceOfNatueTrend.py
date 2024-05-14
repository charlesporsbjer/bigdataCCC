# Import necessary libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect('deathdata.db')

# Query to get the total deaths for exposure to forces of nature for 'World' by year
world_causes_query = """
SELECT 
    Year,
    SUM("Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Number)") AS "Exposure to forces of nature"
FROM death_causes
WHERE Entity = 'World'
GROUP BY Year
ORDER BY Year
"""

# Execute the query and store the result in a DataFrame
world_causes_result = pd.read_sql(world_causes_query, conn)

# Close the database connection
conn.close()

# Check if data is available and process it
if not world_causes_result.empty and not world_causes_result.isna().all().all():
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(world_causes_result['Year'], world_causes_result['Exposure to forces of nature'], marker='o', label='Exposure to Forces of Nature Deaths')

    # Adding a trend line
    z = np.polyfit(world_causes_result['Year'], world_causes_result['Exposure to forces of nature'], 1)
    p = np.poly1d(z)
    plt.plot(world_causes_result['Year'], p(world_causes_result['Year']), linestyle='--', color='r', label='Trend Line')

    plt.title('Deaths Due to Exposure to Forces of Nature (World, 1990 - 2004)')
    plt.xlabel('Year')
    plt.ylabel('Number of Deaths')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("No data available for 'World' or data is incomplete.")
