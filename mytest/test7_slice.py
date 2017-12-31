#-*- coding:utf-8 -*-

L = ['Reala', 'Reason', 'Jasper', 'Eve', 'Denil']

print(L[0:3])

L = list(range(100))
print(L)

#取得列表的最后两个
print(L[-2:])
#取得列表的最后一个
print(L[-2])
print(L[-2:-1])


#取前十个 每两个取一个
print(L[:10:2])

#定义一个函数，去除字符串的收尾空格
def delspace(str):
    while str[:1] == ' ':
        str = str[1:]
    while str[-1] == ' ':
        str = str[:-1]
    return str


print(delspace('   hello world    '))


