#https://www.acmicpc.net/problem/1316
#그룹 단어 체커
def groupCheck(word):
    isGroupcheck = True
    n = len(word)
    prev = word [0]
    curr = word[0]
    firstEncounter = []
    for i in range(n):
        curr = word[i]
        #not in the list
        if curr not in firstEncounter:
            firstEncounter.append(curr)
        #already in the list but its not the same as previous
        elif curr in firstEncounter and curr != prev:
            isGroupcheck = False
        prev = curr
    return isGroupcheck


n = int(input())
count = 0
for _ in range(n):
    if(groupCheck(input()) == True):
        count += 1
print(count)