from itertools import permutations
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1): #제곱근 까지만 확인
            if n % i == 0:
                return False
    return True

def solution(numbers):
    answer = 0
    #셋으로 중복 숫자 제거
    numSet = set()
    for i in range(1,len(numbers)+1):
        #순열 생성
        candidates = list(permutations(numbers,i))
        #int 변형 후 셋에 추가
        for can in candidates:
            temp = ""
            for c in can:
                temp += c
                numSet.add(int(temp))
    for num in numSet:
        if isPrime(num): answer += 1
    return answer