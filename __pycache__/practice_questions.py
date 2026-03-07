from practice_questions import ask_question

import json
from datetime import datetime

def update_streak():
    today = str(datetime.today().date())

    try:
        with open("streak.json", "r") as f:
            data = json.load(f)
    except:
        data = {"last_day": "", "streak": 0}

    if data["last_day"] != today:
        data["streak"] += 1
        data["last_day"] = today

    with open("streak.json", "w") as f:
        json.dump(data, f)

    return data["streak"]

    import random

def ask_question():
    q = random.choice(questions)

    user_answer = input(q["question"] + "\nYour answer: ")

    if user_answer.lower() in q["answer"].lower():
        print("✅ Correct!")
        streak = update_streak()
        print(f"🔥 Your practice streak: {streak} days")
    else:
        print("❌ Incorrect")
        print("Correct answer:", q["answer"])

