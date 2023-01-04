# https://www.acmicpc.net/problem/1780

negs, zeros, pos = 0, 0, 0


def check_all_minus_one(page: list):
    for pag in page:
        for pa in pag:
            if pa != -1:
                return False
    return True


def check_all_zero(page: list):
    for pag in page:
        for pa in pag:
            if pa != 0:
                return False
    return True


def check_all_plus_one(page: list):
    for pag in page:
        for pa in pag:
            if pa != 1:
                return False
    return True


def divide(graph: list):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = [], [], [], [], [], [], [], [], []

    onethird = len(graph) // 3
    twothird = len(graph) // 3 * 2

    for i in range(onethird):
        s1.append(graph[i][:onethird])
        s2.append(graph[i][onethird:twothird])
        s3.append(graph[i][twothird:])

    for i in range(onethird, twothird):
        s4.append(graph[i][:onethird])
        s5.append(graph[i][onethird:twothird])
        s6.append(graph[i][twothird:])

    for i in range(twothird, len(graph)):
        s7.append(graph[i][:onethird])
        s8.append(graph[i][onethird:twothird])
        s9.append(graph[i][twothird:])

    return s1, s2, s3, s4, s5, s6, s7, s8, s9


def recursion(graph: list, n: int):
    global negs, zeros, pos
    # if all(0 not in l for l in graph):
    #     if all(-1 not in l for l in graph):
    #         pos += 1
    #         return
    #     elif all(1 not in l for l in graph):
    #         negs += 1
    #         return
    # if all(1 not in l for l in graph):
    #     if all(-1 not in l for l in graph):
    #         zeros += 1
    #         return
    if check_all_minus_one(graph):
        negs += 1
        return
    if check_all_zero(graph):
        zeros += 1
        return
    if check_all_plus_one(graph):
        pos += 1
        return

    else:
        for s in divide(graph):
            recursion(s, n//3)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
recursion(graph, n)
print(negs)
print(zeros)
print(pos)
