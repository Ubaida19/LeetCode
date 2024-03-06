class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    def removeNthFromEnd(self, head, n: int):
        current = head
        nodes = 0
        while current:
            nodes += 1
            current = current.next

        if nodes-n-1 == -1:
            return head.next
        else:
            new_start = head
            i = 0
            while i<nodes-n-1:
                new_start = new_start.next
                i += 1
            new_start.next = new_start.next.next
            return head
        
