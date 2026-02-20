from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

sql = """
INSERT INTO users (name,email,password)
VALUES (%s,%s,%s)
"""

values = ("Ranji","ranji@gmail.com","1234")

cursor.execute(sql, values)
conn.commit()

print("User Inserted")
