#!/usr/bin/python
import socket
addr = ('127.0.0.1',5000)
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.sendto('hello world',addr)
strrecv,addr = udp.recvfrom(1024)
print strrecv
udp.close()
