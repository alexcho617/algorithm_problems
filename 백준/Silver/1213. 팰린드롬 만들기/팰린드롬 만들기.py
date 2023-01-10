#https://www.acmicpc.net/problem/1213
engName = list(input())
dict = {}
engName.sort()
isMoreThanOneOdd = False
for e in engName:
    if e in dict:
        dict[e] += 1
    else:
        dict[e] = 1
# print(dict)
pelindrom = ''
sorry = "I'm Sorry Hansoo"
#filter impossibles
oddCount = 0
for i in dict.values():
    if i % 2 != 0:
        oddCount += 1
        if oddCount > 1:
            print(sorry)
            quit()
#make pelindrom
#get odd one in the middle
for key,value in dict.items():
    if value % 2 == 1:
        pelindrom = key
        dict[key] -= 1
# print(dict)
wordPool = sorted(dict, reverse=True) #get all the keys in reverse order
# print(wordPool)
# print(pelindrom)
#make pelindrom around it alphabetically
for word in wordPool:
    while dict[word] != 0:
        pelindrom = word + pelindrom #front
        dict[word] -= 1
        pelindrom = pelindrom + word #back
        dict[word] -= 1
print(pelindrom)