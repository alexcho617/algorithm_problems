#https://www.acmicpc.net/problem/10799

brackets = input()
ans = 0
stack = 0
for i in range(len(brackets)-1):
    curr = brackets[i]
    next = brackets[i+1]
    if curr == '(':
        if next == '(':
            stack += 1
        else:
            #laser
            ans += stack 
    #')'
    else:
        #end of wood
        if next == ')':
            ans += 1
            stack -=1
print(ans)