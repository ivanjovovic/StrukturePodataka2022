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

s1=Stack()

def u_binarni(broj):
    s = Stack()
    while broj>0:
        reminder=broj%2
        s.push(reminder)
        broj = broj//2
    binarni_broj=""
    while not s.is_empty():
        binarni_broj=binarni_broj+str(s.pop())
    return binarni_broj
print(u_binarni(6))









'''
def to_binary(num):
    
    while num > 0:
        reminder = num % 2
        s1.push(reminder)
        num = num // 2
    
    bin_num = ""
    while not s1.is_empty():
        bin_num = bin_num + str(s1.pop())
    return bin_num

print(to_binary(94))
'''