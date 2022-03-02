#HANGMAN
#Import the required modules
import random
import hangman_art
import hangman_words

from replit import clear #function

#Define the variables and functions
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
users_guesses = []

#Import the logo from hangman_art.py and print it
print(hangman_art.logo + "\n")

#Testing code
#print(f'Pssst, the solution is {chosen_word}.\n')

#Create blanks for each letter in the chosen_word
display = []
for each in range(0, word_length):
    display += "_"

#Join elements in the list for better readability
print(f"{' '.join(display)}")

#Run the game...
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    clear()
    
    #Check guessed letter.
    #If the user has already guessed the letter...
    if guess in display:
        print(f"You've already guessed '{guess}'. Try again.")

    #If guess is correct, replace "_" with letter
    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    #If the guess is wrong, lose a life
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}'. That's not in the word.\nYou lose a life.")


    #Print out updated 'display' after every guess
    print(f"{' '.join(display)}")

    #Import the hangman ASCII art corresponding to
    #each stage, after each guess
    print(hangman_art.stages[lives])
    
    #Display the user's guesses
    users_guesses += guess
    print(f"You've guessed: {', '.join(users_guesses)}")
    
    #Check if the user has gotten all the letters
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")
    if lives == 0:
        end_of_game = True
        print(f"\nYou lose. The word was '{chosen_word}'.")
