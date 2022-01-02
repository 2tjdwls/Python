#%%
def trace(func) :
    def wrapper() :
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper


def hello() :
    print('hello')
    
def world() :
    print('world')
    

trace_hello = trace(hello)
trace_hello()
trace_world = trace(world)
trace_world()
#%%
def trace(x) :
    def wrapper() :
        x()
        print(x.__name__, 'World')
    return wrapper

def hello() :
    print('Hello World')
    
a = trace(hello)
a()
#%%
def trace(func) :
    def wrapper() :
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper

@trace
def hello() :
    print('world')
    
@trace
def world() :
    print('world')
    
hello()
world()
#%%
def abcd(func) :
    def wrapper() :
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper

@abcd
def hello() :
    print('world')
    
@abcd
def world() :
    print('world')
    
hello()
world()
#%%
def trace(func) :
    def wrapper(a, b) :
        r = func(a, b)
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))
        
        return r
    return wrapper

@trace
def add(a, b) :
    return a + b

print(add(10, 20))
#%%
def trace(func) :
    def wrapper(*args, **kwargs) :
        r = func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
        
        return r
    return wrapper

@trace
def get_max(*args) :
    return max(args)

@trace
def get_min(**kwargs) :
    return min(kwargs.values())

print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))
#%%
def is_multiple(x) :
    def real_decorator(func) :
        def wrapper(a, b) :
            r = func(a, b)
            if r % x == 0 :
                print('{0}의 반환값은 {1}의 배수입니다'.format(func.__name__, x))
            else :
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator

@is_multiple(3)
def add(a, b):
    return a + b

print(add(10, 20))
print(add(2, 5))
#%%
class Trace :
    def __init__(self, func) :
        self.func = func
        
    def __call__(self) :
        print(self.func.__name__, '함수 시작')
        self.func()
        print(self.func.__name__, '함수 끝')
        
@Trace
def hello() :
    print('hello')
    
hello()
#%%
class Trace :
    def __init__(self, func) :
        self.func = func
        
    def __call__(self, *args, **kwargs) :
        r = self.func(*args, **kwargs)
        
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        
        return r
    
@Trace
def add(a, b):
    return a+b

print(add(10,20))
print(add(a=10, b=20))
print(add(50,50))
#%%
class IsMultiple() :
    def __init__(self, x) :
        self.x = x
        
    def __call__(self, func) :
        def wrapper(a, b) :
            
            r = func(a, b)
            if r % self.x == 0 :
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else :
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r
        return wrapper
    
@IsMultiple(3)
def add(a, b) :
    return a+b

print(add(10,20))
print(add(2,5))
#%%
import re
re.match('Hello', 'Hello world!')   
re.match('Python', 'Hello world!')
re.search('^Hello', 'Hello world!')
re.search('world!$', 'Hello world!')
re.match('abc?d', 'abd')
re.match('ab[0-9]?c', 'ab3c')
re.match('ab.d', 'abxd')
re.match('[^A-Z]+', 'a')
#%%
m = re.match('(?P<func>[a-zA-z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
m.group('func')
#%%
re.sub('apple|orange', 'fruit', 'apple box orange tree', 1)
#%%
def multiple10(m) :
    n = int(m.group())
    return str(n * 10)

re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8')
#%%
import math
math.pi
math.sqrt(4.0)
math.sqrt(1.0)
#%%
import math as m
m.sqrt(4.0)
m.pi
r = 4.0
x = r*m.pi*r
print(x)
m.sqrt(x)
#%%
from math import pi
r = 2.0
x = pi*r*r
print(x)
m.sqrt(4.0)
#%%
from math import sqrt
sqrt(4.0)
#%%
from math import pi, sqrt
pi
sqrt(4.0)
r = sqrt(4.0)
s = pi*r*r
h = 5.0
v = s*h
print(v)
#%%
from math import *
pi
sqrt(4.0)
#%%
from math import sqrt as s
s(4.0)
s(2.0)
#%%
from math import pi as p, sqrt as s
p
s(5)
#%%
import math
math.pi
del math
import math
math.pi
#%%
import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
response.status
#%%
import urllib.request as r
response = r.urlopen('http://www.naver.com')
response.status
#%%
from urllib import request
response = r.urlopen('http://www.naver.com')
response.status
#%%
from urllib.request import Request, urlopen
req = Request('http://www.naver.com')
response = urlopen(req)
response.status
#%%
from urllib.request import *

req = Request('http://www.naver.com')
response = urlopen(req)
response.status
#%%
from urllib.request import Request as r, urlopen as u
req = r('http://naver.com')
response = u(req)
response.status
#%%
import requests
r = requests.get('http://www.naver.com')
r.status_code