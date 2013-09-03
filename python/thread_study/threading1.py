#!/usr/bin/python
import threading
from time import ctime,sleep

class MyThread(threading.Thread):
    def __init__(self,n_loop,n_time):
        threading.Thread.__init__(self)
        self.n_loop = n_loop
        self.n_time = n_time
    def run(self):
        print '%s begin at %s'%(self.n_loop,ctime())
        sleep(self.n_time)
        print '%s end at %s'%(self.n_loop,ctime())

def main():
    loops = [5,2,5,7,8,6,9,10]
    threads = []
    loop = xrange(len(loops))
    for i in loop:
        threads.append(MyThread(i,loops[i]))
    for i in loop:
        threads[i].start()
    for i in loop:
        threads[i].join()
if __name__=='__main__':
    main()
