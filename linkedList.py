class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)

def printNodes (node: ListNode):
    current = node
    while current is not None:
        print(current.val, end=' ')
        current = current.next

printNodes(head_node)