#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2018/5/1 15:36
#@Author    :weijizhen
#@File      :筛选数据.py
from random import randint
'''
筛选列表
'''
        # import  time
        # """
        # 如何在列表，字典，集合中根据条件筛选数据
        # """
        # '''
        # filter（）函数
        # '''
        # stati_cmethod = time.time()
        # from random import randint#导入random库中的randint方法
        # data = [randint(-10,10) for _  in  range(10)]#随机-10到10之间的数，然后迭代10个打印出来赋值个data
        # k =(list (filter(lambda x: x >=0, data)))####在python2.X中filter函数输出的是列表，在python3X中输出的是对象。用list（）函数将其转换成列表
        # enum_erate = time.time()
        # print(k,enum_erate - stati_cmethod)
        # '''
        # 列表解析
        # '''
        # static_method = time.time()
        # l = [x for x in data if x >=0]
        # enumer_ate = time.time()
        # print(l,enumer_ate - static_method)
        # """
        # 运用time（）函数来准确判断两个筛选方法的速度
        # """
'''
筛选字典
'''
        # d = {x:randint(60,100) for x in range(1,21)}#字典 x：y 随机 x 的值是1到20，y的值是60到100。整个字典传给 d
        # print(d)
        #
        # l ={k:v for  k ,v in d.items() if v > 90}#迭代 字典键值k：v，调用items（），判断v的值是否大于90
        # print(l)

'''
筛选集合
'''
    # s = set(range(-5,10))#set 将列表转换为集合
    # d ={i  for i in s if i % 3 == 0}#迭代 s 集合，i 判断取余为3
    # print(d)
'''
元组命名
'''
#元组
    # from collections import namedtuple  #给引索定义下标
    # Student = namedtuple('Student',['name','age','sex','email'])
    # s = Student('Jim',16,'male','jim785400')#元组不可变
    # #Student(name='Jim', age=16, sex='male', email='jim785400')
    # print(s)
