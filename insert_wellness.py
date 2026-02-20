from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

sql = """
INSERT INTO wellness
(user_id,sleep_hours,water_intake,health_score,recommendations)
VALUES (%s,%s,%s,%s,%s)
"""

values = (
 1,
 7,
 2.5,
 82,
 "Increase protein, Drink more water"
)

cursor.execute(sql, values)
conn.commit()

print("Wellness Data Added")
