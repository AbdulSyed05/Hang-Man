import os
import random

from hangman_words import word_list
from hangman_art import stages, logo


def main_menu():
    """
    Displays the main menu and returns the user's choice.
    """
    clear()
    print(logo)
    print("Welcome to Hangman Game!")
    print("\nMain Menu:")
    print("1. Start a New Game")
    print("2. Game Description")
    print("3. Exit")
    while True:
        choice = input("Enter your choice (1/2/3): ")
        try:
            choice = int(choice)
            if choice > 3 or choice < 1:
                print("Invalid input! Enter your choice (1/2/3): ")
                continue
        except ValueError:
            print("Invalid input! Enter your choice (1/2/3): ")
            continue
        return choice


def game_description():
    """
    Displays the game description.
    """
    clear()
    print(logo)
    print("\nHangman is a word-guessing game where you have"
          " to guess a hidden word letter by letter.")
    print("You can make a limited number of incorrect guesses"
          " before the hangman is complete.")
    print("Your goal is to guess the word before the hangman is fully drawn.")
    print("Good luck!\n")
    input("Press ENTER to continue")


def clear():
    """
    Clears the terminal to prevent clutter.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def display_stage(lives, guesses, message):
    """
    Displays the current stage of the hangman game.
    """
    clear()
    print(stages[lives])
    print(f"{' '.join(guesses)}")
    print(message)
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 0:
            print("Guess cannot be empty")
        elif len(guess) > 1:
            print("Guess should not be more than one character!")
        elif not guess.isalpha():
            print("Guess should be a letter")
        else:
            return guess


def main():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    menu_choice = main_menu()
    if menu_choice == 3:
        end_of_game = True
        print("Goodbye!")
        return
    elif menu_choice == 2:
        game_description()
        main()
    else:
        display = ["_" for _ in range(word_length)]
        current_guesses = []
        current_message = ''
        while not end_of_game:
            guess = display_stage(lives, display, current_message)

            if guess in current_guesses:
                current_message = f"You've already guessed {guess}"
            elif guess not in chosen_word:
                lives -= 1
                current_message = f"You guessed {guess}"
                "that's not in the word.You lose a life."
                if lives == 0:
                    end_of_game = True
                    clear()
                    print(stages[lives])
                    print("You are out of lives!")
                    print(f"The word was: {chosen_word}.")
                    print("You lose. Good luck next time!")
            else:
                for position in range(word_length):
                    letter = chosen_word[position]
                    if letter == guess:
                        current_message = "Correct guess!"
                        display[position] = letter
            current_guesses.append(guess)
            if "_" not in display:
                end_of_game = True
                clear()
                print(stages[lives])
                print("You got it!")
                print(f"The word was: {chosen_word}.")
                print("You win! Great job!")

        while True:
            play_again = input("Do you want to play again? Y or N: ").lower()
            if play_again not in ["y", "n"]:
                print("Invalid input!")
            elif play_again == 'y':
                main()
            else:
                print("Thank you for playing Hangman. Goodbye!")
                return


main()
