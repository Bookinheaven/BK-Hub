from threading  import Thread

class mythread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        print(self.getName())
        print("Hello World")
t1 = mythread()
t1.setName('BK0001')
t1.start()