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

# if no argument is given, instruct on use
if (len(sys.argv) < 2):
  print "To use, enter a message to attempt to decrypt as an argument."
  sys.exit()

# Pop the first argument (the program), and then combine all other arguments to form a single string
sys.argv.pop(0)
cipherInput = ' '.join(sys.argv)

# sort the words of the input string by length
sortedWords = sorted(cipherInput.split(" "), key = len, reverse = True)

aList = []
bList = []

# read in the file of words
with open('/home/boz/Documents/python/DailyProgrammer/AffineCipherSolver/enable1.txt') as f:
  lines = f.read().splitlines()

for i in range(1, 27):
  for j in range(1, 27):
    if (singleWordAffine(sortedWords[0], i, j) in lines):
      aList.append(i)
      bList.append(j)
      print (i, j, ' '.join([singleWordAffine(word, i, j) for word in cipherInput.split(" ")]))