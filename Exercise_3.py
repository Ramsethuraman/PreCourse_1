class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        if self.head==None:
            self.temp=ListNode(data)
            self.head=self.temp
        else:
            self.temp=self.head
            while(self.temp.next!=None):
                self.temp=self.temp.next
            self.newe=ListNode(data)
            self.temp.next=self.newe
            self.newe.next=None
            
                
            
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        
    def find(self, key):
        self.index=0
        self.temp=self.head
        self.flag=-1
        if self.temp==None:
            return None,None
        while(self.temp!=None):
            self.index+=1
            if self.temp.data==key:
                self.flag=1
                return self.temp.data,self.index
            self.temp=self.temp.next
        if self.flag==-1:
            return None,None
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        
    def remove(self, key):
        self.temp=self.head
        if self.temp==None:
            return None
        elif self.temp.data==key:
            self.head=self.head.next
            return "Element"+str(self.temp.data)+ "Deleted"
        elif self.temp.next!=None:
            while(self.temp.next!=None):
                if self.temp.data==key:
                    a=self.temp.data
                    self.prev.next=self.temp.next
                    return "Element"+str(a)+ "Deleted"
                self.prev=self.temp
                self.temp=self.temp.next
            if self.temp.data==key:
                self.prev.next=None
                return "Element" + str(self.temp.data)+ "Deleted"
                
        else:
            return None
                    
                    
                    
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
    def printlist(self):
        if self.head==None:
            print("NO List")
        else:
            self.temp=self.head
            while(self.temp!=None):
                print(self.temp.data)
                self.temp=self.temp.next
        print("\n")
        
N1=SinglyLinkedList()
N1.printlist()
N1.append(2)
N1.printlist()
N1.append(4)
N1.append(9)
N1.append(9)
N1.append(4)
N1.append(0)
N1.append(5)
N1.printlist()
a,b=N1.find(2)
print("ELEMENT IS",a, "POSITION IS",b)
N1.printlist()
print(N1.remove(0))
N1.printlist()