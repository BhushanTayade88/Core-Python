from threading import Thread
import time
def odd_disp():
    for i in range(1,100,2):
        time.sleep(0.5)
        print(i)
        
def even_disp():
    for i in range(2,100,2):
        time.sleep(0.5)
        print(i)
        
t1 = Thread(target=odd_disp)
t2 = Thread(target=even_disp)
t1.start()
time.sleep(0.5)
t2.start()

