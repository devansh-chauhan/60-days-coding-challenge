class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def create_cycle(self, position):
        if position < 0:
            return

        cycle_node = None
        current = self.head
        index = 0

        while current.next:

            if index == position:
                cycle_node = current

            current = current.next
            index += 1

        current.next = cycle_node

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

maze1 = LinkedList()

maze1.append("A")
maze1.append("B")
maze1.append("C")
maze1.append("D")

print("Maze 1 Has Cycle:",
      maze1.detect_cycle())

maze2 = LinkedList()

maze2.append("X")
maze2.append("Y")
maze2.append("Z")
maze2.append("W")

maze2.create_cycle(1)

print("Maze 2 Has Cycle:",
      maze2.detect_cycle())