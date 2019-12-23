#!/usr/bin/env python3

from subprocess import *

def checktree():
    cmd = "ps -ef |grep xmastree.py |grep python3|grep -v grep |awk {'print $2'}"
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    if(output == b''):
        return False
    else:
         return True

if __name__ == '__main__':
    if(checktree()):
        print("1")
    else:
        print("0")


