# -*- coding:utf-8 -*-


# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#def now():
 #   print("2018-1-1")


#f = now
#f()


# 装饰器就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 等效于now = log(now)
@log
def now():
    print('hello world')


now()
