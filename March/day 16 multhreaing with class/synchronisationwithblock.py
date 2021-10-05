from threading import Thread,Lock

def Display(msg,lock):
    with lock:
        print("[")
        print(msg)
        print("]")
        
lock = Lock()
t1 = Thread(target = Display,args =("Python",lock))
t2 = Thread(target = Display,args = ("Classes",lock))
t1.start()
t2.start()
