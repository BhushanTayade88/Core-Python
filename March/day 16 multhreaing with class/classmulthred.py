from threading import Thread
import time
class Testing(Thread):
    
    def __init__(self,st,end):
         super().__init__()
         self.st=st
         self.end=end

    def run(self):
        for i in range(self.st,self.end,2):
            time.sleep(0.5)
            print(i)
            time.sleep(0.5)
odd = Testing(1,100)
even = Testing(2,100)

odd.start()
time.sleep(0.5)
even.start()
