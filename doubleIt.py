class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

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

    def print_list(self,head):
        current = head
        while current:
            print(current.val)
            current = current.next

    def double_it(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while current:
            twice_val = current.val * 2
            if twice_val < 10:
                current.val = twice_val
            elif prev:
                current.val = twice_val % 10
                prev.val += twice_val // 10
            else:
                head = ListNode(twice_val // 10, current)

                current.val = twice_val % 10

            prev = current
            current = current.next

        return head




def main():
    # linked_list = LinkedList()
    #
    # linked_list.append(1)
    # linked_list.append(8)
    # linked_list.append(9)
    #
    # linked_list.double_it(linked_list.head)
    # linked_list.print_list(linked_list.head)
    #
    # print()
    linked_list2 = LinkedList()
    linked_list2.append(9)
    linked_list2.append(9)
    linked_list2.append(9)

    start = linked_list2.double_it(linked_list2.head)
    linked_list2.print_list(start)


main()