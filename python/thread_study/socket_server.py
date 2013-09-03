#!/usr/bin/python

import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',5300))
s.listen(10)
conn,addr = s.accept()
print 'get connection from ',addr

def server_say(conn):
    while True:
        say = raw_input()
        print 'say'
        conn.send('server>>>'+say)
def server_listen(conn):
    while True:
        hear = conn.recv(1024)
        print hear
threads = []
threads.append(threading.Thread(target=server_say,args=(conn,)))
threads.append(threading.Thread(target=server_listen,args=(conn,)))
threads[0].start()
threads[1].start()
threads[0].join()
threads[1].join()
    
conn.close()
