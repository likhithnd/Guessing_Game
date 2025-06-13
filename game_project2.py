import random
compGuess = random.randint(1,100)
def userguess():
    userGuess = int(input("entre any number b/w 1-100: "))
    return userGuess
x = userguess()
y = 1
while compGuess != x:
    if compGuess > x:
        print("big number please")
    elif compGuess < x:
        print("less number please")
    x = userguess()
    y += 1
print(f"the guess is correct.the number is {compGuess}. You took {y} chances to guess")
