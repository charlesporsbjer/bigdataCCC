# Import necessary libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect('deathdata.db')

# Query to get the total deaths for specified causes for 'World' by year
world_causes_query = """
SELECT 
    Year,
    SUM("Deaths - Measles - Sex: Both - Age: All Ages (Number)") AS "Measles",
    SUM("Deaths - Tuberculosis - Sex: Both - Age: All Ages (Number)") AS "Tuberculosis",
    SUM("Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Number)") AS "HIV/AIDS",
    SUM("Deaths - Diarrheal diseases - Sex: Both - Age: All Ages (Number)") AS "Diarrheal diseases",
    SUM("Deaths - Protein-energy malnutrition - Sex: Both - Age: All Ages (Number)") AS "Protein-energy malnutrition"
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
    # Calculate the 'Fully Preventable' totals for each year
    world_causes_result['Fully Preventable'] = (
        world_causes_result['Measles'] +
        world_causes_result['Tuberculosis'] +
        world_causes_result['HIV/AIDS'] +
        world_causes_result['Diarrheal diseases'] +
        world_causes_result['Protein-energy malnutrition']
    )

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(world_causes_result['Year'], world_causes_result['Fully Preventable'], marker='o', label='Fully Preventable Deaths')

    # Adding a trend line
    z = np.polyfit(world_causes_result['Year'], world_causes_result['Fully Preventable'], 1)
    p = np.poly1d(z)
    plt.plot(world_causes_result['Year'], p(world_causes_result['Year']), linestyle='--', color='r', label='Trend Line')

    plt.title('Fully Preventable Deaths (World, 2015 - 2019)')
    plt.xlabel('Year')
    plt.ylabel('Number of Deaths')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("No data available for 'World' or data is incomplete.")
