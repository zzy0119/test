#-*- coding:utf-8 -*-
#用迭代的方式求得List中的最大最小值
def findmaxandmin(L):
    if len(L)==0:
        return None, None
    min = L[0]
    max = L[0]
    for x in L:
        if min > x:
            min = x
        if max < x:
            max = x
    return max, min

li=[1,2,3,4,5,6,7,8]
print(findmaxandmin(li))



