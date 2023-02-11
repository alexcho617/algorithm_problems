#https://www.acmicpc.net/problem/13335
import sys
from collections import deque
sys.stdin.readline
N,W,L = map(int,input().split())
trucks = deque(list(map(int,input().rstrip().split())))
bridge = deque([0 for _ in range(W)])

clock = 0
currentLoad = 0
truckCounter = 0

#loop until all trucks have passed
while truckCounter < N:
    clock += 1
    #if truck made it to end of bridge
    if bridge[0] != 0:
        #pop the truck
        currentLoad -= bridge[0]
        bridge[0] = 0
        #add truck counter
        truckCounter += 1
    
    bridge.rotate(-1)
    
    #load
    if trucks and currentLoad + trucks[0] <= L:
        truckIn = trucks.popleft()
        bridge[-1] = truckIn
        currentLoad += truckIn
    
    #DEBUG: break
    # if clock == 15:quit()

    # print(bridge,clock)
print(clock)