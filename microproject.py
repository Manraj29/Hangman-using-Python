import word

def instructions():
    print("\n**Instructions:**\n")
    print("You have 5 chances to guess the complete word")
    print("If you guess the word, you win")
    print("If you didn't guess the word, you lose")
    print("If you guess the wrong letter, you lose one chance")
    print("You can enter only alphabetical characters")
    print("It is just a simple game, Don't take it seriously")
    print("Save the Hangman!!!!\n")
    print("\n**Enjoy!**\n")


def draw(turns):
    if turns == 4:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif turns == 3:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif turns == 2:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |      \n"
              "__|__\n")
    elif turns == 1:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |     \n"
              "__|__\n")
    elif turns == 0:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n"
              "Hanged, you were not able to save the Hangman!!!\n")



playagain = True
while playagain:
    name = input("Enter your name: ")
    turns = 5
    guesses = ''
    print("Hello ", name)
    print("\n**********Welcome to the game**********\n")
    print("Guess the word || Hangman")
    words = word.get_word()
    instructions()
    while turns > 0:
        failed = 0
        for char in words:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        if failed == 0:
            # print("\nYou Win!!!!")
            print()
            print("\/ _       |    |o.__ ||\n"
                  "/ (_)|__|   \/\/ ||  |oo ")
            print("The word is: ", words)
            print("   O \n"
                "  /|\ \n"
                "  / \ \n"
                "\n Safe to go home!!!")
            break   
        print()
    
        guess = input("guess a character:")
        if(len(guess) != 1):
            print("You can only enter one character")
            continue
        guesses += guess
        if guess not in words:
            turns -= 1
            # print("Wrong")
            draw(turns)
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("\/ _      | _   _  _  ||\n"
                      "/ (_)|_|  |(_) _\ }_  oo")
                print("The word is: ", words)
                print("Game Over!")
    print("Do you want to play again (y/n)?")
    play_again = input()
    if play_again == 'y':
        playagain = True
    elif play_again == 'n':
        playagain = False
    else:
        print("Invalid input")
        playagain = False
else:
	print("Thank you for playing")
