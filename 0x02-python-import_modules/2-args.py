#!/usr/bin/python3
import sys

n = len(sys.argv)

if n == 2:
    print("1 argument:")
elif n == 1:
    print("0 arguments:")
else:
    print("{} arguments:".format(n))
for i in range(1, n):
    print("{}: {}".format(i, sys.argv[i]))