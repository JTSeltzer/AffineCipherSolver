# This is my solution to this daily programmer challenge -
# https://www.reddit.com/r/dailyprogrammer/comments/6k123x/20170629_challenge_321_intermediate_affine_cipher/

import sys

# take a word, and values for a and b and apply the following rule: Out = a * In + b, where 
# In is a character converted to number (a = 0, b = 1, c = 2, etc), and out is the character after
# performing the operation. Returns the word with all characters adjusted
def singleWordAffine(word, a, b):
  asciiWord = [(((a * (ord(letter) - 97)) + b) % 26) for letter in word.lower()]
  outputWord = [chr(number + 97) for number in asciiWord]
  return ''.join(outputWord)

def recursiveSearch(wordList, aVals, bVals):
  
  # if there are no words left in the wordlist, return the a and b values
  if (len(wordList) <= 0):
    return aVals, bVals
  
  aList = []
  bList = []
  
  # if this is the first time the recursiveSearch function has been called, iterate over
  # every possible combination of a and b values.
  if (len(wordList) == len(sys.argv)):
    for i in range(0, len(aVals)):
      for j in range(0, len(bVals)):
        
        # if the current longest word in the wordlist, and the a and b values decode to a word
        # in the dictionary of words (lines), append the a and b values to a new list
        if (singleWordAffine(wordList[0], aVals[i], bVals[j]) in lines):
          aList.append(aVals[i])
          bList.append(bVals[j])
  
  # if this is not the first time the recursiveSearch function has been called, then there should
  # be pairs of a and b values. Cycle through each pair.
  else:
    for i in range(0, len(aVals)):
    
      # if the current longest word in the wordlist, and the a and b values decode to a word
      # in the dictionary of words (lines), append the a and b values to a new list
      if (singleWordAffine(wordList[0], aVals[i], bVals[i]) in lines):
        aList.append(aVals[i])
        bList.append(bVals[i])
  
  # if either aList or bList contain more than one number, and neither is empty, call
  # recursiveSearch again with the next longest word, and the new a and b pairs
  if ((len(aList) * len(bList)) > 1):
    wordList.pop(0)
    aList, bList = recursiveSearch(wordList, aList, bList)
    
  return aList, bList

# if no argument is given, instruct on use
if (len(sys.argv) < 2):
  print "To use, enter a message to attempt to decrypt as an argument."
  sys.exit()

# Pop the first argument (the program), and then combine all other arguments to form a single string
sys.argv.pop(0)

# create a string from all of the arguments
cipherInput = ' '.join(sys.argv)

# sort the words of the input string by length
sortedWords = sorted(sys.argv, key = len, reverse = True)

# read in the file of words
with open('/home/boz/Documents/python/DailyProgrammer/AffineCipherSolver/enable1.txt') as f:
  lines = f.read().splitlines()

aList = range(1, 27)
bList = range(1, 27)

aList, bList = recursiveSearch(sortedWords, aList, bList)

for i in range (0, len(aList)):
  print ' '.join([singleWordAffine(word, aList[i], bList[i]) for word in cipherInput.split(" ")])
