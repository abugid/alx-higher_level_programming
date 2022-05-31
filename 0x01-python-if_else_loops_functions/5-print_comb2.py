#!/usr/bin/python3
pre_num = "0"
for i in range(100):
    if i == 10:
        pre_num = ""
    if i != 99:
        print("{}{}".format(pre_num, i), end=", ")
    else:
        print("{}".format(i))
