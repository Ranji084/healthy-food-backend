import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="healthyfoodhabitapp"
)

cursor = conn.cursor()

# Drop the old meals table
cursor.execute("DROP TABLE IF EXISTS meals")

# Recreate with new structure
cursor.execute("""
CREATE TABLE meals (
 id INT AUTO_INCREMENT PRIMARY KEY,
 user_id INT,
 meal_type VARCHAR(50),
 food TEXT,
 calories FLOAT,
 protein FLOAT,
 carbs FLOAT,
 fat FLOAT
)
""")

conn.commit()
cursor.close()
conn.close()

print("Meals table updated")