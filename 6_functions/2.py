def getSum(n):
    sum1 = 0
    while (n != 0):
        sum1 = sum1 + n % 10 #get last digit
        n = n // 10 #advance to next digit
    return sum1
 
def isSelfNum(n):
    for m in range(1, n + 1):
        if (m + getSum(m) == n):#loop from 1 to n, add the sum of digits till n is found.
            return False
    return True
 
n = 221
if (isSelfNum(n)):
    print("Yes")
 
else:
    print("No")