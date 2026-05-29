class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def print_chain(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def remove_nth_from_end(self, n):

        dummy = Node(0)
        dummy.next = self.head

        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        self.head = dummy.next

messages = LinkedList()

messages.append("Msg1")
messages.append("Msg2")
messages.append("Msg3")
messages.append("Msg4")
messages.append("Msg5")

print("Original Message Chain:\n")
messages.print_chain()

n = 2

messages.remove_nth_from_end(n)

print(f"\nAfter Removing {n}th Message From End:\n")
messages.print_chain()