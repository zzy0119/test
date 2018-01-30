# -*- coding:utf-8 -*-


class Student:
    pass


bart = Student()
bart.name = 'zhangzongyan'


print(bart.name)


# 属性名字前加__ 私有变量
class TestStudent:
    def __init__(self, name, score): # __init__第一个参数永远都是self
        self.__name = name
        self.__score = score

    def print_it(self):
        print("%s %d" % (self.__name, self.__score))
    def get_name(self):
        return self.__name


ts = TestStudent('liruizhong', 100)
ts.print_it()
print(ts.get_name())


