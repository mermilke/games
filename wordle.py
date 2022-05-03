import random
from WordleAssistant import *

def wordOK(word):
   return len(word) == 5 and len(word) == len(set(word)) and word[-1] != 's'

def BinarySearch ( lst , key ):
   """ Search for key in sorted list lst . """
   low = 0
   high = len ( lst ) - 1
   while ( high >= low ):
      mid = ( low + high ) // 2
      if key < lst [ mid ]:
         high = mid - 1
      elif key == lst [ mid ]:
         return mid
      else:
         low = mid + 1
   return (- low - 1)


def playWordle( answer = None ):

   print('''\nWelcome to WORDLE, the popular word game. The goal is to guess a
five letter word chosen at random from our wordlist. None of the
words on the wordlist have any duplicate letters.

You will be allowed 6 guesses. Guesses must be from the allowed
wordlist. We'll tell you if they're not.

Each letter in your guess will be marked as follows:

   x means that the letter does not appear in the answer
   ^ means that the letter is correct and in the correct location
   + means that the letter is correct, but in the wrong location

Good luck!\n''')

   filename = None
   while filename == None:
      filename = input("Enter the name of the file from which to extract the wordlist: ") + ".txt"
      try:
         wordlist = createWordlist(filename)[0]
      except:
         print("File does not exist. Try again!")
         filename = None

   if answer == None:
      validWord = random.choice(wordlist)
      while not wordOK(validWord):
         validWord = random.choice(wordlist)
   else:
      validWordKey = BinarySearch(wordlist, answer.lower())
      validWord = wordlist[validWordKey].lower()
      if validWordKey < 0:
         print("Answer supplied is not legal.\n")
         return 
   
   for guess in range(6):
      test = -1
      while test < 0:
         wordGuessed = input(f"Enter your guess ({guess+1}): ").lower()
         test = BinarySearch(wordlist, wordGuessed)
         if test < 0:
            print("Guess must be a 5-letter word in the wordlist. Try again!")

      outputChars = []
      for charIndex, char in enumerate(wordGuessed):
         if validWord[charIndex] == char:
            outputChars.append("^")
         elif char in validWord:
            outputChars.append("+")
         else:
            outputChars.append("x")
      print( "  ".join(wordGuessed.upper()))
      print( "  ".join(outputChars))
      if outputChars == ['^','^','^','^','^'] and guess <= 5:
         print("CONGRATULATIONS! You win!\n")
         break
      elif guess == 5:
         print("Sorry! The word was " + validWord + ". Better luck next time!\n") 

playWordle()