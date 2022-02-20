import random
from gameplay.util import *

class AutoSolver():
    def __init__(self, solution, algorithm_name, wordlist):
        self.guessNum = 0
        self.maxGuesses = 5
        self.guess_algorithm = self.getAlgorithm(algorithm_name)
        self.guesses = []
        self.solution = solution
        self.words = self.parseWordlist(wordlist)

    #sets algorithm function based on supplies algorithm name
    def getAlgorithm(self, algorithm_name):
        if algorithm_name == 'random': return self.guess_random
        return None

    #solves Wordle using the supplied algorithm, pretty-printing steps and results to stdout
    def solveToStdOut(self):
        while len(self.guesses) <= 5:
            guessInput = self.guess_algorithm()
            guessAsList = evaluatedGuess(guessInput, self.solution)
            formattedGuess = formatGuessToColor(guessAsList)
            sys.stdout.write("\n\033[F")
            print(formattedGuess)
            self.guesses.append(guessAsList)
            if guessIsCorrect(guessAsList, self.solution):
                print("\n\n\033[37m" + "solved in " + str(len(self.guesses)) + "/6 attempts.")
                break
        print("\033[37m\n" + "The word was" + "\033[92m " + self.solution)

    #parses given wordlist into a list of words
    def parseWordlist(self, wordlist):
        with open(wordlist) as wl:
            words = wl.read().split()
        return words

    #true random guessing algorithm; just chooses a random word from wordlist for each guess, without learning.
    def guess_random(self):
        guess = random.choice(self.words)
        return guess
