# Blackjack Python

A command-line Blackjack game written in Python.

Play against a computer-controlled dealer, choose whether to hit or stand, and track the results of completed rounds during the current session.

The application interface is in Polish.

---

## Features

- A freshly shuffled 52-card deck for every round.
- Two initial cards dealt to each side in alternating order.
- A hidden dealer hole card during the player's turn.
- Text-based card graphics.
- Hit and stand actions.
- Automatic ace values of 1 or 11.
- Natural blackjack detection.
- A dealer that stands on all totals of 17 or more, including soft 17.
- Explanations of round results.
- Session statistics for wins, losses, and draws.
- Input validation and graceful exit with Ctrl+C or end of input.

---

## Game Rules

The goal is to finish closer to 21 than the dealer without exceeding 21.

| Card | Value |
| --- | --- |
| 2–10 | Face value |
| J, Q, K | 10 |
| A | 11, reduced to 1 when needed |

A natural blackjack is exactly two cards totaling 21. It takes priority over a total of 21 made from more cards. If both sides have a natural blackjack, the round is a draw.

Initial natural blackjacks are resolved before further player or dealer actions.

If the player exceeds 21, the round ends immediately and the dealer does not draw. Otherwise, the dealer draws below 17 and stands on every total of 17 or more.

A soft total includes an ace counted as 11. The dealer stands on soft 17, such as an ace and a six.

This version uses hit and stand actions. Each round has its own full deck.

---

## Session Statistics

Completed rounds are counted as wins, losses, or draws.

The win rate is the number of wins divided by all completed rounds, including draws.

Statistics remain in memory for the current session and start again when the application is restarted. A round interrupted by Ctrl+C or end of input is not counted.

---

## Project Structure

| File | Responsibility |
| --- | --- |
| `game.py` | Deck creation, dealing, scoring, dealer rules, and round results |
| `main.py` | Terminal graphics, input, menus, game flow, and statistics |
| `README.md` | Project overview and usage instructions |
| `.gitignore` | Excludes local environments and generated files |

---

## Requirements

Python 3.12 or newer.

The project uses only the Python standard library.

---

## Installation

Open the project directory and create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

No third-party dependencies need to be installed.

---

## Running the Game

Run the following command from the directory containing both Python files:

```bash
python main.py
```

Choose a menu option:

| Option | Action |
| --- | --- |
| 1 | Play a round |
| 2 | Display session statistics |
| 3 | Display game rules |
| 0 | Exit |

During the player's turn, choose `1` to hit or `2` to stand.

---

## Technologies

- Python
- Python standard library: `random`
- Visual Studio Code
- Terminal

---

## Python Concepts Practiced

- Functions, parameters, and return values.
- Lists, tuples, and dictionaries.
- Loops and conditional statements.
- Mutating a deck with `pop()` and `shuffle()`.
- Flexible ace scoring with a `while` loop.
- Separating game logic from the interface.
- Importing functions between modules.
- Input validation.
- Exception handling and `finally`.
- String formatting and text graphics.
- `enumerate()`, `zip()`, slicing, and argument unpacking.

---

## Possible Future Improvements

- Persistent statistics.
- Additional player actions.
- Configurable game rules.
- A graphical interface.

---

## Educational and Portfolio Purpose

This project demonstrates game logic, user interaction, score calculation, and organizing a Python application into small functions and separate modules.
