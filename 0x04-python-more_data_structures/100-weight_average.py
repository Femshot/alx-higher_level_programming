#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    avg = 0
    if my_list:
        for tup in my_list:
            x, y = tup
            res += x * y
            avg += y
    return (res / avg)
