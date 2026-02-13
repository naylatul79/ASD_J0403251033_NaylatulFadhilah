class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        temp = self.head
        if not temp:
            print("Doubly Linked List kosong.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Latihan 3: search
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


# Contoh uji (sesuai contoh tampilan #1 di materi)
dll = DoublyLinkedList()

data_input = input("Masukkan elemen (pisahkan dengan koma): ")
data_list = list(map(int, data_input.split(",")))

for x in data_list:
    dll.insert_at_end(x)

cari = int(input("Masukkan elemen yang ingin dicari: "))

if dll.search(cari):
    print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {cari} tidak ditemukan dalam Doubly Linked List.")

