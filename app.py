from flask import Flask, request, jsonify
import mysql.connector
import requests
import re
from datetime import date
from flask_mail import Mail, Message
import random

app = Flask(__name__)

# ---------------- EMAIL CONFIG ----------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ranjithavangaveeti@gmail.com'
app.config['MAIL_PASSWORD'] = 'abxyurcdkhprgbcx'

mail = Mail(app)

# ---------------- API KEY ----------------
API_KEY = "tTgJqNFFeULlBzJJ18Z+fA==WalvHu2K4pA1RCB1"

# ---------------- DATABASE CONNECTION ----------------
def get_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="healthyfoodhabitapp"
        )
        return conn
    except mysql.connector.Error as err:
        print("Database connection failed:", err)
        return None

# ---------------- BMI FUNCTION ----------------
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = round(weight / (height_m * height_m), 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

# ---------------- PASSWORD VALIDATION ----------------
def is_password_strong(password):
    # Must contain alphabet, number and special character
    if not password:
        return False

    has_letter = re.search(r"[A-Za-z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[@#_$!%*?&]", password)

    return has_letter and has_digit and has_special

# ---------------- SIMPLE FOOD ANALYSIS ----------------
def analyze_food(food_text):

    food_text = food_text.lower()
    foods = re.split(r'[ ,]+', food_text)

    total_calories = total_protein = total_carbs = total_fat = 0

    for food in foods:

        if food in ["egg", "eggs"]:
            calories, protein, carbs, fat = 155, 13, 1, 11

        elif food == "rice":
            calories, protein, carbs, fat = 206, 4, 45, 1

        elif food == "milk":
            calories, protein, carbs, fat = 103, 8, 12, 2

        elif food == "banana":
            calories, protein, carbs, fat = 89, 1, 23, 0

        elif food == "chicken":
            calories, protein, carbs, fat = 239, 27, 0, 14

        else:
            continue

        total_calories += calories
        total_protein += protein
        total_carbs += carbs
        total_fat += fat

    return {
        "calories": total_calories,
        "protein": total_protein,
        "carbs": total_carbs,
        "fat": total_fat
    }

# ---------------- NUTRITION API ----------------
def get_nutrition_ai(food_text):

    try:
        response = requests.get(
            "https://api.calorieninjas.com/v1/nutrition",
            headers={"X-Api-Key": API_KEY},
            params={"query": food_text}
        )

        if response.status_code != 200:
            return None

        data = response.json()
        items = data.get("items", [])

        if not items:
            return None

        calories = sum(item.get("calories", 0) for item in items)
        protein = sum(item.get("protein_g", 0) for item in items)
        carbs = sum(item.get("carbohydrates_total_g", 0) for item in items)
        fat = sum(item.get("fat_total_g", 0) for item in items)

        return {
            "calories": calories,
            "protein": protein,
            "carbs": carbs,
            "fat": fat
        }

    except Exception as e:
        print("API ERROR:", e)
        return None

# ---------------- AI ADVICE ----------------
def generate_ai_advice(calories, protein, carbs, fat, meal_type):
    # Ensure meal_type is treated as a string
    meal_type = str(meal_type).lower() 
    
    advice_list = []
    
    if meal_type == "daily":
        if calories > 2500:
            advice_list.append("Your total calories for today are high. ")
        

    # Meal specific advice
    if meal_type == "breakfast":
        if fat > 15:
            advice_list.append("Try to avoid morning oily food. Opt for a lighter start for better energy.")
        elif protein < 10:
            advice_list.append("Your breakfast is low in protein. Adding eggs or sprouts can help.")
        else:
            advice_list.append("Great start! This breakfast looks light and healthy.")

    elif meal_type == "lunch":
        if carbs > 100:
            advice_list.append("This lunch is high in carbs. Try adding more fiber-rich veggies.")
        elif protein < 15:
            advice_list.append("Consider adding dal or lean protein to your lunch to feel fuller.")
        else:
            advice_list.append("Excellent! Your lunch is well-balanced.")

    elif meal_type == "snack":
        if calories > 300:
            advice_list.append("This snack is quite heavy. Try fruit or nuts for a healthier pick-me-up.")
        else:
            advice_list.append("Nice choice for a healthy snack.")

    elif meal_type == "dinner":
        if fat > 20 or calories > 600:
            advice_list.append("Try to keep dinner light and avoid oily food for better sleep and digestion.")
        else:
            advice_list.append("Perfect choice for a light and healthy dinner.")

    # Generic fallback if no specific rule is met
    if not advice_list:
        advice_list.append("This meal seems balanced. Remember to stay hydrated!")

    return " ".join(advice_list)

# ---------------- ROOT ----------------
@app.route("/")
def home():
    return "Healthy Food Habit Backend Running"

# ----------------FORGOT PASSWORD ----------------
import random
from flask_mail import Message

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
    try:
        data = request.json
        email = data.get("email")

        db = get_db()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        if not user:
            cursor.close()
            db.close()
            return jsonify({"message": "Email not found"})

        otp = random.randint(100000, 999999)

        cursor.execute(
            "UPDATE users SET otp=%s WHERE email=%s",
            (otp, email)
        )
        db.commit()

        # SEND EMAIL
        msg = Message(
            subject="Password Reset OTP",
            sender="yourgmail@gmail.com",
            recipients=[email]
        )

        msg.body = f"Your OTP for password reset is: {otp}"

        mail.send(msg)

        cursor.close()
        db.close()

        return jsonify({"message": "OTP sent to email"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#------------------------RESET PASSWORD-------------------
@app.route('/reset_password', methods=['POST'])
def reset_password():
    try:
        data = request.json
        email = data.get("email")
        new_password = data.get("password")

        # PASSWORD VALIDATION
        if not is_password_strong(new_password):
            return jsonify({
                "status": "fail",
                "message": "Password must contain alphabet, number and special character"
            })

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "UPDATE users SET password=%s WHERE email=%s",
            (new_password, email)
        )

        db.commit()

        cursor.close()
        db.close()

        return jsonify({
            "status": "success",
            "message": "Password updated successfully"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#------------------------VERIFT OTP------------------
@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    try:
        data = request.json
        email = data.get("email")
        otp = data.get("otp")

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND otp=%s",
            (email, otp)
        )

        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:
            return jsonify({"message": "OTP verified"})
        else:
            return jsonify({"message": "Invalid OTP"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- REGISTER ----------------
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    password = data.get("password", "")

    # PASSWORD VALIDATION
    if not is_password_strong(password):
        return jsonify({
            "status": "fail",
            "message": "Password must contain alphabet, number and special character"
        })

    db = get_db()

    if not db:
        return jsonify({"status": "error", "message": "Database not connected"})

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT id FROM users WHERE email=%s", (data["email"],))

    if cursor.fetchone():
        cursor.close()
        db.close()
        return jsonify({"status": "fail", "message": "Email already registered"})

    cursor.execute(
        "INSERT INTO users (name,email,password,goal) VALUES (%s,%s,%s,%s)",
        (data["name"], data["email"], data["password"], data["goal"])
    )

    db.commit()
    cursor.close()
    db.close()

    return jsonify({"status": "success", "message": "Registered Successfully"})

# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()
    db = get_db()

    if not db:
        return jsonify({"status": "error", "message": "Database not connected"})

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email=%s", (data["email"],))
    user = cursor.fetchone()

    cursor.close()
    db.close()

    if user and user["password"] == data["password"]:
        return jsonify({
            "status": "success",
            "user_id": user["id"],
            "name": user["name"]
        })
    else:
        return jsonify({"status": "fail", "message": "Invalid credentials"})

# ---------------- update profile----------------
@app.route("/update_profile", methods=["POST"])
def update_profile():

    data = request.get_json()

    user_id = data.get("user_id")
    name = data.get("name")
    age = data.get("age")
    height = data.get("height")
    weight = data.get("weight")
    gender = data.get("gender")

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE users
        SET name=%s, age=%s, height=%s, weight=%s, gender=%s
        WHERE id=%s
    """, (name, age, height, weight, gender, user_id))

    db.commit()

    cursor.close()
    db.close()

    return jsonify({
        "status": "success",
        "message": "Profile updated"
    })

# ---------------- ADD MEAL ----------------
@app.route("/add_meal", methods=["POST"])
def add_meal():

    data = request.get_json()

    user_id = data.get("user_id")
    meal_type = data.get("meal_type")
    food_text = data.get("food_text")

    if not user_id:
        return jsonify({"error": "user_id missing"}), 400

    if not food_text:
        return jsonify({"error": "food text missing"}), 400

    if not meal_type:
        return jsonify({"error": "meal_type missing"}), 400

    food_text = food_text.lower().strip()

    nutrition = get_nutrition_ai(food_text)

    if nutrition is None:
        return jsonify({
            "status": "fail",
            "message": "Food not recognized"
        })

    ai_tip = generate_ai_advice(
        nutrition["calories"],
        nutrition["protein"],
        nutrition["carbs"],
        nutrition["fat"],
        meal_type
    )

    db = get_db()

    if not db:
        return jsonify({"status": "error", "message": "Database not connected"})

    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO meals (user_id, meal_type, food_text, calories, protein, carbs, fat)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        user_id,
        meal_type,
        food_text,
        nutrition["calories"],
        nutrition["protein"],
        nutrition["carbs"],
        nutrition["fat"]
    ))

    db.commit()
    cursor.close()
    db.close()

    return jsonify({
        "status": "success",
        "meal_type": meal_type,
        "food": food_text,
        "nutrition": nutrition,
        "ai_tip": ai_tip
    })


# ---------------- VIEW INSIGHTS ----------------
@app.route("/view_insights", methods=["POST"])
def view_insights():

    data = request.get_json()
    user_id = data.get("user_id")

    if not user_id or user_id == -1:
        return jsonify({"status": "error", "message": "Invalid User ID"}), 400
    
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT meal_type, food_text, calories, protein, carbs, fat
        FROM meals
        WHERE user_id=%s AND DATE(created_at)=CURDATE()
    """, (user_id,))

    meals = cursor.fetchall()
    # If no meals logged today
    if not meals:
        cursor.close()
        db.close()
        return jsonify({
            "health_percentage": 0,
            "nutrition_totals": {
                "calories": 0,
                "protein": 0,
                "carbs": 0,
                "fat": 0
            },
            "meal_breakdown": {
                "breakfast": [],
                "lunch": [],
                "snack": [],
                "dinner": []
            },
            "ai_suggestion": "Log your first meal to see insights!"
        })
    total_cal = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    meal_breakdown = {
        "breakfast": [],
        "lunch": [],
        "snack": [],
        "dinner": []
    }

    for m in meals:

        total_cal += m["calories"]
        total_protein += m["protein"]
        total_carbs += m["carbs"]
        total_fat += m["fat"]

        meal_type = m["meal_type"].lower()

        meal_data = {
            "food": m["food_text"],
            "calories": m["calories"]
        }

        if meal_type in meal_breakdown:
            meal_breakdown[meal_type].append(meal_data)

    # ---------- Nutrient Percentage ----------
    nutrient_total = total_protein + total_carbs + total_fat

    if nutrient_total == 0:
        protein_percent = carbs_percent = fat_percent = 0
    else:
        protein_percent = round((total_protein / nutrient_total) * 100)
        carbs_percent = round((total_carbs / nutrient_total) * 100)
        fat_percent = round((total_fat / nutrient_total) * 100)

    nutrient_percentages = {
        "protein_percent": protein_percent,
        "carbs_percent": carbs_percent,
        "fat_percent": fat_percent
    }

    target_calories = 2000
    health_percent = min(100, round((total_cal / target_calories) * 100))

    ai_suggestion = generate_ai_advice(
        total_cal,
        total_protein,
        total_carbs,
        total_fat,
        "daily"
    )

    cursor.close()
    db.close()

    return jsonify({
        "health_percentage": health_percent,

        "nutrition_totals": {
            "calories": total_cal,
            "protein": total_protein,
            "carbs": total_carbs,
            "fat": total_fat
        },

        "nutrient_percentages": nutrient_percentages,

        "meal_breakdown": meal_breakdown,

        "ai_suggestion": ai_suggestion
    })

# ---------------- GET TODAY MEALS ----------------
@app.route("/meals/today/<int:user_id>", methods=["GET"])
def get_today_meals(user_id):

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT meal_type, food_text, calories, protein, carbs, fat
        FROM meals
        WHERE user_id=%s AND DATE(created_at)=CURDATE()
    """, (user_id,))

    meals = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify({
        "status": "success",
        "meals": meals
    })

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)