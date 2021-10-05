from threading import Thread
import time

class MyThread(Thread):
    def run(self):
        for i in range(1,100,2):
            time.sleep(0.5)
            print(i)
            time.sleep(0.5)

for x in range(5):
    print("Statrt--main ---Thread")
t1 = MyThread()
t1.start()
t1.join()#t1.join(1)
for x in range(10):
    print("End of--main---Thread")
