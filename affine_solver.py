# This is my solution to this daily programmer challenge -
# https://www.reddit.com/r/dailyprogrammer/comments/6k123x/20170629_challenge_321_intermediate_affine_cipher/

# take a word, and values for a and b and apply the following rule: Out = a * In + b, where 
# In is a character converted to number (a = 0, b = 1, c = 2, etc), and out is the character after
# performing the operation. Returns the word with all characters adjusted
def singleWordAffine(word, a, b):
  asciiWord = [(((a * (ord(letter) - 97)) + b) % 26) for letter in word.lower()]
  outputWord = [chr(number + 97) for number in asciiWord]
  return ''.join(outputWord)

# test cases -> move these to new directory later
input1 = "NLWC WC M NECN"
output1 = "this is a test"

input2 = "YEQ LKCV BDK XCGK EZ BDK UEXLVM QPLQGWSKMB"
output2 = "you lead the race of the worlds unluckiest"

input2B = "Yeq lkcv bdk xcgk ez bdk uexlv'm qplqgwskmb."
output2B = "You lead the race of the world's unluckiest."

input3 = "NH WRTEQ TFWRX TGY T YEZVXH GJNMGRXX STPGX NH XRGXR TX QWZJDW ZK WRNUZFB P WTY YEJGB ZE RNSQPRY XZNR YJUU ZSPTQR QZ QWR YETPGX ZGR NPGJQR STXQ TGY URQWR VTEYX WTY XJGB"
output3 = "my heart aches and a drowsy numbness pains my sense as though of hemlock i had drunk or emptied some dull opiate to the drains one minute past and lethe wards had sunk"

input3B = "Nh wrteq tfwrx, tgy t yezvxh gjnmgrxx stpgx / Nh xrgxr, tx qwzjdw zk wrnuzfb p wty yejgb, / Ze rnsqpry xznr yjuu zsptqr qz qwr yetpgx / Zgr npgjqr stxq, tgy Urqwr-vteyx wty xjgb."
output3B = "My heart aches, and a drowsy numbness pains / My sense, as though of hemlock I had drunk, / Or emptied some dull opiate to the drains / One minute past, and Lethe-wards had sunk."

input4 = "ICH NPJTX MUZDS OZK QPLGB ZWHU ICH EFYR AZV"
output4 = "the quick brown fox jumps over the lazy dog"

aList = []
bList = []
# read in the file of words
with open('/home/boz/Documents/python/DailyProgrammer/AffineCipherSolver/enable1.txt') as f:
  lines = f.read().splitlines()

# sort the words of the input string by length
sortedWords = sorted(input1.split(" "), key = len, reverse = True)

for i in range(1, 27):
  for j in range(1, 27):
    if (singleWordAffine(sortedWords[0], i, j) in lines):
      aList.append(i)
      bList.append(j)
      print ' '.join([singleWordAffine(word, i, j) for word in input1.split(" ")])
      
if (len(aList) > 1):
  for i in range(0, len(aList)):
    if (singleWordAffine(sortedWords[1], aList[i], bList[i]) in lines):
      print ' '.join([singleWordAffine(word, aList[i], bList[i]) for word in input1.split(" ")])