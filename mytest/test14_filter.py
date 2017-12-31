# -*- coding:utf-8 -*-


def odd(n):
    return  n % 2 == 0


#去除所有的奇数
print(filter(odd, [1,2,3,4,5,6,7,8,9,10]))

