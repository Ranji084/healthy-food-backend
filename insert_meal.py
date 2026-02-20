from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

sql = """
INSERT INTO meals
(user_id,breakfast,lunch,snacks,dinner,calories,protein,carbs,fats)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

values = (
 1,
 "Idli",
 "Rice",
 "Nuts",
 "Chapati",
 2100,
 32,
 41,
 18
)

cursor.execute(sql, values)
conn.commit()

print("Meal Added")
