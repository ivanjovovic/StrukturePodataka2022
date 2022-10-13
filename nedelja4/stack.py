class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def is_empty(self):
        return len(self.items)==0
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        return self.items[-1]
    
    def print_stack(self):
        print(self.items)

s2 = Stack()
s1 = Stack()

s1.push(3)
s1.push(1)
s1.push(9)
s1.push(1)
s1.push(2)
s1.push(6)

s1.print_stack()
print("*********")

def even_odd():
    global s1
    global s2
    bucket = Stack()
    while not s1.is_empty():
        temp = s1.pop()
        if temp%2==1:
            s2.push(temp)
        else:
            bucket.push(temp)
    while not bucket.is_empty():
        s1.push(bucket.pop())
even_odd()
s1.print_stack()
print("*********")
s2.print_stack()