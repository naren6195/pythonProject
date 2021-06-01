from time import sleep
from threading import *

class Helllo(Thread):
    def run(self):
        for i in range(100):
            print("Hello",i)
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(100):
            print(i)
            sleep(1)


o1=Helllo()
o2=Hi()

o1.start()
sleep(0.2)
o2.start()

o1.join()
o2.join()

print("The End :)")