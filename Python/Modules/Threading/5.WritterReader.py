# Inter Tread Communication
from threading import Thread, Condition
import time

class Buffer():
    def __init__(self):
        self.data = None
    def write(self,data):
        cv.acquire()
        self.data=data
        print('writer',self.data)
        cv.notify()
        cv.wait()
        cv.release()
    def read(self,data):
        cv.acquire()
        self.data=data
        print('reader',self.data)
        cv.notify()
        cv.wait()
        cv.release()

class Writer(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        for i in range(1, 6):
            self.buffer.write(i)
            time.sleep(1)  

class Reader(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        for i in range(1, 6):
            self.buffer.read(i)
            time.sleep(1) 

cv = Condition()
buffer = Buffer()
writer = Writer(buffer)
reader = Reader(buffer)

writer.start()
reader.start()

writer.join()
reader.join()
