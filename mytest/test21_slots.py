# -*- coding:utf-8 -*-


class Student(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称


s = Student()
s.name = 'Michael'
s.age = 18

