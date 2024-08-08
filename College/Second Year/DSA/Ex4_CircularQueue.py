class Queue:
    def __init__(self, size: int):
        self.front = self.rear = -1
        self.size = size
        self.queue = [None] * self.size

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, value):
        if not self.isFull():
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
        else:
            print("Queue Overflow")

    def dequeue(self):
        if not self.isEmpty():
            x = self.queue[self.front]
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return x
        else:
            print("Queue Underflow")
            return None

    def display(self):
        print(f"Front: {self.front}, Rear: {self.rear}")
        if self.isEmpty():
            print("Queue is empty")
        else:
            if self.rear >= self.front:
                print("Queue:", self.queue[self.front:self.rear + 1])
            else:
                print("Queue:", self.queue[self.front:self.size] + self.queue[0:self.rear + 1])


instance = Queue(size=8)
while True:
    choice = int(input("\nCircular Queue Menu:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\nEnter your choice: "))
    if choice == 1:
        value = input("Enter the value: ")
        instance.enqueue(value)
        print("Enqueued:", value)
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