#!/usr/bin/python
import socket
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.bind(('127.0.0.1',5000))
str,addr = udp.recvfrom(1024)
print str
udp.sendto('i love my country',addr)
udp.close()

