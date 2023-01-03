# https://www.acmicpc.net/problem/25501
ans = []
def recursion(s, l, r,count):
    
    if l >= r:
        ans.append([1,count]) # palindrome
    elif s[l] != s[r]:
        ans.append([0,count]) # not palindrom
    else:
        return recursion(s, l+1, r-1,count + 1)

def isPalindrom(s):
    return recursion(s, 0, len(s)-1,1)

n = int(input())
for _ in range(n):
    isPalindrom(input())
for a in ans:
    print(*a)