class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def getMiddle(head):
    current = head

    count = 0
    while current:
        count += 1
        current = current.next 

    current = head
    while mid_index:
        current = current.next
        mid_index -= 1

    return current