from threading import Thread,currentThread
import time
def display(st,end):
    for i in range(st,end,2):
        time.sleep(0.5)
        print(i)
        time.sleep(0.5)
        
odd=Thread(target=display,args = (1,100),name ="Odd")
even=Thread(target=display,args = (2,100),name ="Even")
odd.start()
time.sleep(0.5)
even.start()
