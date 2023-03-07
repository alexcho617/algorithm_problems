# -*- coding: utf-8 -*-
import math
import time
start = time.time()

a = 4095
# lst = [4, 5, 3, 8, 3, 2, 1, 1, 1]
lst=[0 for i in range(a)]
# print(lst)
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

#solve

result = []
result.append(lst)

for i in range(count+1):
    new_lst = []
    for j in range(0, len(result[i]), 2):
        new_lst.append(result[i][j] + result[i][j+1])
    result.append(new_lst)

for lst in result[::-1]:
    for el in lst:
        print(el, end=' ')
    print()


end = time.time()
print(end - start)