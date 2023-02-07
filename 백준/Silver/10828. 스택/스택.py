class stack:
    def __init__(self, size = 10):
        self.arr = [None] * size
        self.last_index = 0
    
    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index +=1

    def pop(self):
        if self.empty() == 1:
            print(-1)
            return 0
        self.last_index -= 1
        return print(self.arr[self.last_index])
    
    def empty(self):
        if self.last_index == 0:
            return 1
        else: 
            return 0

    def size(self):
        return print(self.last_index)
    
    def top(self):
        if self.last_index == 0:
            return print("-1")
        return print(self.arr[self.last_index - 1])
#modify input method to take all commands at once


n = int(input())
cmdArr = []
for i in range(n):
    cmdArr.append(input())

# if  n < 0 or 10000 < n:
#     raise Exception("invalid argument: 1 <= n <= 10000")


st = stack(n)
for command in cmdArr:
    command = command.split(' ')
    #print(command)
    if command[0] == "push":
        command[1] = int(command[1])
        if 1 <= command[1] and command[1] <= 100000:
            st.push(command[1])
        else: raise Exception("invalid argument: 1 <= n <= 100000")
    elif command[0] == "pop":
        st.pop()
    elif command[0] == "top":
        st.top()
    elif command[0] == "size":
        st.size()
    elif command[0] == "empty":
        print(st.empty())
    else: 
        raise Exception("Wrong Command")