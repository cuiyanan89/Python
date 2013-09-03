import os
import re
import time
import sys

lifeline = re.compile(r"(\d) received")
report = ("No response","Partial Response","Alive")

print time.ctime()

for host in range(60,70):
    ip = "192.168.200."+str(host)
    pingaling = os.popen("ping -q -c2"+ip,'r')
    print "Testing",ip,
    sys.stdout.flush()
    while 1:
        line = pingaling.readline()
        if not line:
            break
        igot = re.findall(lifeline,line)
        if igot:
            print report[int(igot[0])]
print time.ctime()
