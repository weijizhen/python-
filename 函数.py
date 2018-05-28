#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2018/5/22 14:45
#@Author    :weijizhen
#@File      :函数.py
import re
'''
元组不可变
'''
    # num = (11,22,33)
    # print(num[0])
'''
break 结束循环
return 结束函数,函数运行到return会结束
'''
    # def re_q(a,b):
    #     c = a+b
    #     print('%d+%d=%d'%(a,b,c))
    #     return c
    # def get_re(q):#这里需要设置一个参数，接受get_re（d）
    #     m  = q+10
    #     a= 1
    #     b=2
    #     c=3
    #     return (m,a,b,c)#这是元组，小括号
    # def main():
    #     # num = int(input(''))
    #     # unm1 = int(input(''))
    #     #d = re_q(num, unm1)  # c的值已经通过return返回给了函数re _q，然后将值传给d，以便于get_re函数使用。这里d是全局变量
    #     i = get_re(10)
    #     print(i)
    #
    # if __name__ == '__main__':
    #      main()
'''
函数嵌套，重复使用函数
'''
    # def prin_ilne():
    #     print('*'*50)
    # def print_1():
    #     i = 0
    #     while i<5:
    #         prin_ilne() #while 每次循环，调用一次print_ilen（）
    #         i+=1
    #         #i = i+1
    # def main():
    #     print_1()
    # if __name__ == '__main__':
    #     main()
'''
嵌套函数，形参，实参的概念
'''
    # def get_imput(a,b,c):#形参
    #     result = a + b + c#result 接受三个数相加的值
    #     return result#get_imput 获得一个return返回的值
    #     #print(a,b,c)
    # def get_1(q,w,e):#形参
    #     result1 = get_imput(q,w,e)#实参    get_imput（）承接了三个数相加
    #     result1/=3
    #     print('%d'%(result1 * 2))
    # def main():
    #     p = 1
    #     m = 1
    #     d = 2
    #     get_1(p,m,d)#实参  将值传给get_imut（）
    # if __name__ == '__main__':
    #     main()
'''
全局变量，局部变量
'''
# s =100
# def one_program():
#     print('s =%d'%s)
# def two_program():
#     s = 10
#     print('s = %d'%s)
# one_program()
# two_program()
'''
装饰器的简单运用，装饰器的 表示符号@。相当于高级闭包
装饰器的作用就是为已经存在的对象在 不影响其运行功能下 添加额外的功能。
'''
# from time import ctime,sleep
# def tsfunc(func):
#       def wrappedFunc():
#           print('[%s] %s() called' % (ctime(),func.__name__))
#           return func()
#       return  wrappedFunc#这里是返回值 引用wrappedFunc，而不是调用wrappedFunc()。既有返回值就不能有调用
# @tsfunc
# def foo():
#     pass
# foo()
# sleep(4)
# for i in range(2):
#     sleep(1)
#     foo()
'''
菲波那切数列 函数
'''
    # def fibs(n):
    #     result = [0,1]
    #     for i in range(n-2):#range()函数打印整数列表，随机函数需要导入 import random 模块
    #         result.append(result[-2] + result[-1])#每次两个数相加
    #     return result
    # if __name__ == '__main__':
    #     lst = fibs(10)
    #     print(lst)
'''
使用global语句可以清楚地表明变量是在外面的块定义的全局变量
列表，字典 可以不用global。
'''
    # a =1
    # def get_global():#不使用global a ，a+=1运行出错，因为有两个a，一个是全局变量，一个是局部变量
    #     global  a
    #     a+=1
    #     print(a)
    # def get_global2():#这里a 已经是2了
    #     i=1
    #     b = i+a
    #     print(b)
    # def main():
    #     get_global()
    #     get_global2()
    # if __name__ == '__main__':
    #     main()
'''
return 返回多个值
'''
    # def deic(a,d):
    #     shang = a/d
    #     yushu = a%d
    #     return shang,yushu #这里返回的是一个元组，加上[]或者{}则返回列表或者字典
'''

'''