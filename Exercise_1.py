
class myStack:
     def __init__(self):
         self.myStack=[]
         
     def isEmpty(self):
         if len(self.myStack)==0:
             print("Stack is empty")
     def push(self, item):
         self.myStack.append(item)
         
     def pop(self):
         if len(self.myStack)==0:
             print("stack is empty. Unable to pop")
             return 0
         else:
             return self.myStack.pop()

     def peek(self):
         return(self.myStack[-1])
         
     def size(self):
         return(len(self.myStack))
         
     def show(self):
         return(self.myStack)
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
