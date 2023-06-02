# https://www.acmicpc.net/problem/1074
def recursion(n, r, c):
    # base case
    if n == 1:
        if r == 0:
            if c == 0:
                return 0
            elif c == 1:
                return 1
        elif r == 1:
            if c == 0:
                return 2
            else:
                return 3
    # recursive case
    else:
        mid = 2**(n-1) - 1  # half point
        domain = 2**n * 2**n // 4
        # topleft
        if r <= mid and c <= mid:
            return 0 + recursion(n-1, r, c)
        # topright
        if r <= mid and c > mid:
            return domain + recursion(n-1, r, c-(mid+1))  # shift left
        # bottomleft
        if r > mid and c <= mid:
            return domain * 2 + recursion(n-1, r-(mid + 1), c)  # shift up

        # bottomright
        if r > mid and c > mid:
            return domain * 3 + recursion(n-1, r-(mid+1), c-(mid+1)) #shift up and left


n, r, c = map(int, input().split())
print(recursion(n, r, c))
