class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLL:
    def __init__(self):
        self.head = None
    def traversal(self):
        print()
        if self.head is None:
            print("Linked list is empty!")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next
    def delete_at_beginning(self):
        a = self.head
        self.head = a.next
        a.next = None
sll = SinglyLL()
n1 = Node(5)
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(20)
n3.next = n4

sll.traversal()

sll.delete_at_beginning()
sll.traversal()