import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS healthyfoodhabitapp")

print("Database Created")
