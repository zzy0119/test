# -*- coding:utf-8 -*-


def f(x):
    return x * x


r = map(f, [1,2,3,4,5,6])
print(list(r))

r = map(str, [1,2,3,4,5,6])
print(list(r))