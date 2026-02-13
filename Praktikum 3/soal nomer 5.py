#=================================================================================================================
#Praktikum 3 : Linked List dalam Python
#Latihan 5 : Tambahkan metode untuk	membalik (reverse) sebuah single linked	list tanpa	membuat	linked	list baru.
#=================================================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next   # simpan next
            curr.next = prev        # balik arah
            prev = curr             # majuin prev
            curr = next_node        # majuin curr
        self.head = prev

ll = LinkedList()

data_input = input("Masukkan elemen untuk Linked List (pisahkan koma): ")
data_list = list(map(int, data_input.split(",")))

for x in data_list:
    ll.insert_at_end(x)

print("Linked List sebelum dibalik:")
ll.display()

ll.reverse()

print("Linked List setelah dibalik:")
ll.display()
