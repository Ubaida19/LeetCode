class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
    
    
    def is_empty(self):
        return self.head is None


    def append(self, data):
        new_node = ListNode(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

def main():
    linked_list = LinkedList()

    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(1)
    linked_list.append(9)
    linked_list.deleteNode(linked_list.head.next)
    linked_list.print_list()
    
    
if __name__ == "__main__":
    main()