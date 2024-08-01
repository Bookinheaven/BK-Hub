print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")
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
while True:
    print("\nMenu:")
    print("1. Create Stack")
    print("2. Push Element")
    print("3. Pop Element")
    print("4. Peek Element")
    print("5. Display Stack")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        array = list(map(int, input("Enter elements to initialize the stack (space-separated): ").split()))
        Max = int(input("Enter the maximum size of the stack: "))
        stack.create(array, Max)
    
    elif choice == 2:
        value = int(input("Enter the value to push onto the stack: "))
        stack.push(value)
    
    elif choice == 3:
        stack.pop()
    
    elif choice == 4:
        stack.peek()
    
    elif choice == 5:
        stack.display()
    
    elif choice == 6:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.")