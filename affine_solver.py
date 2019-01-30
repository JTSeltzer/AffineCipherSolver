# This is my solution to this daily programmer challenge -
# https://www.reddit.com/r/dailyprogrammer/comments/6k123x/20170629_challenge_321_intermediate_affine_cipher/

import sys

# Takes a word, and values for a and b and applys the following rule: y = a * x + b, where 
# x is a character converted to number (a = 0, b = 1, c = 2, etc), and y is the character after
# performing the operation. Returns the word with all characters adjusted
def singleWordAffine(word, a, b):
  asciiWord = [(((a * (ord(letter) - 97)) + b) % 26) for letter in word.lower()]
  outputWord = [chr(number + 97) for number in asciiWord]
  return ''.join(outputWord)

# Takes a list of words, preferably ordered from longest to shortest, and lists of the
# values of a and b to test. On the first run, all combinations of a and b are tested
# against the first word in the list using the singleWordAffine function, and comparing
# against the provided dictionary. If more than one possible output is found, the function
# is called again with the next word in the list. After the first run, only combinations
# of a and b that were found to work for the first word are considered. The function
# returns the a and b pairs either when there is only one working pair, or when there
# are no more words in the word list.
def recursiveSearch(wordList, aVals, bVals):
  
  # If there are no words left in the wordlist, or the longest word is 1 letter long,
  # return the a and b values
  if ((len(wordList) <= 0) or (len(wordList[0]) <= 1)):
    return aVals, bVals
  
  aList = []
  bList = []
  
  # If this is the first time the recursiveSearch function has been called, iterate over
  # every possible combination of a and b values.
  if (len(wordList) == len(sys.argv)):
    for i in range(0, len(aVals)):
      for j in range(0, len(bVals)):
        
        # If the current longest word in the wordlist, and the a and b values decode to a word
        # in the dictionary of words (lines), append the a and b values to a new list
        if (singleWordAffine(wordList[0], aVals[i], bVals[j]) in lines):
          aList.append(aVals[i])
          bList.append(bVals[j])
  
  # If this is not the first time the recursiveSearch function has been called, then there should
  # be pairs of a and b values. Cycle through each pair.
  else:
    for i in range(0, len(aVals)):
    
      # If the current longest word in the wordlist, and the a and b values decode to a word
      # in the dictionary of words (lines), append the a and b values to a new list
      if (singleWordAffine(wordList[0], aVals[i], bVals[i]) in lines):
        aList.append(aVals[i])
        bList.append(bVals[i])
  
  # If either aList or bList contain more than one number, and neither is empty, call
  # recursiveSearch again with the next longest word, and the new a and b pairs
  if ((len(aList) * len(bList)) > 1):
    wordList.pop(0)
    aList, bList = recursiveSearch(wordList, aList, bList)
    
  return aList, bList

# If no argument is given, instruct on use
if (len(sys.argv) < 2):
  print "To use, enter a message to attempt to decrypt as an argument."
  sys.exit()

# Pop the first argument (the program), and then combine all other arguments to form a single string
sys.argv.pop(0)

# Create a string from all of the arguments
cipherInput = ' '.join(sys.argv)

# Sort the words of the input string by length
sortedWords = sorted(sys.argv, key = len, reverse = True)

# Read in the file of words
with open('/home/boz/Documents/python/DailyProgrammer/AffineCipherSolver/enable1.txt') as f:
  lines = f.read().splitlines()

# Set the initial 
aList = range(1, 27)
bList = range(1, 27)

aList, bList = recursiveSearch(sortedWords, aList, bList)

# Print the possible decoded outputs
for i in range (0, len(aList)):
  print ' '.join([singleWordAffine(word, aList[i], bList[i]) for word in cipherInput.split(" ")])
