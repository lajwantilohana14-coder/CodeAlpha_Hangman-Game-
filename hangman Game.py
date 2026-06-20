import random

# List of words
words = ["python", "laptop", "coding", "banana", "school"]

# Randomly choose a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Attempts
max_attempts = 6
wrong_attempts = 0

# Hangman stages
hangman_stages = [
"""
 -----
 |   |
 |
 |
 |
 |
=========
""",
"""
 -----
 |   |
 |   O
 |
 |
 |
=========
""",
"""
 -----
 |   |
 |   O
 |   |
 |
 |
=========
""",
"""
 -----
 |   |
 |   O
 |  /|
 |
 |
=========
""",
"""
 -----
 |   |
 |   O
 |  /|\\
 |
 |
=========
""",
"""
 -----
 |   |
 |   O
 |  /|\\
 |  /
 |
=========
""",
"""
 -----
 |   |
 |   O
 |  /|\\
 |  / \\
 |
=========
"""
]

print("=" * 40)
print("      WELCOME TO HANGMAN GAME")
print("=" * 40)
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect attempts.\n")

while wrong_attempts < max_attempts:

    print(hangman_stages[wrong_attempts])

    # Display guessed letters
    print("Guessed Letters:", guessed_letters)

    # Build display word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", secret_word)
        break

    print("Attempts Left:", max_attempts - wrong_attempts)

    guess = input("\nEnter a letter: ").lower()

    # Validation
    if len(guess) != 1:
        print("Please enter only ONE letter.")
        continue

    if not guess.isalpha():
        print("Please enter a valid alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        wrong_attempts += 1
        print("❌ Wrong Guess!")

# Lose condition
if wrong_attempts == max_attempts:
    print(hangman_stages[6])
    print("\n💀 GAME OVER!")
    print("The word was:", secret_word)

print("\nThank you for playing Hangman!")




