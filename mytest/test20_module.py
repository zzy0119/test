# -*- coding:utf-8 -*-

#表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
' a test module'

__author__ = 'reala'

#模块的自动导入 file-->default setting--->auto import---->show import popup
import sys
import numpy

def test():
    args = sys.argv
    if len(args) == 1:
       print('there are one argument')
    elif len(args) == 2:
        print('hello %s' % args[1])
    else:
        print('too many arguments')


if __name__ == '__main__':
    test()

