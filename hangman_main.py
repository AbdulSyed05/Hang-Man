
import os
import random

from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

def clear():
    """
    This clears the terminal to prevent clutter on it.
    """
    os.system('cls' if os.name=='nt' else 'clear')


def display_stage(lives, guesses, message):
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




    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    print(logo)

    #Testing code
    # print(f'Pssst, the solution is {chosen_word}.')

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"
        
    current_guesses = []
    current_message = ''
    
    while not end_of_game:
        # display_stage(lives, display, '')
        # guess = input("Guess a letter: ").lower()
        guess = display_stage(lives, display, current_message)

        if guess in current_guesses:
            # display_stage(lives, display, f"You've already guessed {guess}")
            current_message = f"You've already guessed {guess}"
        elif guess not in chosen_word:
            # print(f"You guessed {guess}, that's not in the word. You lose a life.")

            lives -= 1
            # display_stage(lives, display, f"You guessed {guess}, that's not in the word. You lose a life.")
            current_message = f"You guessed {guess}, that's not in the word. You lose a life."
            if lives == 0:
                end_of_game = True
                # display_stage(lives, display, "You lose.")
                # current_message = "You lose!"
                print("You lose.")
        else:

            #Check guessed letter
            for position in range(word_length):
                letter = chosen_word[position]
                #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                if letter == guess:
                    # print("GUESS CORRECT!")
                    current_message = "Correct guess!"
                    display[position] = letter

        current_guesses.append(guess)
        #Check if user is wrong.
        

        #Join all the elements in the list and turn it into a String.
        # print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            # display_stage(lives, display, "You win.")
            # current_message = "You win!"
            print("You win.")


    while True:
        play_again = input("Do you want to play again? Y or N: ").lower()
        if play_again not in ["y", "n"]:
            print("Invalid input!")
        elif play_again == 'y':
            main()
        else:
            print("Thanks for playing! Bye!")
            break

        # print(stages[lives])
        # display_stage(lives, display, '')

main()

