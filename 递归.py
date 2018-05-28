#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2018/5/3 11:16
#@Author    :weijizhen
#@File      :递归.py
"""
递归函数
一个函数内调用另一个函数
一个函数调用自身
"""
    # def fun1():
    #     print("this is fun1")
    #     fun2()
    #
    # def fun2():
    #     print("this is fun2")
    #
    # fun1()
###############################################
"""
阶乘 n!=1*2*3.....*n
"""
    # def fun(n):
    #     if n==1:
    #         return 1
    #     return  n*fun(n - 1)
    # sum = fun(5)
    # print(sum)
###############################################
"""
while循环
"""
    # mylist = [10,1,2,3,5,9]
    # while mylist:
    #     print(mylist[0])
    #     mylist.pop(0)
###############################################
"""
递归的特性
可以解决 for循环，while 循环难以解决的问题
切记一定要有返回条件
用断点可以清晰的看见，递归的运行轨迹
"""
    # num = 5
    # def func(a):
    #     if a<6:
    #         a+=1
    #         print("hello")
    #         return func(a)
    #     else:
    #         return  0
    # res = func(num)
###############################################
'''
解决复杂的列表迭代
'''
    # mylist=[1,2,3,[4,5,6],[7,8,9,[71,64,454,44]]]
    # def func(obj):
    #     for var in obj:
    #         if 'list' in str(type(var)):##这里是判断条件，用type来判断是不是列表，
    #             func(var)
    #         else:
    #             print(var)
    # func(mylist)
###############################################
'''

'''
                                                                                                                                 
