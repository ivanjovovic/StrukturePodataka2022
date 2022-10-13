class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items

    def __len__(self):
        return len(self.items)


s = Stack()
s.push("G")
s.push("E")
s.push("+")
s.push("D")
s.push("+")
s.push("+")
s.push("+")
s.push("C")
s.push("+")
s.push("B")
s.push("L")
s.push("A")
print(s.get_stack())

def ocisti_bombe():
    cisti_stek = Stack()
    counter=0
    while not s.is_empty():
        element = s.pop()
        if element=="+":
            counter = counter + 1
        if element != "+":
            cisti_stek.push(element)
    print("Ocisceni stek:" + str(cisti_stek.get_stack())+ "--" + "Broj bombi u steku:" + str(counter))

ocisti_bombe()