#!/usr/bin/env python3
import sys

arglist = sys.argv[1:]
list1=[]
list2=[]
for arg in arglist:
    str_len = len(arg)
    if str_len <= 3:
        list1.append(arg)
    elif str_len >3:
        list2.append(arg)
print(' '.join(list1))
print(' '.join(list2))
