from ast import arg
import sys
from gameplay.util import *
import argparse

def play():
    print("welcome to pyWORDLE! enter guesses below (lower case):")
    solution = getRandomWord()
    guesses = []
    while len(guesses) <= 5:
        guessInput = receiveGuess()
        guessAsList = evaluatedGuess(guessInput, solution)
        formattedGuess = formatGuessToColor(guessAsList)
        sys.stdout.write("\033[F")
        print(formattedGuess)
        guesses.append(guessAsList)
        if guessIsCorrect(guessAsList, solution):
            print("\n\n\033[37m" + "solved in " + str(len(guesses)) + "/6 attempts.")
            break
    print("\033[37m\n" + "The word was" + "\033[92m " + solution)

with open('sgb-words.txt') as wordlist:
    words = wordlist.read().split()
    
def autosolve(solution, algorithm):
    if not solution: solution = getRandomWord()
    if not validate_input(solution):
        print("invalid word to solve: " + solution)
        return
    guesses = []
    while len(guesses) <= 5:
        guessInput = generateGuess(algorithm)
        guessAsList = evaluatedGuess(guessInput, solution)
        formattedGuess = formatGuessToColor(guessAsList)
        sys.stdout.write("\n\033[F")
        print(formattedGuess)
        guesses.append(guessAsList)
        if guessIsCorrect(guessAsList, solution):
            print("\n\n\033[37m" + "solved in " + str(len(guesses)) + "/6 attempts.")
            break
    print("\033[37m\n" + "The word was" + "\033[92m " + solution)

def generateGuess(algorithm):
    def _random():
        return random.choice(words)
    if algorithm == 'random':
        return _random()
    print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, help="Action to perform: either 'play' or 'solve'", default='play')
    parser.add_argument('-w', type=str, help="five letter word for solve tool", default=None)
    parser.add_argument('--algorithm', type=str, help="autosolver algorithm", default='random')
    args = parser.parse_args()
    action = args.a
    word = args.w
    if action == 'play':
        play()
    elif action == 'solve': 
        autosolve(word, args.algorithm)