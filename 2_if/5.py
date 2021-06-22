h,m = input().split()
h = int(h)
m = int(m)


if(m < 45):
    m += 60
    m -= 45
    h -= 1
    if h < 0:
        h = 23
else:
    m = m-45
    
print(h,m)