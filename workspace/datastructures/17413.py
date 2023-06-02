#https://www.acmicpc.net/problem/17413
import sys
input = sys.stdin.readline
ans = []
left = []
right = []
tags = []
# string = input()
string = '<open>tag hello<close>'

for i in range(len(string)):
    if string[i] == '<':
        left.append(i)
    elif string[i] == '>':
        right.append(i+1)

#remove all tags
for i in range(len(left)):
    tag = string[left[i]:right[i]]
    tags.append(tag)
for tag in tags:
    string = string.replace(tag,'')

#
print('--')
print(string)
print(tags)