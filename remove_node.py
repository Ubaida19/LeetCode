class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def get_head_val(self):
        return self.head.val

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
            print(current.val, '->')
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_ptr = current.next
            current.next = prev
            prev = current
            current = next_ptr
        self.head = prev
        return prev


    def remove_node(self, head):
        reversed = self.reverse()
        greater_val = float('-inf')
        curr = reversed
        prev = None
        while curr:
            if curr.val < greater_val:
                next_ptr = curr.next
                prev.next = next_ptr

            elif curr.val >= greater_val:
                greater_val = curr.val
                prev = curr
            curr = curr.next
        result = self.reverse()
        return result

def main():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(2)
    linked_list.append(13)
    linked_list.append(3)
    linked_list.append(8)
    linked_list.remove_node(linked_list.get_head)
    linked_list.print_list()


if __name__ == "__main__":
    main()
