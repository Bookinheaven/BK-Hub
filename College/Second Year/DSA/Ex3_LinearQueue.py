class Queue:
    def __init__(self, size: int):
        self.front = self.rear = -1
        self.size = size
        self.queue = [None] * self.size

    def isFull(self):
        return self.rear == self.size - 1

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, value):
        if not self.isFull():
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value
            print("Enqueued:", value)
        else:
            print("Queue Overflow")

    def dequeue(self):
        if not self.isEmpty():
            x = self.queue[self.front]
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
            return x
        else:
            print("Queue Underflow")
            return None

    def display(self):
        print(f"Front: {self.front}, Rear: {self.rear}")
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue:", self.queue[self.front:self.rear + 1])

instance = Queue(size=8)
while True:
    choice = int(input("\nLinear Queue Menu:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\nEnter your choice: "))
    if choice == 1:
        value = input("Enter the value: ")
        instance.enqueue(value)
        
    elif choice == 2:
        x = instance.dequeue()
        if x is not None:
            print("Dequeued:", x)
    elif choice == 3:
        instance.display()
    elif choice == 4:
        print("Back")
        break
    else:
        print("Invalid choice")