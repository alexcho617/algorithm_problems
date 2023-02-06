#https://www.acmicpc.net/problem/1874
import sys
input = sys.stdin.readline

n = int(input())
ans = []
stack = [0]

curr = 0

for _ in range(n):
    num = int(input())
    while True:
        

        #increase add to stack
        if stack and stack[-1] < num:
            curr += 1
            stack.append(curr)
            ans.append("+")

        if stack and stack[-1] == num:
            stack.pop()
            ans.append("-")
            break
        #cannot proceed
        elif stack and stack[-1] > num:
            print("NO")
            quit()
    
    
    # print(stack)
    # print(ans)

print(*ans, sep='\n')