try :
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10/x
    print(y)
except :
    print('에러가 발생했습니다.')
#%%
y = [10, 20, 30]

try :
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요 : ').split())
    print(y[index] / x)
except ZeroDivisionError :
    print('숫자를 0으로 나눌 수 없습니다')
except IndexError :
    print('잘못된 인덱스입니다')
#%%
y = [10, 20, 30]

try :
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요 : ').split())
    print(y[index] / x)
except ZeroDivisionError as e :
    print('숫자를 0으로 나눌 수 없습니다', e)
except IndexError as e :
    print('잘못된 인덱스입니다', e)
#%%
try :
    x = int(input('나눌 숫자를 입력하세요 : '))
    y = 10 / x
except ZeroDivisionError :
    print('숫자를 0으로 나눌 수 없습니다.')
else :
    print(y)
#%%
try :
    x = int(input('나눌 숫자를 입력하세요 : '))
    y = 10 / x
except ZeroDivisionError :
    print('숫자를 0으로 나눌 수 없습니다')
else :
    print(y)
finally :
    print('코드 실행이 끝났습니다')
#%%
try :
    x = int(input('3의 배수를 입력하세요 : '))
    if x % 3 != 0 :
        raise Exception('3의 배수가 아닙니다')
    print(x)
except Exception as e :
    print('에러가 발생했습니다.', e)
#%%
def three_multiple():
    x = int(input('3의 배수를 입력하세요 : '))
    if x % 3 != 0 :
        raise Exception('3의 배수가 아닙니다')
    print(x)
    
try :
    three_multiple()
except Exception as e :
    print('에러가 발생했습니다', e)
#%%
def three_multiple() :
    try :
        x = int(input('3의 배수를 입력하세요 : '))
        if x % 3 != 0 :
            raise Exception('3의 배수가 아닙니다')
        print(x)
    except Exception as e :
        print('three_multiple 함수에서 에러가 발생했습니다', e)
        raise
        
try :
    three_multiple()
except Exception as e :
    print('스크립트 파일에서 에러가 발생했습니다', e)
#%%
def three_multiple() :
    try :
        x = int(input('3의 배수를 입력하세요 : '))
        if x % 3 != 0 :
            raise Exception('3의 배수가 아닙니다')
        print(x)
    except Exception as e :
        print('three_multiple 함수에서 에러가 발생했습니다', e)
        raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다')

three_multiple()

#%%
class NotThreeMultipleError(Exception) :
    def __init__(self) :
        super().__init__('3의 배수가 아닙니다')
        
def three_multiple() :
    try :
        x = int(input('3의 배수를 입력하세요'))
        if x % 3 != 0 :
            raise NotThreeMultipleError
        print(x)
    except Exception as e :
        print('예외가 발생했습니다', e)
        
three_multiple()
#%%
dir(range(5))
dir([1,2,3,4,5])
it = [1,2,3].__iter__()
it.__next__()
#%%
it = range(3).__iter__()
it.__next__()
#%%
class Counter :
    def __init__(self, stop) :
        self.current = 0
        self.stop = stop
        
    def __iter__(self) :
        return self
    
    def __next__(self) :
        if self.current < self.stop :
            r = self.current
            self.current += 1
            return r
        else :
            raise StopIteration('Interation이 중단되었습니다')

for i in Counter(3) :
    print(i, end = ' ')
#%%
class Counter :
    def __init__(self, stop) :
        self.current = 0
        self.stop = stop
        
    def __iter__(self) :
        return self
    
    def __next__(self) :
        if self.current < self.stop :
            r = self.current
            self.current += 1
            return r
        else :
            raise StopIteration('Interation이 중단되었습니다')
    
a, b, c = Counter(3)
print(a, b, c)

a, b, c, d, e = Counter(5)
print(a, b, c, d, e)
#%%
class Counter :
    def __init__(self, stop) :
        self.stop = stop
        
    def __getitem__(self, index) :
        if index < self.stop :
            return index
        else :
            raise IndexError
            
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3) :
    print(i, end = ' ')
#%%
it = iter(range(3))
next(it)
#%%
import random
it = iter(lambda : random.randint(0, 5), 2)
next(it)
#%%
def number_generator() :
    yield 0
    yield 1
    yield 2
    
for i in number_generator() :
    print(i, end=' ')

a = number_generator()
dir(a)
a.__next__()
#%%
def number_generator(stop) :
    n = 0
    while n < stop :
        yield n
        n += 1
        
for i in number_generator(3) :
    print(i, end= ' ')
#%%
def upper_generator(x) :
    for i in x :
        yield i.upper()
        
fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits) :
    print(i, end = ' ')
#%%
def number_generator() :
    x = [1, 2, 3]
    for i in x :
        yield i

for i in number_generator() :
    print(i, end = ' ')
#%%
def number_generator() :
    x = [1, 2, 3]
    yield from x
    
for i in number_generator() :
    print(i, end = ' ')
#%%
def number_generator(stop) :
    n = 0
    while n < stop :
        yield n
        n += 1
        
def three_generator() :
    yield from number_generator(3)
    
for i in three_generator() :
    print(i, end = ' ')
#%%
def number_coroutine() :
    while True :
        x = (yield)
        print(x)
        
co = number_coroutine()
next(co)

co.send(1)
co.send(2)
co.send(3)
#%%
def sum_coroutine() :
    total = 0
    while True :
        x = (yield total)
        total += x
        
co = sum_coroutine()
print(next(co))

print(co.send(1))
print(co.send(2))
print(co.send(3))
#%%
def number_coroutine() :
    while True :
        x = (yield)
        print(x, end = ' ')

co = number_coroutine()
next(co)

for i in range(20) :
    co.send(i)
    
co.close()
#%%
def number_coroutine() :
    try :
        while True :
            x = (yield)
            print(x, end = ' ')
    except GeneratorExit :
        print()
        print('코루틴 종료')

co = number_coroutine()
next(co)

for i in range(20) :
    co.send(i)
    
co.close()
#%%
def sum_coroutine() :
    try :
        total = 0
        while True :
            x = (yield)
            total += x
    except RuntimeError as e :
        print(e)
        yield total
        
co = sum_coroutine()
next(co)

for i in range(20) :
    co.send(i)
    
print(co.throw(RuntimeError, '에러로 코루틴 끝내기'))
#%%
def accumulate() :
    total = 0
    while True :
        x = (yield)
        if x is None :
            return total
        total += x
        
def sum_coroutine() :
    while True :
        total = yield from accumulate()
        print(total)
        
co = sum_coroutine()
next(co)

for i in range(1, 11) :
    co.send(i)
co.send(None)

for i in range(1, 101) :
    co.send(i)
co.send(None)
#%%
def accumulate() :
    total = 0
    while True :
        x = (yield)
        if x is None :
            raise StopIteration(total)
        total += x
        
def sum_coroutine() :
    while True :
        total = yield from accumulate()
        print(total)
        
co = sum_coroutine()
next(co)

for i in range(1, 11) :
    co.send(i)
co.send(None)

for i in range(1, 101) :
    co.send(i)
co.send(None)
#%%
def number_coroutine() :
    x = None
    while True :
        x = (yield x)
        if x == 3 :
            return x
        
def print_coroutine() :
    while True :
        x = yield from number_coroutine()
        print('print_coroutine : ', x)
        
co = print_coroutine()
next(co)

x = co.send(1)
print(x)
x = co.send(2)
print(x)
co.send(3)
        