class Stack1:
    def __init__(self, size = 10):
        self.arr = [None] * size # we can reduce perfomance cost by purposely using static array
        self.last_index = 0

    def push(self, value):

        self.arr[self.last_index] = value #must add self here
        self.last_index += 1 # increas index
    
    def pop(self):
        if self.empty == True: #safe check
            raise Exception('Stack is Empty')
        return self.arr[self.last_index -1]

    def empty(self):
        if self.last_index == 0:
            return True
        else: False
    
    def peek(self):
        if self.empty: #safe check
            raise Exception('Stack is Empty')
        return self.arr[self.last_index - 1]

st = Stack1(5)
for i in range(5):
    st.push(i)
print('pop',st.pop())

print(st.arr) #still exists in stack