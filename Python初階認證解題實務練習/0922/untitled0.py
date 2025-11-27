# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:45:31 2022

@author: sunny
"""
# print(a, end = ' # ')
# print(b, end = ' # ')
# print(c)

name="洪琪媛"
print(name, end = ' # ')
print(name, end = ' # ')


height=155
weight=53
print(format(height,"5d"))
print(format(weight,">6d"))

height_1=555
weight_1=55


height_1=int(input('請輸入身高:'))
weight_1=int(input("輸入體重:"))
height_1=height_1 / 100
bmi = weight_1/(height_1*height_1)
print('bmi為:',format(bmi,'6.2f'))