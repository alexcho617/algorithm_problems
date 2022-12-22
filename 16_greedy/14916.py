#https://www.acmicpc.net/problem/14916

from unittest import case


n = int(input())
f = 0
t = 0
ans = 0

#when n is greater than 5
if n >= 5:
    a = n // 5
    remain = n % 5
    b = remain // 2
    #divisible by 5
    if remain == 0:
        ans = a
    elif remain == 1 or remain == 3:
        a -= 1
        remain += 5
        b = remain // 2
        ans = a + b
    elif remain == 2 or remain == 4:
        b = remain // 2
        ans = a+b
#when n is lesser than 5
else:
    if n == 1 or 3:
        ans = -1
    if n == 0:
        ans = 0
    if n == 4:
        ans = 2
    if n == 2:
        ans = 1
# print(ans, a, b, remain)
print(ans)





#연수 코드, 5로 빼면서 어레이에 저장한 후 마지막에 최소값 출력 하는 방식
# n = int(input())
# cnt = 0

# if n % 5 == 0:
# 	print(n // 5)	
# else:
# 	if (n % 5) % 2 == 0:
# 		print((n // 5) + ((n % 5) // 2))
# 	else:
# 		result = []
# 		i = 0
# 		while True:
# 			cnt = i
# 			if n < 0: 
# 				break
# 			if n % 2 == 0:
# 				cnt += (n // 2)
# 				result.append(cnt)
# 			n -= 5
# 			i += 1
# 		print(min(result)) if len(result) else print(-1)
			