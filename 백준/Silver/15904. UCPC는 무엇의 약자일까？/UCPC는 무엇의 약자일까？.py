#https://www.acmicpc.net/problem/15904
love = "I love UCPC"
hate = "I hate UCPC"

word = input()
ucpc = "UCPC"
i = 0
for w in word:
    if w == ucpc[i]:
        i += 1
    if i == 4:
        print(love)
        quit()
print(hate)