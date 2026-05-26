# Day 23 - Train Carriage Reversal Challenge

# -----------------------------------
# Node Class
# -----------------------------------

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


# -----------------------------------
# Linked List Class
# -----------------------------------

class LinkedList:

    def __init__(self):

        self.head = None

    # -----------------------------------
    # Add Carriage
    # -----------------------------------

    def append(self, data):

        new_node = Node(data)

        # Empty list
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # -----------------------------------
    # Print Train
    # -----------------------------------

    def print_train(self):

        current = self.head

        while current:

            print(current.data, end=" -> ")

            current = current.next

        print("None")

    # -----------------------------------
    # Reverse Linked List
    # -----------------------------------

    def reverse(self):

        previous = None
        current = self.head

        while current:

            # Store next node
            next_node = current.next

            # Reverse pointer
            current.next = previous

            # Move pointers forward
            previous = current
            current = next_node

        # Update head
        self.head = previous


# -----------------------------------
# Train Carriages
# -----------------------------------

train = LinkedList()

train.append("Engine")
train.append("C1")
train.append("C2")
train.append("C3")
train.append("C4")

# Original Train
print("Original Train Order:\n")

train.print_train()

# Reverse Train
train.reverse()

# Reversed Train
print("\nReversed Train Order:\n")

train.print_train()