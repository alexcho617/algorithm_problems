#https://www.acmicpc.net/problem/1406
import sys
input = sys.stdin.readline

sentence = input().rstrip()
n = int(input())
left = list(sentence)
right = []

for _ in range(n):
    str = input().rstrip()
    match str:
        case 'L':
            if left:
                right.append(left.pop())
        case 'D':
            if right:
                left.append(right.pop())
        case 'B':
            if left:
                left.pop()
        case default:
            c = str.split()[1]
            left.append(c)
print(*left,*right[::-1],sep="")