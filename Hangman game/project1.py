# TASK 1: Hangman Game

import random

lives = 6
word_list = ["Effective","manifesting","voilent"]
choosen_word = random.choice(word_list).lower()
print(choosen_word)

placeholder = ""
word_length =len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False

correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letter:
        print("you've already guessed " +str(guess))

    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letter:
                correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_" 

    print(display)

    if guess not in choosen_word:
        lives -= 1
        print("Wrong guess! " + guess + " is not in the word.")
        print("You have " + str(lives) + "lives left.")
        if lives == 0:
            game_over = True
            print("you lose.")


    if "_" not in display:
        game_over = True
        print("You win!")