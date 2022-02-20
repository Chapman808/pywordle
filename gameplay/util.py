import random
import sys

#for a given guess and solution, add prefixed to each letter in the guess to indicate matches. '*' for pure match, '+' for partial match, and '_' for no match
def evaluatedGuess(guessInput, solution):
    letterList = [str(char) for char in guessInput]
    matched = set()
    for i, letter in enumerate(letterList):
        if letter in matched: 
            letterList[i] = '_' + letter
        elif letter == solution[i]: 
            letterList[i] = '*' + letter
            matched.add(letter)
        elif letter in set(solution): 
            letterList[i] = '+' + letter
            matched.add(letter)
        else: letterList[i] = "_" + letter
    return letterList

def receiveGuess():
    print("\033[37m", end="\r")
    guess = input()
    while not validate_input(guess):
        sys.stdout.write("\033[F" + (" " * len(guess)) + "\n\033[F")
        guess = input()
    return guess

def validate_input(inp):
    if len(inp) != 5:
        return False
    for char in inp:
        if ord(char) < 97 or ord(char) > 122: return False
    return True

def formatGuessToColor(guessAsList):
    formatted = [letter.replace('*', '\033[92m').replace('+', '\033[93m').replace('_', '\033[37m') for letter in guessAsList]
    return ''.join(formatted)

def guessIsCorrect(guessAsList, target):
    guessString = "".join(guessAsList).replace("_", "").replace("+", "").replace("*", "")
    return guessString == target

def getRandomWord():
    with open("sgb-words.txt") as words:
        return random.choice(words.read().split())