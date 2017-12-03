import random

def main():
    welcome = ['Welcome to Baffoe! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!'
               ]

    for line in welcome:
        print(line)

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "ispace", "osborn", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None # will hold the players guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        joined_word = None # joins the words in the list word_guessed

        BAFFOE = (
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

        print(BAFFOE[0])
        attempts = (10) 


        while (attempts != 0 and "-" in word_guessed):
            print(("You have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("Please select a letter between A-Z" + "\n> "))
            except: # check valid input
                print("Invalid try again")
                               
            else: 
                if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
                    print("That is not a letter. Please try again.")
                    
                elif len(player_guess) > 1: # check the input is only one letter
                    print("That is more than one letter. Please try again.")
                    
                elif player_guess in guessed_letters: # check it letter hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(BAFFOE[(len(BAFFOE) - 1) - attempts])

        if "-" not in word_guessed: # no blanks remaining
            print(("Congratulations! {} was the word").format(chosen_word))
        else: # loop must have ended because attempts reached 0
            print(("Sorry! The word was {}.").format(chosen_word))

        print("Would you like to play again?")

        response = input("> ").lower()
        if response not in ("yes"):
            play_again = False
        else:
            response is ("no")
            print("to exit")
            
if __name__ == "__main__":
    main()

