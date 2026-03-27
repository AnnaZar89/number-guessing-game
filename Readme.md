# Number Guessing Game 🎯

A number guessing game built with Python and Flask. The computer picks a random number between 1 and 100 — guess it before running out of attempts.

## Demo

TBA

## Features

- Web interface built with Flask
- Two difficulty levels: Easy (10 attempts) and Hard (5 attempts)
- Real-time feedback without page reload
- Hints after each incorrect guess (too high / too low)

## Tech Stack

- Python 3
- Flask
- HTML / CSS / JavaScript
- Session management for game state

## Installation

```bash
git clone https://github.com/your-username/number-guessing-game.git
cd number-guessing-game
pip install -r requirements.txt
python app.py
```

Then open your browser at `http://127.0.0.1:5000`

## How to Play

1. Choose difficulty: **Easy** (10 attempts) or **Hard** (5 attempts)
2. Enter your guess (number between 1 and 100)
3. Follow the hints until you guess correctly or run out of attempts

## Project Structure

```
number-guessing-game/
├── app.py
├── art.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## About

Day 11 project from the [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/), extended with a Flask web interface.