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
            
            
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        count = 1
        if left == right:
            return head
        temp = head
        while temp and left<=right:
            if count == left:
                dumm_left = temp
                stack = []
                while count <= right:
                    stack.append(dumm_left.val)
                    dumm_left = dumm_left.next
                    count += 1
                break
            temp = temp.next
            count += 1
        while stack:
            temp.val = stack.pop()
            temp = temp.next
        return head
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val, end = " ")
            temp = temp.next
def main():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.printList()
    linked_list.reverseBetween(linked_list.head,2, 4)
    print()
    linked_list.printList()
    print()
    linked_list2 = LinkedList()
    linked_list2.insert(5)
    linked_list2.printList()
    linked_list2.reverseBetween(linked_list2.head,1, 1)
    print()
    linked_list2.printList()
    print()
    linked_list3 = LinkedList()
    linked_list3.insert(3)
    linked_list3.insert(5)
    linked_list3.printList()
    print()
    linked_list.reverseBetween(linked_list3.head,1, 2)
    linked_list3.printList()
main()