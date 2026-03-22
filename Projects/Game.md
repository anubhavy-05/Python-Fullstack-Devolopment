# Number Guessing Game (Python)

This is a simple command-line game where the computer chooses a random number, and the player tries to guess it.

## What This Game Does

1. The computer picks a secret number between `1` and `100`.
2. You enter your guess.
3. The game gives a hint:
	 - If your guess is too small, it asks you to try a bigger number.
	 - If your guess is too big, it asks you to try a smaller number.
4. The game repeats until you guess the correct number.
5. At the end, it shows how many attempts you took.

## Concepts Used

- `random.randint(1, 100)`: to generate a random secret number.
- `while True`: to keep running the game loop until the correct guess.
- `if / elif / else`: to compare your guess with the secret number.
- `attempts` counter: to track how many guesses were made.
- `break`: to stop the loop when the answer is correct.

## Flow of Logic

- Start game and generate secret number.
- Set `attempts = 0`.
- Ask user for input using `input()` and convert it to integer using `int()`.
- Increase attempts by 1 after each guess.
- Compare guess:
	- `guess < secret_number` -> too low
	- `guess > secret_number` -> too high
	- otherwise -> correct guess, print success message, stop game

## Example Round

- Secret number (hidden): `42`
- User guess: `30` -> Hint: too small
- User guess: `60` -> Hint: too big
- User guess: `42` -> Correct
- Output: You won in `3` attempts.

## Small Improvement Ideas

- Add input validation to handle non-numeric input safely.
- Add difficulty levels (Easy: 1-50, Medium: 1-100, Hard: 1-500).
- Let the player choose to play again after winning.
