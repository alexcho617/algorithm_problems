#https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**6)



def recursion(start,end):
    if start > end:
        return
    mid = end + 1 #to handle when all children are smaller than root,
    for i in range(start+1, end +1):
        if tree[start] < tree[i]:
            mid = i
            break
    recursion(start + 1, mid - 1) #left side
    recursion(mid, end) #right side
    print(tree[start]) #print node

tree = []
while True:
    try: tree.append(int(sys.stdin.readline().strip()))
    except:
        break
recursion(0,len(tree) - 1)
