
class Queue:
    def __init__(self, option: str, size: int):
        self.front = self.rear = -1
        self.size = size
        self.queue = [None]*self.size
        self.option = option.lower().strip()
    def enqueue(self, value):
        def isFull():
            if self.option == "linear":
                return self.rear == self.size - 1
            elif self.option == "circular":
                return (self.rear + 1) % self.size == self.front

        if not isFull():
            if self.front == -1: self.front = 0
            if self.option == "linear":
                self.rear += 1
            elif self.option == "circular":
                self.rear = (self.rear+1 ) % self.size
            self.queue[self.rear] = value
        else:
            print("Queue Overflow")
    
    def isEmpty(self):
            return self.front == -1
    def dequeue(self):
        
        if not self.isEmpty():
            x = self.queue[self.front]
            self.queue[self.front] = None
            if self.rear == self.front:
                self.front = self.rear = -1
            else:
                if self.option == "linear":
                    self.front +=1
                elif self.option == "circular":
                    self.front = (self.front+1 ) % self.size
            return x
        else:
            print("Queue Underflow")
            
    def display(self):
        print(f"Front: {self.front}, Rear: {self.rear}")
        if self.isEmpty():
            print("Queue is empty")
        else:
            if self.option == "linear" or (self.option == "circular" and self.rear >= self.front):
                print("Queue:", self.queue[self.front:self.rear + 1])
            else:
                print("Queue:", self.queue[self.front:self.size] + self.queue[0:self.rear + 1])


def menu(queueType):
    instance = Queue(option=queueType, size=8)
    while True:
        choice = int(input(f"\n{queueType} Queue Menu:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\nEnter your choice: "))
        if choice == 1:
            value = input("Enter the value: ")
            instance.enqueue(value)
            print("Enqueued:", value)
        elif choice == 2:
            x = instance.dequeue()
            print("Dequeued:", x)
        elif choice == 3:
            instance.display()
        elif choice == 4:
            print("Back")
            break
        else:
            print("Invalid choice")

while True:
    choice = int(input("\nMenu:\n1. Linear Queue\n2. Circular Queue\n3. Exit\nEnter your choice: "))
    if choice == 1:
        menu("Linear")
    elif choice == 2:
        menu("Circular")
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
