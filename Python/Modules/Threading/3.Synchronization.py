from threading import *
class Table:
    def printTable(self,number):
        for i in range(1,11):
            print(number,'X',i,'=',number*i)
        print('Table for ',number,' is completed')

class MyThread(Thread):
    def __init__(self,tableobj,number):
        super().__init__()
        self.tableobj=tableobj
        self.number=number
        self.lock=Lock()
    def run(self):
        threadlock.acquire() #synchronization
        self.tableobj.printTable(self.number)
        threadlock.release()

threadlock=Lock()
tableobj=Table()
t1=MyThread(tableobj,5)
t2=MyThread(tableobj,10)
t1.start()
t2.start()