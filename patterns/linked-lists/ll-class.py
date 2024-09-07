class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        head = None
        tail = None
        self.count = 0

    def addNodes(self, data):
        # Append items to the end of the list
        node = Node(data)
        if self.tail:
            self.tail.next = node  # Link the new node after the current tail
            self.tail = node       # Update the tail to be the new node
        else:
            self.head = node  # Set both head and tail to the new node if the list is empty
            self.tail = node
        self.count += 1

    def getSize(self):
        current = self.head

        return self.count

