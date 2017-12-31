# -*- coding:utf-8 -*-


def fun(x):
    return x * x


f = lambda x:x * x


print(f(6))


# lambda匿名函数 优势1防止函数名重复
print(list(map(lambda x:x * x, [1, 2, 3, 4, 5])))
