import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE healthy_food_db")

print("Database Created")
