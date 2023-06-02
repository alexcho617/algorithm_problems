#https://www.acmicpc.net/problem/1439
str = input()
first = str[0]
other = ''
ans = 0
compressed = ''

if first == '0':
    other = '1'
else:
    other = '0'
prev = str[0]
compressed = prev
for i in range(1,len(str)):
    curr = str[i]
    if curr != prev:
        compressed+=curr
        prev = curr
print(compressed.count(other))
