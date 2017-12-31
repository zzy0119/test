# -*- coding:utf-8 -*-

def add(x, y):
    return x + y


print(reduce(add, [1,2,3,4,5]))


# 如果要把序列[1, 3, 5, 7, 9]变换成整数13579
def fun(x, y):
    return x * 10 + y


print(reduce(fun, [1, 3, 5, 7, 9]))


# 将str转换为int
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fun, map(char2num, '13579')))


# 进一步简化str2int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fun, map(char2num, s))


print(str2int('1987'))





