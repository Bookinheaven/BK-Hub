# Stack array list
class Stack :
    def __init__(self): 
        self.stack = []
        self.Max = 1
        self.top = -1  
    def create(self, array: list, Max: int) :
        self.Max = Max
        self.stack = array
        print(f"Stack is created with {self.Max} data => {self.stack}")
    def pop(self):
        def isEmpty():
            if(len(self.stack) == 0):
                return True
            else :
                return False
        if(isEmpty() == False):
            popped = self.stack[-1] 
            # self.top -= 1
            self.stack.remove(popped)
            print(f"Popped : {popped}")
        else:
            print("Stack is Empty")
    def push(self, value):
        def isFull():
            if (len(self.stack) == self.Max):
                return True
            else:
                return False
        if (isFull()):
            print("The Stack Reached Its limit")
        else:
            self.stack.append(value)
            # self.top += 1
    def peek(self):
        print(f"Peek element in the stack: {self.stack[self.top]}")
    def display(self):
        print(f"Stack limit: [{self.Max}] data => {self.stack}")
    
array1 : list = [1,2,3,4]
stack1 = Stack()
stack1.create(array = array1, Max = 5)
stack1.push(12)
stack1.display()
stack1.pop()
stack1.push(122)
stack1.display()
stack1.peek()
stack1.display()