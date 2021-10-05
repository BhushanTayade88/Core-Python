from threading import Thread
def odd_disp():
    for i in range(1,100,2):
        print(i)
def even_disp():
    for i in range(2,100,2):
        print(i)
t1 = Thread(target=odd_disp)
t2 = Thread(target=even_disp)
t1.start()
t2.start()

