class queue:
    def __init__(self,size = 10):
        self.arr = [None] * size
        self.first_index = 0
        self.last_index =0

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1
    
    def pop(self): #pop failing
        if self.empty == 1:
            raise Exception ("pop failed, queue empty")
        else:
            print(self.arr[self.first_index])
            self.first_index += 1
        return 0
    def size(self):
        return print(self.last_index - self.first_index)

    def empty(self):
        if self.last_index == 0:
            return 1
        elif self.first_index == self.last_index:
            return 1
        else: return 0

    def front(self):
        return print(self.arr[self.first_index])
    
    def back(self):
        return print(self.arr[self.last_index-1])



n = int(input())
if  n < 0 or 10000 < n:
    raise Exception("invalid argument: 1 <= n <= 10000")

qu = queue(n)

for i in range(n):
    command = input()
    command = command.split(' ')
    #print(command)
    if command[0] == "push":
        command[1] = int(command[1])
        if 1 <= command[1] and command[1] <= 100000:
            qu.push(command[1])
        else: raise Exception("invalid argument: 1 <= n <= 100000")
    elif command[0] == "pop":
        qu.pop()
    elif command[0] == "size":
        qu.size()
    elif command[0] == "empty":
        print(qu.empty())
    elif command[0] == "front":
        qu.front()
    elif command[0] == "back":
        qu.back()
    else: 
        print("Wrong Command")
        continue