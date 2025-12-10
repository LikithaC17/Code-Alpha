import random

# Predefined list of 5 words
words = ["apple", "tiger", "chair", "water", "music"]

# Pick a random word
secret_word = random.choice(words)
guessed = ["_"] * len(secret_word)
attempts = 6
used_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect attempts.\n")

# Main game loop
while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    print("Incorrect attempts left:", attempts)
    print("Used letters:", used_letters)
    
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single valid letter.\n")
        continue
    
    if guess in used_letters:
        print("⚠ You already used this letter!\n")
        continue

    used_letters.append(guess)

    # Check if letter is in the word
    if guess in secret_word:
        print("✔ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed[i] = guess
    else:
        print("❌ Wrong guess!\n")
        attempts -= 1

# Game result
if "_" not in guessed:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("😢 Out of attempts! The word was:", secret_word)
