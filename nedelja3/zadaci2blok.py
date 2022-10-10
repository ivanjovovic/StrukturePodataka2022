class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def prepend(self, new_element):
        new_element.next = self.head
        self.head = new_element
    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def brisi_prvi(self):
        if not self.head:
            return None
        self.head = self.head.next



    
    def brisi_vrijednost(self, value):
        current = self.head
        prev = None
        while current.value != value and current.next:
            prev = current
            current = current.next
        
        if current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next
    
    def duzina(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count = count + 1
        return count

    

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def kvadriraj(self):
        current = self.head
        while current:
            print(current.value * current.value)
            current = current.next
    def maksimum(self):
        current = self.head
        max_elem = current.value
        while current:
            if current.value > max_elem:
                max_elem = current.value
            current = current.next
        return max_elem
    def brisi_drugi(self):
        current = self.head
        current2 = current.next
        while current.next:
          current_2 = current.next
          current.next = current_2.next
          current = current.next
    
                   
n1 = Node(5)
n2 = Node(7)
n3 = Node(3)
n4 = Node(2)
n5= Node(1)

n6 = Node(11)
n7 = Node(17)
n8 = Node(13)
n9 = Node(22)
n10= Node(14)
#A)
l1 = LinkedList()
l1.append(n4)
l1.append(n3)
l1.append(n2)
l1.append(n1)
l1.append(n5)
l1.print_list()
print("**********************")
#B)
l2= LinkedList()
l2.prepend(n6)
l2.prepend(n7)
l2.prepend(n8)
l2.prepend(n9)
l2.prepend(n10)
l2.print_list()
print("**********************")
#D)
print(l1.maksimum())
print(l2.maksimum())
print("**********************")
#E)
l2.brisi_vrijednost(l2.maksimum())
l2.print_list()
print("**********************")
#F)
l1.kvadriraj()
l2.kvadriraj()
print("**********************")
#G)
print(l1.duzina())
print(l2.duzina())
print("**********************")

#H)
l1.brisi_vrijednost(l1.maksimum())
l1.brisi_vrijednost(l1.maksimum())
l1.print_list()
print(l1.duzina())
print("**********************")
#I)
l1.brisi_prvi()
l1.print_list()