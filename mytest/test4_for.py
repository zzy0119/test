#-*- coding:utf-8 -*-

names=['Maichael', 'Zhangzongyan', 'Liruizhong', 'Reala']

for name in names:
    print(name)

sum = 0
for i in [1,2,3,4,5,6,7,8,9]:
    sum += i
print(sum)

sum = 0
for i in range(101):
    sum += i
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)