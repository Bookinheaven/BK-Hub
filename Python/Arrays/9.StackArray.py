class Stack:
    def __init__(self):
        self.stack = []
        self.Max = 1
        self.top = -1  
    
    def create(self, array: list, Max: int):
        self.Max = Max
        self.stack = [None] * Max
        for i in range(len(array)):
            self.stack[i] = array[i]
        self.top = len(array) - 1
        print(f"Stack is created with {self.Max} data => {self.stack}")
    
    def pop(self):
        def isEmpty():
            return self.top == -1
        
        if not isEmpty():
            popped = self.stack[self.top]
            self.stack[self.top] = None 
            self.top -= 1
            print(f"Popped: {popped}")
        else:
            print("Stack is Empty")
    
    def push(self, value):
        def isFull():
            return self.top == self.Max - 1
        
        if isFull():
            print("The Stack Reached Its Limit")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"Pushed: {value}")
    
    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print(f"Peek element in the stack: {self.stack[self.top]}")
    
    def display(self):
        print(f"Stack limit: [{self.Max}] data => {self.stack}")

stack = Stack()
stack.create([10, 20], 5)
stack.display()
stack.push(30)
stack.pop()
stack.peek()
stack.display()
