import sqlite3
import pandas as pd

conn = sqlite3.connect('deathdata.db')

josefin_query = """
SELECT 
    MIN(Total_Deaths) AS Least_Deaths,
    Cause
FROM (
    SELECT SUM("Deaths - Meningitis - Sex: Both - Age: All Ages (Number)") AS Total_Deaths, 'Meningitis' AS Cause FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Alzheimer's disease and other dementias - Sex: Both - Age: All Ages (Number)"), 'Alzheimer''s disease and other dementias' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Parkinson's disease - Sex: Both - Age: All Ages (Number)"), 'Parkinson''s disease' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Nutritional deficiencies - Sex: Both - Age: All Ages (Number)"), 'Nutritional deficiencies' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Malaria - Sex: Both - Age: All Ages (Number)"), 'Malaria' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Drowning - Sex: Both - Age: All Ages (Number)"), 'Drowning' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Number)"), 'Interpersonal violence' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Maternal disorders - Sex: Both - Age: All Ages (Number)"), 'Maternal disorders' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Number)"), 'HIV/AIDS' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Drug use disorders - Sex: Both - Age: All Ages (Number)"), 'Drug use disorders' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Tuberculosis - Sex: Both - Age: All Ages (Number)"), 'Tuberculosis' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)"), 'Cardiovascular diseases' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Lower respiratory infections - Sex: Both - Age: All Ages (Number)"), 'Lower respiratory infections' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Neonatal disorders - Sex: Both - Age: All Ages (Number)"), 'Neonatal disorders' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Alcohol use disorders - Sex: Both - Age: All Ages (Number)"), 'Alcohol use disorders' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Self-harm - Sex: Both - Age: All Ages (Number)"), 'Self-harm' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Number)"), 'Exposure to forces of nature' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Diarrheal diseases - Sex: Both - Age: All Ages (Number)"), 'Diarrheal diseases' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Environmental heat and cold exposure - Sex: Both - Age: All Ages (Number)"), 'Environmental heat and cold exposure' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Neoplasms - Sex: Both - Age: All Ages (Number)"), 'Neoplasms' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Conflict and terrorism - Sex: Both - Age: All Ages (Number)"), 'Conflict and terrorism' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Diabetes mellitus - Sex: Both - Age: All Ages (Number)"), 'Diabetes mellitus' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Chronic kidney disease - Sex: Both - Age: All Ages (Number)"), 'Chronic kidney disease' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Poisonings - Sex: Both - Age: All Ages (Number)"), 'Poisonings' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Protein-energy malnutrition - Sex: Both - Age: All Ages (Number)"), 'Protein-energy malnutrition' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Road injuries - Sex: Both - Age: All Ages (Number)"), 'Road injuries' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Chronic respiratory diseases - Sex: Both - Age: All Ages (Number)"), 'Chronic respiratory diseases' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Cirrhosis and other chronic liver diseases - Sex: Both - Age: All Ages (Number)"), 'Cirrhosis and other chronic liver diseases' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Digestive diseases - Sex: Both - Age: All Ages (Number)"), 'Digestive diseases' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Fire, heat, and hot substances - Sex: Both - Age: All Ages (Number)"), 'Fire, heat, and hot substances' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Acute hepatitis - Sex: Both - Age: All Ages (Number)"), 'Acute hepatitis' FROM death_causes
    UNION ALL
    SELECT SUM("Deaths - Measles - Sex: Both - Age: All Ages (Number)"), 'Measles' FROM death_causes
) AS Summed_Causes
GROUP BY Cause
ORDER BY Least_Deaths ASC
LIMIT 1;
"""
josefin_query_result = pd.read_sql(josefin_query, conn)

print(josefin_query_result)

conn.close()
