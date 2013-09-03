#!/usr/bin/python
import threading
import socket

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect(('127.0.0.1',5300))

def clent_say(conn):
    while True:
        say = raw_input()
        conn.send('clent>>>'+say)

def clent_listen(conn):
    while True:
        hear = conn.recv(1024)
        print hear

threads = []
threads.append(threading.Thread(target=clent_say,args=(conn,)))
threads.append(threading.Thread(target=clent_listen,args=(conn,)))
threads[0].start()
threads[1].start()
threads[0].join()
threads[1].join()
conn.close()
