from threading import Thread, currentThread
from time import sleep

class mythread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        for i in range(1, 6):
            print(i)
            sleep(1)
t1 = mythread()
t1.setName("BK")
t1.start()
print(currentThread().getName())
