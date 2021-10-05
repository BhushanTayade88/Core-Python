from threading import Thread,Lock

def display(msg,lock):
    lock.acquire()
    print("[")
    print(msg)
    print("]")
    lock.release()
lock = Lock()
t1 = Thread(target = display,args =("Python",lock))
t2 = Thread(target = display,args = ("Classes",lock))
t1.start()
t2.start()
