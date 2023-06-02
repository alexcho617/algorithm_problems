# https://www.acmicpc.net/problem/3190
import sys
from collections import deque
import itertools
sys.stdin.readline

n = int(input())
k = int(input())

# initially snake goes to right
direction = "R"
apples = []
turns = []
for _ in range(k):
    apples.append(list(map(int, input().split())))

l = int(input())
for _ in range(l):
    temp = input().split()
    turns.append([int(temp[0]), temp[1]])
counter = 0

# snake is a que of list
# ~~~> tail on left head on right side of que
snake = deque()
snake.append([1, 1])
# move eat apple or not


def move(snake: deque):
    global counter
    global direction
    counter += 1

    currHead = snake[-1]
    currHeadR = currHead[0]
    currHeadC = currHead[1]
    # extend head towards direction
    if direction == "R":
        snake.append([currHeadR, currHeadC + 1])
    elif direction == "L":
        snake.append([currHeadR, currHeadC - 1])
    elif direction == "U":
        snake.append([currHeadR - 1, currHeadC])
    elif direction == "D":
        snake.append([currHeadR + 1, currHeadC])

    # end game if head collides with body
    body = deque(itertools.islice(snake, 0, len(snake)-1))
    if snake[-1] in body:
        print(counter)
        quit()

    # if not apple cut tail
    if snake[-1] in apples:
        apples.pop(0)
    else:
        snake.popleft()

    # check dir
    if turns and counter == turns[0][0]:
        if turns[0][1] == "L":
            if direction == "R":
                direction = "U"
            elif direction == "L":
                direction = "D"
            elif direction == "U":
                direction = "L"
            elif direction == "D":
                direction = "R"
        # D = turn right
        else:
            if direction == "R":
                direction = "D"
            elif direction == "L":
                direction = "U"
            elif direction == "U":
                direction = "R"
            elif direction == "D":
                direction = "L"
        turns.pop(0)

# driver
while True:
    #emergency break
    # if counter == 30:
    #     print('Emergency Break')
    #     quit()
    # end game if out of bound
    if snake[-1][0] > n or snake[-1][1] > n or snake[-1][0] < 1 or snake[-1][1] < 1:
        print(counter)
        quit()
    else:
        move(snake)
        # print(*list(snake), counter)
