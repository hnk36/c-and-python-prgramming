
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        if self.head is None:
            print("Linked list is empty")
        else:
            while temp:
                print(temp.name, end="->")
                temp = temp.next
            print("None")
# Create node objects
link = LinkedList()
pr_node = None
numberOfNode = 5
for i in range(numberOfNode):
    new_name = input(f"Enter name of {i+1} node: ")
    new_node = Node(new_name)
    if link.head is None:
        link.head = new_node
    else:
        pr_node.next = new_node
    pr_node = new_node

# Display the linked list
link.display()