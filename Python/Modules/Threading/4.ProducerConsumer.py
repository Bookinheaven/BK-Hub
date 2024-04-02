from threading import *
class Buffer():
    def put(self,data):
        cv.acquire()
        self.data=data
        print('Producer',self.data)
        cv.notify()
        cv.wait()
        cv.release()
    def take(self,data):
        cv.acquire()
        self.data=data
        print('Consumer',self.data)
        cv.notify()
        cv.wait()
        cv.release()
        
class producer(Thread):
    def __init__(self,bufferobj):
        Thread.__init__(self)
        self.bufferobj=bufferobj
    def run(self):
        for i in range(1,6):
            self.bufferobj.put(i)
class consumer(Thread):
    def __init__(self,bufferobj):
        Thread.__init__(self)
        self.bufferobj=bufferobj
    def run(self):
        for i in range(1,6):
            self.bufferobj.take(i)
cv=Condition()
bufferobj=Buffer()
p=producer(bufferobj)
p.start()
c=consumer(bufferobj)
c.start()