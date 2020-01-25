import math
def loadWords():
    file = open('p098_words.txt')
    stream = file.read()
    stream = stream.replace('\"', '')
    return stream.split(',')

def anagram(w1, w2):
    if len(w1) != len(w2):
        return False

    s1 = {}
    for char in w1:
        s1[char] = s1.get(char, 0) + 1
    s2 = {}
    for char in w2:
        s2[char] = s2.get(char, 0) + 1

    return s1 == s2

def findAnagrams(words):
    pairs = set()
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j or ((words[j], words[i]) in pairs):
                continue
            if anagram(words[i], words[j]):
                pairs.add((words[i], words[j]))
        print(i)
    return pairs

def loadSquares(maxLen):
    squares = list()
    for i in range(1, math.ceil(10**(maxLen/2))):
        squares.append(str(i**2))
    return squares

words = loadWords()
bestLen = 0
bestWord = None
i = 0
for word in words:
    if bestLen < len(word):
        bestLen = len(word)
        bestWord = word
    i += 1

wordPairs = findAnagrams(words)

bestLen = 0
for pair in wordPairs:
    bestLen = max(len(pair[0]), bestLen)
print(bestLen)

squares = loadSquares(bestLen)
print(len(squares))
print(findAnagrams(squares))
