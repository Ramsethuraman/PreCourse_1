
class myStack:
     def __init__(self):
         self.myStack=[]
         
     def isEmpty(self): #Time complexity is O(1)
         if len(self.myStack)==0:
             print("Stack is empty")
             
        
     def push(self, item): #Time complexity is O(1)
         self.myStack.append(item)
         
     def pop(self): #Time complexity is O(1)
         if len(self.myStack)==0:
             print("stack is empty. Unable to pop")
             return 0
         else:
             return self.myStack.pop()

     def peek(self): #Time complexity is O(1)
         return(self.myStack[-1])
         
     def size(self): #Time complexity is O(1)
         return(len(self.myStack))
         
     def show(self): #Time complexity is O(N)
         return(self.myStack)
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
