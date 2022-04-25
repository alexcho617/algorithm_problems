#https://www.acmicpc.net/problem/4673
#셀프 넘버

#리스트 A를 먼저 숫자로 채운 다. 다음 반복문으로 숫자들을 생성한다
#생성된 숫자들을 리스트 A에서 제외시키면 남은 숫자들이 셀프넘버가 된다
#초기화 -> 생성 -> 제거 방식은 똑같지만 set으로 한번에 빼는 방법도 있다.
#하나하나 리스트에서 뺏을 경우보다 셋에서 한번에 뺀 경우 시간이 3분의 1로 줄었다.
def self_number():
    #initialize array
    initialSet = set(range(1,10000))
    generatedNumberSet = set()
    for i in range(1,10001):
        #digit sum
        n = (i + sum([int(j) for j in str(i)]))
        #remove it
        if(n < 10000):
            generatedNumberSet.add(n)
    answerSet = sorted(initialSet - generatedNumberSet)
    return answerSet

answerSet = self_number()
for l in answerSet:
    print(l)


