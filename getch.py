#!/usr/bin/python
import termios,sys,os
TERMIOS=termios
def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] &~TERMIOS.ICANON &~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd,TERMIOS.TCSANOW,new)
    c = None
    try:
        c = os.read(fd,1)
    finally:
        termios.tcsetattr(fd,TERMIOS.TCSAFLUSH,old)
    return c
if __name__=='__main__':
    print 'Enter something'
    while True:
        c = getch()
        if c =='q':
            break
        else:
            print 'Entered',c
