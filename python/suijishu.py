#!/usr/bin/python
import random
def suiji_4():
    return random.sample([chr(i) for i in range(ord('a'),ord('z')+1)+range(ord('A'),ord('Z')+1)]+range(0,10),4)

def suiji_1():
    return random.choice([chr(i) for i in range(ord('a'),ord('z')+1)+range(ord('A'),ord('Z')+1)]+range(0,10))

if __name__ == '__main__':
    print suiji_4()
    print suiji_1()
