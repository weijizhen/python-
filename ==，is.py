#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2018/5/27 16:16
#@Author    :weijizhen
#@File      :==，is.py
'''
is	是⽐较两个引⽤是否指向了同⼀个对象（引⽤⽐较）。
 ==	是⽐较两个对象是否相等。
'''
    # a=[1,2,2]
    # b=[0,1,1]
    # print(a==b)
    # print(a is b)
'''
深拷⻉、浅拷⻉
浅拷贝：是对于一个对象的顶层拷贝
          拷贝了引用，并没有拷贝内容
深拷贝：是对于一个对象所有层次的拷贝
'''
    # import copy#导入深拷贝的模块
    # a=[1,2,3,3]
    # c=a
    # b=copy.deepcopy(a)#深拷贝
    # print(id(a),id(c),id(b))#a，c，b的内存地址，a，c一样浅拷贝。b是深拷贝
import copy
a = [1,1,2,1]
b = [1,5,8,9]
c = a,b #class tuple 元组
e=copy.copy(c)#copy.copy全拷贝用于元组,内存地址相同。如果用列表就内存不是一样
print(id(e),id(c))
a.append(444)
print(a)
print(e)