# Python program for word guessing game
"""import random
def choose():
    words = ["banana", "orange", "apple", "strawberry"]
    return random.choice(words)
def play(word , guess_letter):
    display = ""
    for letter in word:
        if letter in guess_letter:
            display +=letter
        else:
            display += "_"
  def game

"""
import random

def word_guessing_game():
    word_list = ["python", "programming", "developer", "keyboard", "computer"]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = ["_"] * word_length
    guessed_letters = []
    guesses_left = 6

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {word_length} letters: {' '.join(display)}")

    while "_" in display and guesses_left > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed {guess}. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            for i in range(word_length):
                if chosen_word[i] == guess:
                    display[i] = guess
            print("Correct!")
        else:
            guesses_left -= 1
            print(f"Wrong! You have {guesses_left} guesses left.")

        print(f"{' '.join(display)}")

    if "_" not in display:
        print("Congratulations! You guessed the word.")
    else:
        print(f"Sorry, you ran out of guesses. The word was {chosen_word}.")

word_guessing_game()
