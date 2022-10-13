class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None
class DoublyLinkedlist:
    def __init__(self ):
        self.head = None
    
    

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        new_node = Node(data)
        cur.next = new_node
        new_node.prev = cur
        new_node.next = None
    
    def printaj(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next
    def duzina(self) :
        duzina = 0
        temp = self.head
        while (temp != None) :
            duzina += 1
            temp = temp.next
        return duzina


    def izbaci(self, N):
        p=0
        if N >= self.duzina():
          while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
            p=p+1
          return p  
        else:
          n=0
          while N != n :
              if self.head is None:
                return 
              if self.head.next is None:
                self.head = None
              current = self.head
              while current.next:
                current = current.next
              current.prev.next = None
              current.prev = None
              n=n+1
              
          return n
      
dl=DoublyLinkedlist()
dl.append(1)
dl.append(2)
dl.append(3)
dl.append(79)
dl.append(14)
dl.append(9)
dl.append(4)
dl.append(7)
dl.printaj()
print("**********")
print(dl.duzina())
print("**********")
print(dl.izbaci(9))
print("**********")
dl.printaj()