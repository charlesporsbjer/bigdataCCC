# Import necessary libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect('deathdata.db')

# Query to get the total deaths for each cause for 'World' by year
world_causes_query = """
SELECT 
    Year,
    SUM("Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Number)") AS "Interpersonal violence",
    SUM("Deaths - Conflict and terrorism - Sex: Both - Age: All Ages (Number)") AS "Conflict and terrorism"
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
    # Calculate the 'Direct Violence' totals for each year
    world_causes_result['Direct Violence'] = (
        world_causes_result['Interpersonal violence'] +
        world_causes_result['Conflict and terrorism']
    )

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(world_causes_result['Year'], world_causes_result['Direct Violence'], marker='o', label='Direct Violence Deaths')

    # Adding a trend line
    z = np.polyfit(world_causes_result['Year'], world_causes_result['Direct Violence'], 1)
    p = np.poly1d(z)
    plt.plot(world_causes_result['Year'], p(world_causes_result['Year']), linestyle='--', color='r', label='Trend Line')

    plt.title('Direct Violence Deaths (World, 2015 - 2019)')
    plt.xlabel('Year')
    plt.ylabel('Number of Deaths')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("No data available for 'World' or data is incomplete.")
