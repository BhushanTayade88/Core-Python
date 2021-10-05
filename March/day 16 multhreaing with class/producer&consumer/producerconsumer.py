from threading import Thread,Condition
import time
flag = True
value = 0

def produce(i,cond):
    global flag
    global value
    with cond:
        if flag==True:
            value = i
            print("producer produce--",value)
            flag = False
            cond.notify()
        else:
            cond.wait()
def consume(cond):
    global flag
    with cond:
        if flag==True:
            cond.wait()
        flag=True
        cond.notify()
        return value

def producer_thread(cond):
    i=1
    while True:
        produce(i,cond)
        i=i+1
        time.sleep(1)
def consumer_thread(cond):
    while True:
        val = consume(cond)
        print("consumer consume --",val)
        time.sleep(1)

c = Condition()
t1 = Thread(target = producer_thread,args=(c,))
t2 = Thread(target = consumer_thread,args=(c,))
t1.start()
t2.start()
