import math
import time

class SumTree:

  def __init__(self, leaves):
    self.leaves = leaves

  def nodeAt(self, i, j):
    if i < self.height() - 1:
      return self.nodeAt(i+1, 2*j) + self.nodeAt(i+1, 2*j+1)
    elif i == self.height() - 1:
      return self.leaves[j]
    else:
      raise 'no nodes exists at this depth.'

  def nodesAtDepth(self, i):
    return [self.nodeAt(i, j) for j in range(self.widthAtDepth(i))]

  def maxWidth(self):
    return self.widthAtDepth(self.height() - 1)

  def widthAtDepth(self, i):
    return 2 ** i

  def height(self):
    return math.floor(math.log(len(self.leaves), 2)) + 1

  def __str__(self):
    result = ''
    width = self.maxWidth()
    for i in range(self.height()):
      result += '{}\n'.format(self.nodesAtDepth(i))
    return result



start = time.time()
# lst = [4, 5, 3, 8, 4, 2, 1, 1, 1]
# a = 9

a = 4095
# lst = [4, 5, 3, 8, 3, 2, 1, 1, 1]
lst=[1000 for i in range(a)]
count = 0
b = a


#get tree level
while (True):
    b = b/2
    if int(b) == 1:
        if b != 1:
            count += 1
        break
    else:
        count = count + 1

#extra zeros
add_0 = 2**(count+1) - int(a)
lst = lst + [0] * add_0
# print(lst)
# tree = SumTree(list(range(1, 5)))
tree = SumTree(lst)
# print('leaves', tree.leaves)
# print('height', tree.height())
print(tree)

end = time.time()
print(end - start)