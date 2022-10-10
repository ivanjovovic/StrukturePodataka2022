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

    def delete_first(self):
        if not self.head:
            return None
        self.head = self.head.next

    def delete_last(self):
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def get_value_from_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter = counter + 1
        return None

    def insert_on_position(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter = counter + 1
            return None
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            return None

    def delete_val(self, value):
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
    
    def delete_from_position(self, position):
        current = self.head
        prev = None
        counter = 1

        if position == 1:
            self.head = current.next
            current = None
            return
        
        while current and counter != position:
            prev = current
            current = current.next
            counter = counter + 1

        if current is None:
            return None

        prev.next = current.next
        current = None

    def len_iterative(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count = count + 1
        return count

    def getCountRec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.getCountRec(node.next)
    
    def len_recursive(self):
        return self.getCountRec(self.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    #        
    def minimalni(self):
        current = self.head
        min_elem = current.value
        while current:
            if current.value < min_elem:
                min_elem = current.value
            current = current.next
        return min_elem
    def brisi_drugi(self):
        current = self.head
        current2 = current.next
        while current.next:
          current_2 = current.next
          current.next = current_2.next
          current = current.next

    def brisi_svaki_drugi(self):
        brojac=1
        current=self.head
        prev=current
        while current:
            if brojac==2:
                prev.next=current.next
                brojac=0
            brojac+=1
                
            prev=current
            current=current.next          
    def delete_min(self):
        current=self.head
        min=self.head.value
        while current:
            if current.value<min:
                min=current.value
            current=current.next
        self.delete_value(min)
        self.print_list()
    
    def concat_lists(self, l2):
        current = self.head
        if not current:
            current.head = l2.head
        else:
            while current.next:
#                 print(current.value)
                current = current.next
            current.next = l2.head

    def concat (self,other):
        current = self.head
        while current.next:
            current = current.next

        current.next = other.head

n1 = Node(5)
n2 = Node(7)
n3 = Node(3)
n4 = Node(2)
n5= Node(1)

n6 = Node(8)
n7 = Node(9)
n8 = Node(11)
n9 = Node(12)
n10= Node(14)

l1 = LinkedList()
l1.prepend(n4)
l1.prepend(n3)
l1.prepend(n2)
l1.prepend(n1)
l1.prepend(n5)
l2 = LinkedList()
l2.append(n6)
l2.append(n7)
l2.append(n8)
l2.append(n9)
l2.append(n10)

l2.concat(l2)
#print(n1.value)
#print("************")
#l1.print_list()
#print("************")
#l1.delete_first()
#l1.print_list()
#print("************")
#print(l1.get_value_from_position(2).value)
#print("************")
#l1.delete_val(3)
#l1.print_list()
#print("************")
#print(l1.len_iterative())
#print(l1.len_recursive())
#l1.print_list()
#print("************")
#l2.print_list()

#l1.delete_val(l1.minimalni())

#print("************")
#l1.brisi_drugi()
#l1.print_list()
# l1.concat_lists(l2)
l1.print_list()