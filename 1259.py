#https://www.acmicpc.net/problem/1259

while True:
    num = input()
    if num == '0': quit()
    if num == num[::-1]:
        print("yes")
    else: print("no")