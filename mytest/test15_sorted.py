# -*- coding:utf-8 -*-


L = sorted([-21, 15, -2, 80, 50], key = abs)
print(L)


L = ['hello', "Hello", "world", "Zhang"]
print(sorted(L, key = str.lower, reverse = True))


# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()

# t是元祖
def by_score(t):
    return t[1]


print(sorted(L, key = by_name))
print(sorted(L, key = by_score))