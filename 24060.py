# https://www.acmicpc.net/problem/24060
import sys
input = sys.stdin.readline
count = 0
def merge(p:int,q:int,r:int):
    global a
    global k
    global count
    i = p
    j = q+1
    tmp = []
    
    #both left and right side remain
    while i <=q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i+=1
        else:
            tmp.append(a[j])
            j+=1
    #left side remain
    while i <= q:
        tmp.append(a[i])
        i += 1
    
    #right side remain
    while j <= r:
        tmp.append(a[j])
        j += 1
    
    # counting, and copying from tmp to a
    i = p
    for j in range(len(tmp)):
        a[i] = tmp[j]
        count += 1
        if count == k:
            print(a[i])
            quit()
        i += 1




def merge_sort(p:int, r:int):
    if p<r:
        #// 써야 인트로 들어감, 안그러면 float이라 안됨
        q = (p+r)//2
        merge_sort(p,q)
        merge_sort(q+1,r)
        merge(p,q,r)
n, k = map(int, input().split())
a = list(map(int, input().split()))


merge_sort(0,n-1)
print('-1')