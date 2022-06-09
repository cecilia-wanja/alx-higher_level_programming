#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        res = 0
        res2 = 0
        for x, y in my_list:
            res += x * y
            res2 += y
        return (res / res2)
