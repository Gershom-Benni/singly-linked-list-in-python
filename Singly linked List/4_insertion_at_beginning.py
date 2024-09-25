class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLL:
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next
    def insert_at_beginning(self,data):
        print()
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    def insert_at_end(self,data):
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
    def insert_at_any_position(self,data,position):
        npn = Node(data)
        a = self.head
        for i in range(1,position-1):
            a = a.next
        npn.next = a.next
        a.next = npn
sll = SinglyLL()
n = int(input("Enter N : "))
for i in range(n):
    sll.insert_at_end(int(input("Enter Element : ")))
    
