import Utils
import random

print("Welcome to Rock-Paper-Scissors game!!\n")
print("Rock - 1\nPaper - 2\nScissors - 3\nQuit Game - 4")


def playGame():
    userInput = int(input("\nEnter your choice: "))

    if userInput not in [1, 2, 3, 4]:
        print("\nWrong value entered! Exiting the application :(")
    elif userInput == 4:
        print("\nThanks for playing :)")
        quit(0)
    else:
        print("You selected ", Utils.printHand(userInput))

    computerInput = random.randint(1, 3)
    print("\nComputer selected ", Utils.printHand(computerInput))
    print(Utils.evaluate(userInput, computerInput))


playGame()
