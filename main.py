import random

minNum = 1
maxNum = 100
numToGuess = random.randint(minNum, maxNum)
userTries = 0

while True:
    userGuess = int(input(f"Please guess a number from {minNum} - {maxNum} \n"))
    if userGuess < numToGuess:
        userTries += 1
        print("Too low \n")
        minNum = userGuess
    elif userGuess > numToGuess:
        userTries += 1
        print("Too high \n")
        maxNum = userGuess
    else:
        userTries += 1
        print(f"Congrats {userGuess} was the correct number and it took {userTries} tries\n")
        break
