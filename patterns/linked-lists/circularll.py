# Search an Element in a Circular Linked List
# For example, if the key to be searched is 30 and the linked list is 5->4->3->2, then the function should return false. If the key to be searched is 4, then the function should return true. 
class Node:  
    def __init__(self,data):     
        self.data = data; 
        self.next = None; 

class CircularLinkedList:
    def __init__(self, data=None):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def addNode(self,data):
        new_node = Node(data)

        if self.head.data is None:

            self.head = new_node
            self.tail = new_node

            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def search_element(self, num):
        current = self.head
        head = self.head
        while current:
            if current == head:
                break

            if current.val == num:
                return True
            current = current.next
        
        return False