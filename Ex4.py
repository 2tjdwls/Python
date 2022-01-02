# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:12:57 2021

@author: tjdwl
"""

#%%
a = ['But soft what light through yonder window breaks\n', 'It is the east and Juliet is the sun\n' , 'Arise fair sun and kill the envious moon\n', 'Who is already sick and pale with grief']
lst = list()
b = a[0]
c = b.split(' ')
print(c)
    lst.append(f)
lst.sort()
print(lst)
a = { 'a' : 0, 'b' : 20, 'c' : 30}
print(a.attend('d',5))
#%%
import os
os.chdir("C:\Python\Coursera")

path = os.getcwd()
print(path)
#%%
import re

with open('Q1.txt','r') as file :
    x = file.read()

y = list()

n = re.findall('\d+',x)
y.extend(n)

sum = 0
for a in y :
    sum += int(a)
    
print(sum)
#%%
git init