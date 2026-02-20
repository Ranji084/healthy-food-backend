from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="healthy_food_db"
)

cursor = db.cursor(dictionary=True)


@app.route("/")
def home():
    return "Healthy Food Backend Running ✅"


# ---------------- REGISTER ----------------
@app.route("/register", methods=["POST"])
def register():

    data = request.json
    name = data["name"]
    email = data["email"]
    password = data["password"]

    sql = "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
    cursor.execute(sql, (name, email, password))
    db.commit()

    return jsonify({"message": "User Registered"})


# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():

    data = request.json
    email = data["email"]
    password = data["password"]

    sql = "SELECT * FROM users WHERE email=%s AND password=%s"
    cursor.execute(sql, (email, password))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login Successful"})
    else:
        return jsonify({"message": "Invalid Email or Password"})


# ---------------- ADD WELLNESS ----------------
@app.route("/add_wellness", methods=["POST"])
def add_wellness():

    try:
        data = request.json

        sql = """INSERT INTO wellness
        (user_id, sleep_hours, water_intake, health_score, recommendations)
        VALUES (%s,%s,%s,%s,%s)"""

        values = (
            data.get("user_id"),
            data.get("sleep_hours"),
            data.get("water_intake"),
            data.get("health_score"),
            data.get("recommendations")
        )

        cursor.execute(sql, values)
        db.commit()

        return jsonify({"message": "Wellness Added Successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/add_meal", methods=["POST"])
def add_meal():

    data = request.get_json(force=True)
    print("Received Data:", data)

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    user_id = data.get("user_id")
    breakfast = data.get("breakfast")
    lunch = data.get("lunch")
    snacks = data.get("snacks")
    dinner = data.get("dinner")
    calories = data.get("calories")
    protein = data.get("protein")
    carbs = data.get("carbs")
    fats = data.get("fats")

    if user_id is None:
        return jsonify({"error": "user_id is required"}), 400

    sql = """INSERT INTO meals 
    (user_id, breakfast, lunch, snacks, dinner, calories, protein, carbs, fats)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    values = (user_id, breakfast, lunch, snacks, dinner, calories, protein, carbs, fats)

    cursor.execute(sql, values)
    db.commit()

    return jsonify({"message": "Meal Added Successfully"})

# ---------------- GET MEALS ----------------
@app.route("/get_meals/<int:user_id>", methods=["GET"])
def get_meals(user_id):

    sql = "SELECT * FROM meals WHERE user_id = %s"
    cursor.execute(sql, (user_id,))
    rows = cursor.fetchall()

    result = []

    for row in rows:
        result.append({
            "id": row["id"],
            "user_id": row["user_id"],
            "breakfast": row["breakfast"],
            "lunch": row["lunch"],
            "snacks": row["snacks"],
            "dinner": row["dinner"],
            "calories": row["calories"],
            "protein": row["protein"],
            "carbs": row["carbs"],
            "fats": row["fats"]
        })

    return jsonify(result)

   

# ---------------- GET WELLNESS ----------------
@app.route("/wellness/<int:user_id>", methods=["GET"])
def get_wellness(user_id):

    sql = "SELECT * FROM wellness WHERE user_id=%s"
    cursor.execute(sql, (user_id,))
    data = cursor.fetchall()

    return jsonify(data)

# ---------------- UPDATE MEAL ----------------
@app.route("/update_meal/<int:meal_id>", methods=["PUT"])
def update_meal(meal_id):

    try:
        data = request.json

        sql = """UPDATE meals SET
        breakfast=%s,
        lunch=%s,
        snacks=%s,
        dinner=%s,
        calories=%s,
        protein=%s,
        carbs=%s,
        fats=%s
        WHERE id=%s"""

        values = (
            data.get("breakfast"),
            data.get("lunch"),
            data.get("snacks"),
            data.get("dinner"),
            data.get("calories"),
            data.get("protein"),
            data.get("carbs"),
            data.get("fats"),
            meal_id
        )

        cursor.execute(sql, values)
        db.commit()

        return jsonify({"message": "Meal Updated Successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})
    
    # ---------------- DELETE MEAL ----------------
@app.route("/delete_meal/<int:meal_id>", methods=["DELETE"])
def delete_meal(meal_id):

    try:
        sql = "DELETE FROM meals WHERE id=%s"
        cursor.execute(sql, (meal_id,))
        db.commit()

        return jsonify({"message": "Meal Deleted Successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})
    
    # ---------------- ANALYZE HEALTH ----------------
@app.route("/analyze/<int:user_id>", methods=["GET"])
def analyze(user_id):

    try:
        # Get latest meal
        cursor.execute("SELECT * FROM meals WHERE user_id=%s ORDER BY id DESC LIMIT 1", (user_id,))
        meal = cursor.fetchone()

        # Get latest wellness
        cursor.execute("SELECT * FROM wellness WHERE user_id=%s ORDER BY id DESC LIMIT 1", (user_id,))
        wellness = cursor.fetchone()

        if not meal or not wellness:
            return jsonify({"message": "Meal or Wellness data not found"})

        calories = float(meal["calories"])
        protein = float(meal["protein"])
        water = float(wellness["water_intake"])
        sleep = float(wellness["sleep_hours"])

        score = 100
        recommendations = []

        # Simple AI Rules
        if calories > 2500:
            score -= 20
            recommendations.append("Reduce calorie intake")

        if protein < 40:
            score -= 20
            recommendations.append("Increase protein-rich foods")

        if water < 2:
            score -= 20
            recommendations.append("Drink more water")

        if sleep < 6:
            score -= 20
            recommendations.append("Improve sleep duration")

        return jsonify({
            "health_score": score,
            "recommendations": recommendations
        })

    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/recommend/<int:user_id>", methods=["GET"])
def recommend(user_id):

    cursor.execute("SELECT calories, protein, carbs, fats FROM meals WHERE user_id=%s", (user_id,))
    rows = cursor.fetchall()

    if not rows:
        return jsonify({"message": "No meal data found for recommendation"})

    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fats = 0

    for row in rows:
        total_calories += row["calories"]
        total_protein += row["protein"]
        total_carbs += row["carbs"]
        total_fats += row["fats"]

    # Simple AI Logic
    if total_calories > 2500:
        advice = "Your calorie intake is high. Try reducing fried foods."
    elif total_calories < 1500:
        advice = "Your calorie intake is low. Increase protein-rich foods."
    else:
        advice = "Your diet looks balanced. Keep maintaining it!"

    return jsonify({
        "total_calories": total_calories,
        "total_protein": total_protein,
        "total_carbs": total_carbs,
        "total_fats": total_fats,
        "recommendation": advice
    })


if __name__ == "__main__":
    app.run(debug=True)
