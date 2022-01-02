#%%
a = [10, 20, 30]
a.append(500)
print(a)
len(a)
#%%
a=[]
a.append(50)
a
#%%
a = [10, 20, 30]
a.append([500, 600])
a
len(a)
#%%
a = [10, 20, 30]
a.extend([500, 600])
a
#%%
a = [10, 20, 30]
a.insert(2, 500)
a
len(a)
#%%
a = [10, 20, 30]
a.insert(len(a), 500)
a
#%%
a = [10, 20, 30]
a.insert(0, 500)
a
#%%
a = [10, 20, 30]
a.insert(1, [500, 600])
a
#%%
a = [10, 20, 30]
a[1:1] = [500, 600]
a
#%%
a = [10, 20, 30]
a.pop()
a
#%%
a = [10, 20, 30]
a.pop(1)
a
#%%
a = [10, 20, 30]
del a[1]
a
#%%
a = [10, 20, 30]
a.remove(30)
a
#%%
from collections import deque
a = deque([10, 20, 30])
a
a.append(500)
a
a.popleft()
a
#%%
a = [10, 20, 30, 15 ,20, 40]
a.index(40)
a.count(20)
#%%
a = [10, 20, 30, 15, 20, 40]
a.reverse()
a
#%%
a = [10, 20, 30, 15, 20, 40]
a.sort(reverse=True)
a
#%%
a = [10, 20, 30, 15, 20, 40]
a.sort()
a
b = [10, 20, 30, 15, 20, 40]
sorted(b)
b
#%%
a = [10, 20, 30]
a.clear()
a
#%%
a = [10, 20, 30]
a[len(a):] = [500]
a
#%%
a = [0, 0, 0, 0, 0]
b = a.copy()
a is b
a == b
b[2] = 99
a
b
#%%
a = [38, 21, 53, 62, 19]
for i in a :
    print(i)
#%%
for i in [38, 21, 53, 62, 19]:
    print(i)
#%%
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a) :
    print(index + 1, value)
#%%
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a, start=1):
    print(index, value)
#%%
a = [38, 21, 53, 62, 19]
for i in range(len(a)) :
    print(a[i])
#%%
a = [38, 21, 53, 62, 19]
i = 0
while i < len(a) :
    print(a[i])
    i += 1
#%%
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a :
    if i < smallest :
        smallest = i
smallest
#%%
a = [38, 21, 53, 62, 19]
a.sort()
a[0]

a.sort(reverse=1)
a[0]
#%%
a = [38, 21, 53, 62, 19]
min(a)
max(a)
#%%
a = [10, 10, 10, 10, 10]
x = 0
for i in a :
    x += i
x
#%%
a = [10, 10, 10, 10, 10]
sum(a)
#%%
a = [i for i in range(10)]
a
b = list(i for i in range(10))
b
c = [i + 5 for i in range(10)]
c
d = [i * 2 for i in range(10)]
d
#%%
a = [i for i in range(10) if i % 2 == 0]
a
#%%
a = [i * j for j in range(2, 10)
           for i in range(1, 10)]
print(a, end= ' ')
#%%
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)) :
    a[i] = int(a[i])
#%%
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
a
#%%
a = list(map(str, range(10)))
a
#%%
a = input().split()
a
#%%
a = map(int, input().split())
a
list(a)
a, b = [10, 20]
a
#%%
a = (38, 21, 53, 62, 19, 53)
a.index(53)
a = (10, 20, 30, 15, 20, 40)
a.count(20)
#%%
a = (38, 21, 53, 62, 19)
for i in a :
    print(i, end=' ')
#%%
a = [[10,20],
     [30,40],
     [50,60]]
a[0][0]
a[1][1]
a[2][1] = 1000
a[2][1]
#%%
a = []
a.append([])
a[0].append(10)
a[0].append(20)
a.append([])
a[1].append(500)
a[1].append(600)
a[1].append(700)
a
#%%
a = [[10,20], [30,40], [50,60]]
from pprint import pprint
pprint(a, indent=4, width=20)
#%%
a = [[10,20], [30,40], [50,60]]
for x,y in a :
    print(x,y)
#%%
a = [[10,20], [30,40], [50,60]]
for i in a :
    for j in i :
        print(j, end=' ')
    print()
#%%
a = [[10,20], [30,40], [50,60]]

for i in range(len(a)) :
    for j in range(len(a[i])) :
        print(a[i][j], end=' ')
    print()
#%%
a = [[10,20], [30,40], [50,60]]
i = 0
while i < len(a) :
    x,y = a[i]
    print(x,y)
    i += 1
#%%
a = [[10,20], [30,40], [50,60]]
i = 0
while i < len(a) :
    j = 0
    while j < len(a[i]) :
        print(a[i][j], end = ' ')
        j += 1
    print()
    i += 1
#%%
a = []
for i in range(10):
    a.append(0)
print(a)
#%%
a = []
for i in range(3) :
    line = []
    for j in range(2) :
        line.append(0)
    a.append(line)
print(a)
#%%
a = [[0 for j in range(2)] for i in range(3)]
a
#%%
a = [[0] * 2 for i in range(3)]
a
#%%
a = [3, 1, 3, 2, 5]
b = []
for i in a :
    line = []
    for j in range(i) :
        line.append(0)
    b.append(line)
print(b)
#%%
a = [[0] * i for i in [3, 1, 3, 2, 5]]
a
#%%
students = [
        ['john', 'C', '19'],
        ['maria', 'A', '25'],
        ['andrew', 'B', '7']
        ]
print(sorted(students, key = lambda student : student[1]))
print(sorted(students, key = lambda student : student[2]))
#%%
a = [[10,20], [30,40], [50,60]]
b = a
b[0][0] = 500
a
b
#%%
a = [[10,20], [30,40]]
b = a.copy()
b[0][0] = 500
a
b
#%%
a = [[10,20], [30,40], [50,60]]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
b
#%%
x = {'a': 10, 'b':20, 'c':30, 'd':40}
x.setdefault('e')
x.setdefault('f', 100)
x.update(a=50)
x.update(a=900, e=100, f=20, g=55)
x
#%%
y = {1 : 'one', 2 : 'two'}
y.update({1:'ONE', 3:'three'})
y.update([[2,'TWO'], [4,'four']])
y.update(zip([1,2], ['one', 'two']))
y
#%%
x = {'a':10, 'b':20, 'c':30, 'd':40}
del x['a']
x.popitem()
x
x.clear()
x
#%%
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.get('g', 0)
#%%
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.items()
x.keys()
x.values()
#%%
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys,100)
from collections import defaultdict
x = defaultdict(int)
x['a']
#%%
x = {'a':10, 'b':20, 'c':30, 'd':40}
for i in x :
    print(i, end=' ')
#%%
x = {'a':10, 'b':20, 'c':30, 'd':40}
for key, value in x.items() :
    print(key, value)
#%%
keys = ['a', 'b', 'c', 'd']
x = {key : value for key, value in dict.fromkeys(keys).items()}
x
#%%
x = {'a':10, 'b':20, 'c':30, 'd':40}
for key, value in x.items() :
    if value == 20 :
        del x[key]
print()
#%%
x = {'a':10, 'b':20, 'c':30, 'd':40}
x = {key : value for key, value in x.items() if value != 20}
x
#%%
x = {'a' : {'python' : '2.7'}, 'b' : {'python' : '3.6' }}
import copy
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
y
#%%
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
'orange' in fruits
'peach' in fruits
a = set('apple')
a
#%%
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
set.union(a,b)
a & b
set.intersection(a,b)
a-b
set.difference(a,b)
a^b
set.symmetric_difference(a,b)
#%%
a = {1, 2, 3, 4}
a |= {5}
a.update({5})
a &= {0, 1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4, 5})
a
#%%
a = {1, 2, 3, 4}
a -= {3}
a.difference_update({3})
a
#%%
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
a.symmetric_difference_update({3, 4, 5, 6})
a
#%%
a = {1, 2, 3, 4}
a <= {1, 2, 3, 4}
a.issubset({1, 2, 3, 4})
#%%
a = {1, 2, 3, 4}
for i in a :
    print(i)
#%%
print('hello, world!')
#%%
file = open('hello.txt', 'w')
file.write('Hello, world!')
file.close()
#%%
file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()
#%%
with open('hello.txt', 'r') as file :
    s = file.read()
print(s)
#%%
with open('hello.txt', 'w') as file :
    for i in range(3) :
        file.write('Hello, world! {0}\n'.format(i))
file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()
#%%
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.']
with open('hello.txt','w') as file :
    file.writelines(lines)
with open('hello.txt','r') as file :
    s = file.read()
    print(s)
#%%
with open('hello.txt', 'r') as file :
    lines = file.readlines()
    print(lines)
#%%
with open('hello.txt', 'r') as file :
    line = None
    while line != '' :
        line = file.readline()
        print(line.strip('\n'))
#%%
with open('hello.txt', 'r') as file :
    for line in file :
        print(line.strip('\n'))
#%%
import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'Korean' : 90, 'english' : 95, 'mathmatics' : 85, 'science' : 82}
with open('james.p', 'wb') as file :
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
    
with open('james.p', 'rb') as file :
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
#%%
word = input('단어를 입력하세요 : ')

is_palindrome = True
for i in range(len(word) // 2) :
    if word[i] != word[-1 - i] :
        is_palindrome = False
        break
print(is_palindrome)
#%%
word = input('단어를 입력하세요 : ')
print(word == word[::-1])
#%%
word = 'level'
list(word) == list(reversed(word))
#%%
word = 'level'
word == ''.join(reversed(word))
#%%
text = 'Hello'

for i in range(len(text) - 1) :
    print(text[i], text[i+1], sep='')
#%%
text = 'this is python script'
words = text.split()
for i in range(len(words) - 1) :
    print(words[i], words[i + 1])
#%%
text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram :
    print(i[0], i[1], sep='')
#%%
text = 'this is python script'
words = text.split()
two_gram = list(zip(words, words[1:]))

for i in two_gram :
    print(i[0], i[1], sep=' ')
#%%
text = 'hello'
[text[i:] for i in range(3)]
list(zip(*['hello', 'ello', 'llo']))
three_gram = list(zip(*[text[i:] for i in range(3)]))
for i in three_gram :
    print(i[0], i[1], i[2], sep='')
#%%
def hello() :
    print('hello, world!')
hello()
#%%
def add( a, b ) :
    print(a + b)
    
add(10, 20)
#%%
def add(a, b) :
    return a + b

x = add(10, 20)
x
print(add(10,20))
#%%
def not_ten(a) :
    if a == 10 :
        return
    print(a, '입니다', sep='')

not_ten(10)
#%%
def add_sub(a, b) :
    return a+b, a-b

x, y = add_sub(10,20)
#%%
def mul(a,b) :
    c = a*b
    return c

def add(a, b):
    c = a+b
    print(c)
    d = mul(a,b)
    print(d)
    
x=10
y=20
add(10,20)
#%%
def print_numbers(a, b, c) :
    print(a)
    print(b)
    print(c)
    
print_numbers(10, 20, 30)
x = [10, 20, 30]
print_numbers(*x)
print_numbers(*[30,40,50])
#%%
x = [1, 2, 3, 4, 5]
def print_numbers(*args) :
    for arg in args :
        print(arg)
        
print_numbers(*x)
#%%
def print_numbers(a, *args) :
    print(a)
    print(args)

print(*(10,30,50))
#%%
def personal_info(name, age, address) :
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

personal_info('이성진',25,'안산')
personal_info(name='이성진', age=25, address='경기도 안산시')
personal_info(age=25, address='경기도 안산시',name='이성진')

print(10, 20, 30, sep=':')
#%%
def personal_info(name, age, address) :
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)
    
x = {'age' : 25, 'name' : '이성진', 'address' : '경기도 안산시'}
personal_info(**x)
#%%
def personal_info(**kwargs) :
    for kw, arg in kwargs.items() :
        print(kw, ' : ', arg, sep='')

personal_info(name = '이성진', age = 25, address = '경기도 안산시', hobby = '게임')
#%%
def personal_info(**kwargs):
    if 'name' in kwargs :
        print('이름 : ', kwargs['name'])
    if 'age' in kwargs :
        print('나이 : ', kwargs['age'])
    if 'address' in kwargs :
        print('주소 : ', kwargs['address'])

personal_info(name = '이성진', age = 25)
#%%
def personal_info(name, age, address = '비공개' ) :
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

personal_info('이성진', 25)
#%%
def hello() :
    print('Hello,world!')
    hello()
    
hello()
#%%
def hello(count) :
    if count == 0 :
        return
    
    print('Hello, world!', count)
    
    count -= 1
    hello(count)
    
hello(5)
#%%
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)

print(factorial(4))
#%%
def plus_ten(x) :
    return x + 10

plus_ten(5)
#%%
lambda x : x + 10
#%%
plus_ten = lambda x : x + 10
plus_ten(4)
#%%
(lambda x : x+10)(10)
#%%
def plus_ten(x) :
    return x + 10

list(map(plus_ten, [1,2,3]))
#%%
list(map(lambda x : x+10, [1,2,3]))
#%%
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x : str(x) if x % 3 == 0 else x, a))
#%%
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x : str(x) if x == 1 else float(x) if x == 2 else x + 10, a))

def f(x) :
    if x == 1 :
        return str(x)
    elif x == 2 :
        return float(x)
    else :
        return x + 10
    
list(map(f, a))
#%%
a = [1,2,3,4,5]
b = [2,4,6,8,10]
list(map(lambda x, y : x*y, a, b))
#%%
def f(x) :
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(f, a))
#%%
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(lambda x : x > 5 and x < 10, a))
#%%
def f(x ,y) :
    return x + y
a = [1,2,3,4,5]
from functools import reduce
reduce(f, a)
#%%
a = [1,2,3,4,5]
from functools import reduce
reduce(lambda x , y : x * y , a)
#%%
x = 10
def foo() :
    global x
    x = 20
    print(x)
    
foo()
print(x)
#%%
def print_hello() :
    hello = 'Hello, world!'
    def print_message() :
        print(hello)
    print_message()
print_hello()
#%%
def A() :
    x = 10
    def B() :
        x = 20
        
    B()
    print(x)
A()
#%%
def A() :
    x = 10
    def B() :
        nonlocal x
        x = 20
        
    B()
    print(x)
A()
#%%
def A() :
    x = 10
    y = 100
    def B() :
        x = 20
        def C() :
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A()
#%%
x = 1
def A() :
    x = 10
    def B() :
        x = 20
        def C() :
            global x
            x = x + 30
            print(x)
        C()
    B()
A()
#%%
def calc() :
    a = 3
    b = 5
    def mul_add(x) :
        return a * x + b
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4), c(5))
#%%
def calc() :
    a = 3
    b = 5
    return lambda x : a * x + b
c = calc()
print(c(1), c(2), c(3), c(4), c(5))
#%%
def calc() :
    a = 3
    b = 5
    total = 0
    def mul_add(x) :
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
c = calc()
c(1)
c(2)
c(3)
#%%
class Person :
    def greeting(self) :
        print('Hello')
    
james = Person()
james.greeting()
#%%
b = list(range(10))
b.append(20)
b
a = 10
type(a)
type(b)
#%%
class Person :
    def __init__(self) :
        self.hello = '안녕하세요'
        
    def greeting(self) :
        print(self.hello)
        
james = Person()
james.greeting()
#%%
class Person :
    def __init__(self, name, age, address) :
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address  = address
        
    def greeting(self) :
        print('{0} 저는 {1}입니다.' .format(self.hello, self.name))
        
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

print('이름 :', maria.name)
print('나이 :', maria.age)
print('주소 :', maria.address)
#%%
class Person :
    def __init__(self, *args) :
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
maria = Person(*['마리아', 20, '서울시 서초구 반포동'])
#%%
class Person :
    def __init__(self, **kwargs) :
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
        
maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name' : '마리아', 'age' : 20, 'address' : '서울시 서초구 반포동'})
#%%
class Person :
    pass

maria = Person()
maria.name = '마리아'
maria.name

james = Person()
james.name
#%%
class Person :
    def greeting(self) :
        self.hello = '안녕하세요'

maria = Person()
maria.greeting()
maria.hello
#%%
class Person :
    __slots__ = ['name', 'age']
    
maria = Person()
maria.name = '마리아'
maria.age = 20
maria.name
#%%
class Person :
    def __init__(self, name, age, address) :
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address
#%%
class Person :
    def __init__(self, name, age, address, wallet) :
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
        
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.name
#%%
class Person :
    def __init__(self, name, age, address, wallet) :
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
    
    def pay(self, amount) :
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))
        
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
#%%
desk = str.maketrans('aeiou', '12345')
'apple'.translate(desk)
'aaaaa'.translate(desk)
#%%
'apple, pear, grape, pineapple, orange'.split(', ')
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
#%%
'%03d'%1
'{0:03d}'.format(35)
#%%
class Person :
    bag = []
    
    def put_bag(self, stuff) :
        self.bag.append(stuff)
        
james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)
#%%
class Knight :
    __item_limit = 10
    
    def print_item_limit(self) :
        print(Knight.__item_limit)
        
x = Knight()
x.print_item_limit()

print(Knight.__item_limit)
#%%
class Calc :
    @staticmethod
    def add(a, b) :
        print(a + b)
        
    @staticmethod
    def mul(a, b) :
        print(a * b)
        
        
Calc.add(10,20)
Calc.mul(10,20)
#%%
class Person :
    count = 0
    
    def __init__(self) :
        Person.count += 1
        
    @classmethod
    def print_count(cls) :
        print('{0}명 생성되었습니다.'.format(cls.count))

james = Person()
maria = Person()

Person.print_count()
#%%
class Person :
    def greeting(self) :
        print('안녕하세요')
        
class Student(Person) :
    def study(self) :
        print('공부하기')

james = Student()
james.greeting()
james.study()
#%%
class Person :
    def greeting(self) :
        print('안녕하세요')

class PersonList :
    def __init__(self) :
        self.person_list = []
        
    def append_person(self, Person) :
        self.person_list.append(Person)
#%%
class Person :
    def __init__(self) :
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person) :
    def __init__(self) :
        print('Student __init__')
        super().__init__()
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)
#%%
class Person :
    def greeting(self) :
        print('안녕하세요')
    
class Student(Person) :
    def greeting(self) :
        super().greeting()
        print('안녕하세요, 저는 이성진입니다.')
        
james = Student()
james.greeting()
#%%
class Person :
    def greeting(self) :
        print('안녕하세요')
        
class University :
    def manage_credit(self) :
        print('학점 관리')
        
class Undergraduate(Person, University) :
    def study(self) :
        print('공부하기')

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()
#%%
class A :
    def greeting(self) :
        print('A입니다')
        
class B(A) :
    def greeting(self) :
        print('B입니다')
        
class C(A) :
    def greeting(self) :
        print('C입니다')

class D(B,C) :
    pass

x = D()
x.greeting()
D.mro()
#%%
from abc import *

class StudentBase(metaclass=ABCMeta) :
    @abstractmethod
    def study(self) :
        pass
    
    @abstractmethod
    def go_to_school(self) :
        pass
    
class Student(StudentBase) :
    def study(self) :
        print('공부하기')
        
    def go_to_school(self) :
        print('학교가기')
        
james = Student()
james.study()
james.go_to_school()
#%%
import math

class Point2D :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
p1 = Point2D(x = 30, y = 20)
p2 = Point2D(x = 60, y = 50)

print('p1 : {} {}'.format(p1.x, p1.y))
print('p2 : {} {}'.format(p2.x, p2.y))

a = p2.x - p1.x
b = p2.y - p1.y

c = math.sqrt((a*a) + (b*b))
print(c)
#%%
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        x = int(num)
    except :
        print('Invalid input')
        continue
    if largest is None :
        largest = x
        if smallest is None :
            smallest = x
    elif x > largest :
        largest = x
    elif x < smallest :
        smallest = x

print("Maximum is", largest)
print('Minimum is', smallest)