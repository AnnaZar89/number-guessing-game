import os
import random

from flask import Flask, render_template, request, session, jsonify
from art import logo

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/")

def home():
    return render_template("index.html", logo=logo)



@app.route("/start", methods=['POST'])

def start():
    level_chosen = request.form["difficulty"]

    if level_chosen == "easy":
        num_of_guess = 10

    else:
        num_of_guess = 5
    session["num_of_guess"] = num_of_guess
    session["computer_value"] = random.randint(1, 100)
    session["difficulty_level"] = level_chosen
    return jsonify(level_chosen=level_chosen, num_of_guess=num_of_guess)


@app.route("/guess", methods=['POST'])

def guess():
    user_guess = int(request.form["guess"])
    computer_value = session["computer_value"]
    num_of_guess = session["num_of_guess"]

    if user_guess <= 0:
        message = "You lose. Game over!"

    elif computer_value == user_guess:
        message = f"Guessed! {user_guess} is the right answer!"
    else:
        num_of_guess -= 1
        session["num_of_guess"] = num_of_guess
        if num_of_guess == 0:
            message = f"You lose! The number was {computer_value}. Game over!"
        elif user_guess > computer_value:
            message = "Too high."
        else:
            message = "Too low."

    return jsonify(message=message, num_of_guess=num_of_guess)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

