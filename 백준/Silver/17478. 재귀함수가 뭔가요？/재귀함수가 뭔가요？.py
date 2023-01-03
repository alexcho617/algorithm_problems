# https://www.acmicpc.net/problem/17478


def recursion(n, m1, m2, m3, m4, m5, m6):
    if n == 0:
        print(m1)
        print(m5)
        print(m6)
        return 0
    print(m1)
    print(m2)
    print(m3)
    print(m4)

    m1 = "____" + m1
    m2 = "____" + m2
    m3 = "____" + m3
    m4 = "____" + m4
    m5 = "____" + m5
    m6 = "____" + m6

    recursion(n-1, m1, m2, m3, m4, m5, m6)

    print(m6[4:])


n = int(input())
intro = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
print(intro)
m1 = "\"재귀함수가 뭔가요?\""
m2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
m3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
m4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
m5 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
m6 = "라고 답변하였지."
recursion(n, m1, m2, m3, m4, m5, m6)
