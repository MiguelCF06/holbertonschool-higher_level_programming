#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numMul = 0
        numSum = 0
        for tuple in my_list:
            numMul += (tuple[0] * tuple[1])
            numSum += tuple[1]
        return (numMul / numSum)
    return 0
