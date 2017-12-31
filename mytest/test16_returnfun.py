# -*- coding:utf-8 -*-


def calc_num(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


def lazy_sum(*args):
    def sumall():
        sum = 0
        for n in args:
            sum += n
        return sum
    return sumall

f = lazy_sum(1,3,5,7,9)
print(f())
