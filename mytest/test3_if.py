#-*- coding:utf-8 -*-
age = 8
if age > 18:
    print('your age is', age)
    print('adult')
elif age > 6:
    print('teenager')
else:
    print('kid')

a = input('births:')
birth = int(a)
if a > 2000:
    print('00后')
else:
    print('00前')