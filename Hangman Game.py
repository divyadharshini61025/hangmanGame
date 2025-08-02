import random

words = ['apple', 'mango', 'grape', 'peach', 'lemon']
word = random.choice(words)
guesses = ''
attempts = 6

while attempts > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
    print()

    if failed == 0:
        print("You won!")
        break

    guess = input("Guess a letter: ")
    guesses += guess

    if guess not in word:
        attempts -= 1
        print("Wrong!")
        print(f"You have {attempts} more guesses.")

    if attempts == 0:
        print("You lost! The word was:", word)
