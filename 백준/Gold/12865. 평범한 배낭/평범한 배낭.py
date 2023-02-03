# https://www.acmicpc.net/problem/12865
# Knapsack

# items = [
#     [6, 13],
#     [4, 8],
#     [3, 6],
#     [5, 12],
# ]
# numberOfItems,weightTotal=4,7
numberOfItems, weightTotal = map(int, (input().split()))
items = [[0,0]]
for _ in range(numberOfItems):
    items.append(list(map(int,input().split())))
arr = [[0] * (weightTotal + 1) for _ in range(numberOfItems + 1)]

#main loop
for currentItem in range(1,numberOfItems+1):
    for currentWeight in range(1,weightTotal + 1):
        itemWeight = items[currentItem][0]
        itemValue = items[currentItem][1]

        if currentWeight < itemWeight:#bag cannot hold anymore
            arr[currentItem][currentWeight] = arr[currentItem-1][currentWeight]
        else:
            arr[currentItem][currentWeight] = max(arr[currentItem-1][currentWeight],arr[currentItem-1][currentWeight - itemWeight] + itemValue)



print(arr[-1][-1])