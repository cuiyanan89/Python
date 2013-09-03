#!/usr/bin/python
import time
if __name__ == '__main__':
    time.sleep(1)
    print 'clock1:%s'%time.clock()
    print 'time1:%s'%time.time()
    time.sleep(1)
    print 'clock2:%s'%time.clock()
    print 'time2:%s'%time.time()
    time.sleep(1)
    print 'clock3:%s'%time.clock()
    print 'time3:%s'%time.time()
