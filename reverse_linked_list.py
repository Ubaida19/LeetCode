class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, data):
        if not self.head:
            self.head = ListNode(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(data)
    def printList(self):
        current = self.head
        while current:
            print(current.val,end=" ")
            current = current.next

    def reverseList(self,head:ListNode)->ListNode:
        # temp = head
        # stack = []
        # while temp:
        #     stack.append(temp.val)
        #     temp = temp.next
        
        # temp2 = head
        # while stack:
        #     temp2.val = stack.pop()
        #     temp2 = temp2.next
        # return head

        current_node = head
        prev_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node
    
def main():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.printList()
    print()
    linked_list.reverseList(linked_list.head)
    linked_list.printList()
    print()
    linked_list2 = LinkedList()
    linked_list2.insert(1)
    linked_list2.insert(2)
    linked_list2.printList()
    print()
    linked_list2.reverseList(linked_list2.head)
    linked_list2.printList()
    print()
    linked_list3 = LinkedList()
    linked_list3.reverseList(linked_list3.head)
main()