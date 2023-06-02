import itertools
def solution(word):
    alphabet = "AEIOU"
    wordPool = []
    wordDict = []
    for i in range(1,6):
        wordPool += list(itertools.product(alphabet,repeat = i))
    for wordItem in wordPool:
        temp = ""
        for character in wordItem:
            temp += character
        wordDict.append(temp)
    
    wordDict.sort()
    temp = ""
    for w in word:
        temp += w
    return wordDict.index(temp) + 1
