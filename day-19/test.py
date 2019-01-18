#!/usr/bin/env python

import math

def fun(regs):
    regs[2] += 2
    regs[2] *= regs[2]
    regs[2] *= 19
    regs[2] *= 11
    regs[4] += 8
    regs[4] *= 22
    regs[4] += 20
    regs[2] += regs[4]
    if regs[0] != 0:
        if regs[0] >= 10:
            return regs
        if regs[0] <= 1:
            regs[4] = 27
        if regs[0] <= 2:
            regs[4] *= 28
        if regs[0] <= 3:
            regs[4] += 29
        if regs[0] <= 4:
            regs[4] *= 30
        if regs[0] <= 5:
            regs[4] *= 14
        if regs[0] <= 6:
            regs[4] *= 32
        if regs[0] <= 7:
            regs[2] += regs[4]
        if regs[0] <= 8:
            regs[0] = 0
    regs[0] += 1 + regs[2]
    for d in range(2, 1 + int(math.sqrt(regs[2]))):
        if regs[2] % d == 0:
            regs[0] += d
            od = regs[2] // d
            if od != d:
                regs[0] += od
    regs[1] = 1 + regs[2]
    regs[3] = 1 + regs[2]
    regs[4] = 1
    return regs
# fun([0, 0, 0, 0, 0]) == [2640, 1033, 1032, 1033, 1]
# fun([7, 0, 0, 0, 0]) == [2156, 1229, 1228, 1229, 1]
# fun([8, 0, 0, 0, 0]) == [2640, 1033, 1032, 1033, 1]
print(fun([0, 0, 0, 0, 0]))
print(fun([7, 0, 0, 0, 0]))
print(fun([8, 0, 0, 0, 0]))
print(fun([1, 0, 0, 0, 0]))
