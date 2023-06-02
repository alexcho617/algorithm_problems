#https://www.acmicpc.net/problem/2941
#크로아티아 알파벳

#input
word = input()
croatiaWords = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0

for croatia in croatiaWords:
    if croatia in word:
        count += word.count(croatia)
        word = word.replace(croatia, '*')
        #Error from replacing it with blank space
#output
#count of croatia words
print(len(word))
