class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head=None
        
    def push(self, data):
        if self.head==None:
            self.head=Node(data)
            print("Pushed value is:", self.head.data)
        else:
            self.temp=Node(data)
            self.temp.next=self.head
            self.head=self.temp
            print("Pushed value is:",self.head.data)
        
    def pop(self):
        if self.head==None:
            return None
        else:
            self.value=self.head.data
            self.head=self.head.next
            return self.value
            
        
a_stack = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
