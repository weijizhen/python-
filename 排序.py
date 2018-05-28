#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2018/5/18 22:15
#@Author    :weijizhen
#@File      :排序.py
import random
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i -1):
            if li[j] > li[j +1]:
                li[j],li[j+1] = li[j+1],li[j]

def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]

data = list(range(10))
random.shuffle(data)
select_sort(data)
#bubble_sort(data)
print(data)