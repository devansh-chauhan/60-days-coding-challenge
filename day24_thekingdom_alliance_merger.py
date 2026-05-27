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

    
    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def merge_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next

        else:
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next
    
    if list1:
        tail.next = list1

    if list2:
        tail.next = list2

    return dummy.next

army1 = LinkedList()

army1.append(1)
army1.append(3)
army1.append(5)
army1.append(7)

army2 = LinkedList()

army2.append(2)
army2.append(3)
army2.append(6)
army2.append(8)


print("First Army:\n")
army1.print_list()

print("\nSecond Army:\n")
army2.print_list()

merged_head = merge_lists(
    army1.head,
    army2.head
)

print("\nMerged Sorted Army:\n")

current = merged_head

while current:

    print(current.data, end=" -> ")

    current = current.next

print("None")