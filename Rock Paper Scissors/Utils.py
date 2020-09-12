def printHand(value):
    hands = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    return hands.get(value)


def evaluate(userInput, computerInput):
    if userInput == computerInput:
        return "It is a draw"
    elif userInput == 1 and computerInput == 2:
        return "You lose"
    elif userInput == 2 and computerInput == 3:
        return "You lose"
    elif userInput == 3 and computerInput == 1:
        return "You lose"
    else:
        return "You won"
