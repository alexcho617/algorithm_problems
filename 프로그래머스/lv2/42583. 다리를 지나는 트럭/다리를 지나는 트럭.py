from collections import deque

def solution(bridge_length, weight, truck_weights):
    clock = 0
    bridgeQue = deque([0 for _ in range(bridge_length)]) #0으로 초기화
    truckQue = deque(truck_weights)
    currentBridgeWeight = 0
    
    while True:
        # print("CLOCK:",clock,"BRIDGE:", bridgeQue,"WEIGHT:",currentBridgeWeight)
        
    
        #getoff
        if bridgeQue[0] != 0:
            print("GET OFF:",bridgeQue[0])
            currentBridgeWeight -= bridgeQue[0]
            # currentBridgeCount -= 1
            bridgeQue[0] = 0

            #rotate
        clock += 1
        bridgeQue.rotate(-1) #trucks go from right to left
        
        #board
        if truckQue:
            if truckQue[0] + currentBridgeWeight <= weight:
                currentTruck = truckQue.popleft()
                # print("BOARD:", currentTruck)
                bridgeQue[bridge_length - 1] = currentTruck
                currentBridgeWeight += currentTruck

        #end condition
        if len(truckQue) == 0:
            print("currentTruck Empty")
            if currentBridgeWeight == 0:
                break

    answer = clock
    return answer