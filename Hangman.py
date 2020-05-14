#!/usr/bin/python3

"""This program plays a game of HangMan with alternate difficulty for the words to guess. Created by myself."""


import sys
import random

def main():

    print("\n\nWelcome to Hangman!\nPlease choose the level of difficulty:\n1) Easy (3-4 letters)\n2) Medium (5-6 letters)\n 3) Hard (7+ letters)\n")
    answer = input("Choice: ")

    while True:
        if answer not in "123":
            print("Invalid Option, please choose again\n")
            answer = input("Choice: ")
        else:
            break

    Easy = ["cat","dog","cab","ape","cup","bone","love","sad","game", "word"]
    Medium = ["phone","friend","Hippo","choice","london","spain","python","snake","league","legend"]
    Hard = ["television","computer","question","difficulty","graphics","detroit","hangman","wardrobe","monitor","hospital"]
    if answer == "1":
        word = Easy[random.randrange(11)].upper()
    elif answer == "2":
        word = Medium[random.randrange(11)].upper()
    else:
       word = Hard[random.randrange(11)].upper()
    
    print("-" * 40)

    Body = [
        """
        _______
        |     |
        |     
        |
        |
        |
        |__
        """,
        """
        _______
        |     |
        |     0
        |
        |
        |
        |__
        """,
        """
        _______
        |     |
        |     0
        |     |
        |
        |
        |__
        """,
        """
        _______
        |     |
        |     0
        |     |
        |    /
        |
        |__
        """,
        """
        _______
        |     |
        |     0
        |     |
        |    //
        |
        |__
        """,
        """
        _______
        |     |
        |     0
        |    /|
        |    //
        |
        |__
        """,
        """
        _______
        |     |
        |     0
        |    /|/
        |    //
        |
        |__
        """,
    ]
    count = 0
    buzzer = False
    guess = "_" * len(word)
    while count < 6:
        print(Body[count])
        print(guess)
        letter_guess = input().upper()
        if letter_guess in word:
            (letter_guess, "Is in the word.")
            index = [i for i in range(len(word)) if letter_guess == word[i].upper()]
            guess_list = list(guess)
            for i in index:
                guess_list[i] = letter_guess
                guess = "".join(guess_list)
            if guess == word:
                buzzer = True
                break
        else:
            print("Not in the word, the word was: ", word)
            count += 1
    if buzzer is True:
        answer = input("Congratz you won the game !!!\n Would you like to play again ? (Y/N)")
        if answer.upper() == "Y":
            main()
        else:
            print("Thanks for playing!")
    else:
        print(Body[6])
        answer = input("Better luck next time !!!\n Would you like to play again ? (Y/N)")
        if answer.upper() == "Y":
            main()
        else:
            print("Thanks for playing!")

if __name__ == '__main__':
    main()
