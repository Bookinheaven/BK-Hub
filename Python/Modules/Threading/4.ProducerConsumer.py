# # Inter Tread Communication
# from threading import *
# class Buffer():
#     def put(self,data):
#         cv.acquire()
#         self.data=data
#         print('Producer',self.data)
#         cv.notify()
#         cv.wait()
#         cv.release()
#     def take(self,data):
#         cv.acquire()
#         self.data=data
#         print('Consumer',self.data)
#         cv.notify()
#         cv.wait()
#         cv.release()
        
# class producer(Thread):
#     def __init__(self,bufferobj):
#         Thread.__init__(self)
#         self.bufferobj=bufferobj
#     def run(self):
#         for i in range(1,6):
#             self.bufferobj.put(i)
# class consumer(Thread):
#     def __init__(self,bufferobj):
#         Thread.__init__(self)
#         self.bufferobj=bufferobj
#     def run(self):
#         for i in range(1,6):
#             self.bufferobj.take(i)
# cv=Condition()
# bufferobj=Buffer()
# p=producer(bufferobj)
# p.start()
# c=consumer(bufferobj)
# c.start()

from threading import Thread, Condition

class Buffer:
    def put(self, data):
        locker.acquire()
        self.data = data
        print(f"Writer {self.data}")
        locker.notify()
        locker.wait()
        locker.release()
    def get(self):
        locker.acquire()
        print(f"Reader {self.data}")
        locker.notify()
        locker.wait()
        locker.release()
class Producer(Thread):
    def __init__(self, bufferobg):
        Thread.__init__(self)
        self.buffer = bufferobg
    def run(self):
        for x in range(1,6):
            self.buffer.put(x)
    
class Consumer(Thread):
    def __init__(self, bufferobg):
        Thread.__init__(self)
        self.buffer = bufferobg
    def run(self):
        for x in range(1,6):
            self.buffer.get(  )

locker = Condition()
bufferobg = Buffer()
p1 = Producer(bufferobg)
p1.start()
c1 = Consumer(bufferobg)
c1.start()
    

        
