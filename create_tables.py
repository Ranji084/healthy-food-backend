import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="healthyfoodhabitapp"
)

cursor = conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(100),
 email VARCHAR(100) UNIQUE,
 password VARCHAR(100),
 age INT,
 height FLOAT,
 weight FLOAT,
 gender VARCHAR(20),
 goal VARCHAR(100)
)
""")

# FOOD LOGS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS food_logs (
 id INT AUTO_INCREMENT PRIMARY KEY,
 user_id INT,
 meal_type VARCHAR(50),
 food_text TEXT,
 calories FLOAT,
 protein FLOAT,
 carbs FLOAT,
 fat FLOAT,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
