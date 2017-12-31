# -*- coding:utf-8 -*-
import functools


# functools.partial创建一个偏函数
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
# 转换二进制int('100010', base=2) 偏函数使得转换二进制时不需要再传base=2
int2 = functools.partial(int, base=2)


print (int2('100'))


