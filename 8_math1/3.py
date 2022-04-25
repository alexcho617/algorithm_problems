#https://www.acmicpc.net/problem/1193
#분수찾기

n = 0
total = 0
#숫자 x 를 입력받는다.
x = int(input())

#토탈이 x보다 커질때까지 반복한다. 토탈이 커지는 순간에 n이 분수가 있는 줄이다.
while(x > total):
    n += 1
    total += n

#몇번째 분수인지 구한다
prevTotal = total - (n)
difference = x - prevTotal

if n % 2 == 0:
    isEven = True
else:
    isEven = False

#n이 홀수
if(isEven == False):
    top = n - difference + 1
    bottom = difference
#n이 짝수
else:
    top = difference
    bottom = n - difference + 1
print("{:d}/{:d}".format(top,bottom))

