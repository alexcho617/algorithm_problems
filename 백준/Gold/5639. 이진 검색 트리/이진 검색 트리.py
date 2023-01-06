#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


class Element(object):
    def __init__(self, value, lower, upper):
        self.value = value
        self.lower = lower
        self.upper = upper


def solve(pre_ordered):
    if (len(pre_ordered) == 0):
        return pre_ordered

    post_ordered = []
    stack = [Element(pre_ordered[0], 1, 1000000 - 1)]
    for n in pre_ordered[1:]:
        while n < stack[-1].lower or stack[-1].upper < n:
            e = stack.pop(-1)
            post_ordered.append(e.value)
        if n < stack[-1].value:
            stack.append(Element(n, stack[-1].lower, stack[-1].value - 1))
        else:
            stack.append(Element(n, stack[-1].value + 1, stack[-1].upper))
    while 0 < len(stack):
        post_ordered.append(stack.pop(-1).value)
    return post_ordered


if __name__ == "__main__":
    pre_ordered = []
    while True:
        try:
            pre_ordered.append(int(sys.stdin.readline().strip()))
        except:
            break

    for key in solve(pre_ordered):
        print(key)