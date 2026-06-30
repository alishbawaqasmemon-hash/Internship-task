import random

# List of predefined words
words = ["python", "computer", "program", "hangman", "keyboard"]

# Randomly choose a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
incorrect_guesses = 0
max_attempts = 6

print("=" * 40)
print("        Welcome to Hangman!")
print("=" * 40)

while incorrect_guesses < max_attempts:

    # Display the current progress
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check correctness
    if guess in secret_word:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong!")
        print(f"Attempts Left: {max_attempts - incorrect_guesses}")

# If player loses
if incorrect_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)


```
