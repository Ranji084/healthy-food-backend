import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="healthy_food_db"
)

cursor = conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(100),
 email VARCHAR(100),
 password VARCHAR(100)
)
""")

# MEALS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS meals (
 id INT AUTO_INCREMENT PRIMARY KEY,
 user_id INT,
 breakfast TEXT,
 lunch TEXT,
 snacks TEXT,
 dinner TEXT,
 calories FLOAT,
 protein FLOAT,
 carbs FLOAT,
 fats FLOAT
)
""")

# WELLNESS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS wellness (
 id INT AUTO_INCREMENT PRIMARY KEY,
 user_id INT,
 sleep_hours INT,
 water_intake FLOAT,
 health_score FLOAT,
 recommendations TEXT
)
""")

print("Tables Created Successfully")
