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
    def insert_at_any_position(self,data,position):
        npn = Node(data)
        a = self.head
        for i in range(1,position-1):
            a = a.next
        npn.next = a.next
        a.next = npn

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

sll.insert_at_any_position(100,3)

sll.traversal()