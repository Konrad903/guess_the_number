
# 🎮 Guess The Number (Python Console Game)

A simple command-line number guessing game built using Python. The program generates a random secret number between **1 and 1000**, and challenges the user to guess it within a maximum of **10 attempts**. After each incorrect guess, the program provides feedback indicating whether the guess was too high or too low.

## 📌 Project Overview

This project demonstrates:

- Generating random numbers using Python's `random` module
- Using functions to organize program logic
- Implementing `while` loops for repeated execution
- Using conditional statements (`if`, `elif`, `else`)
- Taking user input using `input()`
- Converting string input into integers
- Handling invalid input using `try` and `except`
- Tracking the number of attempts using a global variable
- Providing feedback based on user guesses

## ⚙️ How It Works

### 1. Random Number Generation

- Imports all functions from Python's `random` module using `from random import *`.
- Generates a random integer between **1 and 1000** using `randint(1,1000)`.
- Stores the generated number in the variable `num`.
- Initializes `attempts = 0` to track the number of guesses.

### 2. Game Function (`play()`)

- Defines the main game function `play()`.
- Uses the `global attempts` statement to access and modify the global attempt counter.
- Initializes `won = False` to represent the initial winning state.
- Runs a `while` loop as long as `attempts < 10`.

### 3. Taking User Input

- Displays a welcome message.
- Accepts the user's guess using `input()`.
- Converts the entered value into an integer using `int()`.
- Increments the attempt counter with every guess.

### 4. Checking the Guess

The program compares the user's guess with the randomly generated number:

- **Guess Too High:** If `user > num`, displays a message indicating that the guess was too high.
- **Guess Too Low:** If `user < num`, displays a message indicating that the guess was too low.
- **Correct Guess:** If `user == num`, displays a winning message along with the secret number and exits the loop using `break`.

### 5. Trying Again

- After an incorrect guess, the program asks the user to type `"go"` to try again.
- If the user enters `"go"`, the `play()` function is called again.
- Uses `return` to exit the current function call after starting another game function call.

### 6. Invalid Input Handling

- Uses a `try` and `except ValueError` block to handle invalid numeric input.
- Displays an error message if the input cannot be converted into an integer.

### 7. Maximum Attempts

- The game allows a maximum of **10 attempts**.
- If the attempt counter reaches 10, the program displays a message indicating that the user has run out of attempts.
- Reveals the secret number when the user fails to guess it within the allowed attempts.

### 8. Starting the Game

- Calls `play()` at the end of the program to start the game automatically.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **random module** — Generates the secret random number
- **Command Line / Terminal** — User interaction

## ▶️ How to Run

### Requirements

- Python 3.x installed on your system
- A terminal or command prompt

### Execution

1. Save the Python source file as `Guess The Number.py`.
2. Open a terminal in the directory containing the file.
3. Execute the following command:

```bash
python "Guess The Number.py"
```

4. Enter your guesses when prompted.
5. Follow the feedback provided by the program until you win or run out of attempts.

## 🎯 Learning Outcomes

By completing this project, you can understand:

- How to generate random numbers in Python.
- How to build interactive console-based games.
- How to use loops and conditional statements.
- How to manage variables across functions using the `global` keyword.
- How to handle exceptions using `try` and `except`.
- How to control function execution using `break` and `return`.
