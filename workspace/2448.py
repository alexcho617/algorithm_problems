# https://www.acmicpc.net/problem/2448

def appendStars(n):
    # base case
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    # print
    stars = appendStars(n//2)
    temp = []
    for s in stars:
        temp.append(" "*(n//2)+s+' '*(n//2))
    for s in stars:
        temp.append(s+" "+s)
    return temp
    # recursive


# n = int(input())
print("\n".join(appendStars(6)))
