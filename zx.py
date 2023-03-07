#DEBUG:
# import time
import math

def construct_tree(leaves):
    n = len(leaves)
    tree = [None] * (2*n - 1)

    # Copy the leaves to the bottom level of the tree
    for i in range(n):
        tree[n-1+i] = leaves[i]

    # Construct the upper levels of the tree
    for i in range(n-2, -1, -1):
        tree[i] = tree[2*i+1] + tree[2*i+2]

    return tree

def print_tree(tree):
    levels = math.ceil(math.log2(len(tree)))
    for i in range(levels):
        level_start = 2**i - 1
        level_end = min(level_start + 2**i, len(tree))
        level_nodes = tree[level_start:level_end]
        print(*level_nodes)

#DEBUG:
# start = time.time()

# Example usage
a = 9
leaves = [4,5,3,8,4,2,1,1,1]


tree = construct_tree(leaves)
print_tree(tree)

#DEBUG: print time
# end = time.time()
# print(end - start)