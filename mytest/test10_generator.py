# -*- coding:utf-8 -*-

L = [x * x for x in range(10)]

print(type(L))

# 生成器
g = (x * x for x in range(10))
print(type(g))
for n in g:
    print(n)


# 斐波那契数列
def f(nn):
    t, a, b = 0, 0, 1
    while t < nn:
        print(b)
        a, b = b, a + b
        t = t + 1
    return None


print(f(6))


# yield 生成器
def f_g(num):
    t, a, b = 0, 0, 1
    while t < num:
        yield b
        a, b = b, a + b
        t = t + 1


for g in f_g(6):
    print(g)


# 打印杨辉三角
def triangles():
    my_list = [1]
    tmp_list = []
    while True:
        yield my_list
        # 列表增加一个元素
        my_list.append(0)
        # print(len(my_list))
        for x in range(len(my_list)):
            tmp_list.append(my_list[x-1] + my_list[x])
        my_list = tmp_list
        tmp_list = []

n = 0
for x in triangles():
    print(x)
    n = n + 1
    if n == 10:
        break





