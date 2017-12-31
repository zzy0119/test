#-*- coding:utf-8 -*-

def my_febonacii(n):
    if n == 1 :
        return 1
    if n == 2:
        return 1
    return my_febonacii(n-1)+my_febonacii(n-2)

print(my_febonacii(10))