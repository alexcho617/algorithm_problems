def solution(sizes):
    sizes.sort(reverse = True)
    globalMax1 = 0
    globalMax2 = 0

    #max1
    for size in sizes:
        if globalMax1 < max(size):
            globalMax1 = max(size)

    #filter
    for size in sizes:
        size.remove(max(size))

    #max2
    for size in sizes:
        if size[0] > globalMax2:
            globalMax2 = size[0]
    return globalMax1 * globalMax2