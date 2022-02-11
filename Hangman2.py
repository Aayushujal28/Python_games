import random
import time

print("________Welcome to the game Guess the word by Aayush ujal!________")
name = input("Enter your name:")
print("________Hello "+name+" welcome to game________")
print("Game is about to start!")
time.sleep(1)

def main():
    global length
    global word1, word2
    global display
    global count
    global an, animal
    word_guess = ["Animals", "Months", "Plants", "Fruits", "vehicles"]
    word1 = random.choice(word_guess)
    hint()


def hint():
    global length
    global display
    if(word1 == "Animals"):

        print("Hint:it is a animal ")
        Animal()

    elif(word1 == "Months"):

        print("Hint:it is a month")
        Months()

    elif(word1 == "Plants"):

        print("Hint:it is a plant")
        Plants()

    elif(word1 == "Fruits"):

        print("Hint:it is a fruit")
        Fruits()

    else:

        print("Hint:it is a vehicles")
        Vehicles()

    play_game()


def Animal():
    global length
    global display
    global ani
    global word
    ani = ["dog", "cat", "cow", "deer", "bear"]
    length = random.choice(ani)
    length = len(word)
    display = "_"*length
    print(display + " Guess the word!")


def Months():
    global length
    global display
    global mon
    global word
    mon = ["january", "august", "july", "june", "september", "november"]
    word = random.choice(mon)
    length = len(word)
    display = "_"*length
    print(display + " Guess the word!")


def Plants():
    global length
    global display
    global pl
    global word
    pl = ["lily", "sunflower", "neem", "money"]
    word = random.choice(pl)
    length = len(word)
    display = "_"*length
    print(display + " Guess the word!")


def Fruits():
    global length
    global display
    global frui
    global word
    frui = ["apple", "banana", "watermelon", "orange", "pear"]
    word = random.choice(frui)
    length = len(word)
    display = "_"*length
    print(display + " Guess the word!")


def Vehicles():
    global length
    global display
    global veh
    global word
    veh = ["car", "bus", "cycle", "scooter", "truck"]
    word = random.choice(veh)
    length = len(word)
    display = "_"*length
    print(display + " Guess the word!")


def play_game():
    global word
    guess = input("Enter the word:")
    if(word == guess):

        print("YOU GUESSED THE CORRECT WORD!\n")
        play_again()

    else:
        {
            hangman()
        }


def hangman():
    print("   _____ \n"
          "  |     | \n"
          "  |     |\n"
          "  |     | \n"
          "  |     O \n"
          "  |    /|\ \n"
          "  |    / \ \n"
          "__|__\n")
    print("Wrong guess. You are hanged!!!\n")
    play_again()


def play_again():
    global note
    note = input("You want to play again say y or n\n")
    if(note == "y" or note == "Y"):
        {
            main()
        }
    else:
        {
            print("Better luck next time!")
        }


main()
