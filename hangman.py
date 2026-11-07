import random
words = ["python", "computer", "program", "coding", "developer"]
word = random.choice(words)
Assumed_letters = []
attempts = 6

print("===== WELCOME TO HANGMAN GAME =====")
while attempts > 0:
    display = ""

    for letter in word:
        if letter in Assumed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts remaining:", attempts)

    if all(letter in Assumed_letters for letter in word):
        print("Congratulations! You win the Gamegit status!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in Assumed_letters:
        print("You already guessed that letter!")
        continue

    Assumed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)
