
def linearSort(array):
    temp = 0
    idx = 0
    length = len(array)
    print("length of the array: (linearSort):",length)

    for idx in range (0,length-1):
        if array[idx] > array[idx + 1]:
            temp = array[idx]
            array[idx] = array[idx + 1]
            array[idx + 1] = temp
    print("printing index (linearSort)",idx)
    return array




size = int(input("How many numbers to sort?\n"))
array = [] #to store them
sorted = []
for i in range(0,size):
    n= int(input())
    array.append(n)
print(array)

array = linearSort(array)
print(array)
