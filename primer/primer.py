# coding=utf-8

from __future__ import print_function

import base64
import hashlib
import struct
import types
import logging
import os
import pickle
import shutil
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

import itertools

import module
from module import Bike
from module import MountainBike
from module import Fib
from module import Github

# Basic type
import functools

a = -8000
b = 0x123
c = 1.2e5
print(a, b, c)

# Char \
print(r'\\\\\\\\')
print('I\'m \\ok\n\t')
print('''line1
line2
line3
''')
print(True, False)
print(True or False, True and False, not True)
print(None)

a = 'ABC'
b = a
a = 'DEF'
print(a, b)

NUM = 1000
print(NUM)

print('这是一句中文')

# List
lists = ['a']
print(lists)

lists.append('b')
print(lists)

lists.insert(1, 'c')
lists.append('d')
lists.append('e')
print(lists)

lists.pop()
print(lists)
print(lists[0], lists[3])

# Tuple
tuples = (0, 1, 2)
print(tuples)

t = (1,)
print(t)

# Loop
ages = (17, 20)
for age in ages:
    if age > 18:
        print("成年人")
    else:
        print("未成年")

# Dict 空间换时间
d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(d['b'])

# Set
s = {0, 1, 2}
print(s)

# Function
print(abs(-100))


def abs_ex(num):
    if not isinstance(num, (int, float)):
        raise TypeError('Bad operand type')
    if num > 0:
        return num
    else:
        return -num


print(abs_ex(-100))


# print(abs_ex('abc'))

def get_rect(size):
    if not isinstance(size, (int, float)):
        raise TypeError('Bad operand type')
    return size, size, size, size


print(get_rect(100))

# 切片
print(ages[0:1])
print(ages[1:2])
print(ages[:2:2])

# Iteration
for key, value in d.iteritems():
    print(key, value)

# Get
for i, value in enumerate(ages):
    print(i, value)

# Create list
print([x * x for x in range(1, 6) if x % 2 == 0])
print([m + n for m in 'ABC' for n in "abc"])
print([age > 18 for age in ages])


# Generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


print(fib(10))
for n in fib(10):
    print(n)


# Map
def f(x):
    return x * x


print(map(f, [1, 2, 3, 4]))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def first_up(s):
    if not isinstance(s, str):
        return s
    return s[:1].upper() + s[1:].lower()


print(map(first_up, [1111, 'EFedda', 'A', 'c']))
print(map(first_up, ['adam', 'LISA', 'barT']))


# Reduce
def add(x, y):
    return 10 * x + y


def multiplication(x, y):
    return x * y


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(list):
    return reduce(multiplication, list)


print(prod([1, 2, 3, 4, 5]))

print(reduce(add, [1, 3, 5, 7, 9]))


# Filter
def not_prime(num):
    if not isinstance(num, int):
        return num

    if num == 1:
        return False

    n = 2
    while n < num:
        if num % n == 0:
            return False
        n += 1

    return True


print(filter(not_prime, range(1, 101)))


# Sorted
def cmp_ignore_case(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        return 0

    u1 = s1.lower();
    u2 = s2.lower();
    return u1 > u2


print(sorted([1, 2, 3, 4, 5]))
print(sorted([1, 2, 3, 4, 5], reverse=True))
print(sorted(['abbc', 'DDDD', 'eeere']))
print(sorted(['abbc', 'DDDD', 'eeere'], cmp_ignore_case))

# 匿名函数
print(map(lambda x: x * x, [1, 2, 3, 6]))


# 装饰器
def logDecorator(func):
    def wrapper(*args, **kw):
        print('call %s before' % func.__name__)
        func(*args, **kw)
        print('call %s after' % func.__name__)

    return wrapper


@logDecorator
def log(s):
    print(s)


log("bean")

# 偏函数
int2 = functools.partial(int, base=2)
print(int('100000'))
print(int2('100000'))

# Array
company = ['珠海扬智电子科技有限公司']
company_str = company[0]
print(company)

# Module
module.test()

# Class
bike = Bike("美利达", 1000)
print(Bike)
print(bike)
print(bike.name)
print(bike.price)
print(bike.get_level())

mountainBike = MountainBike("捷安特", 1500)
print(mountainBike.name)
print(mountainBike.price)
print(mountainBike.get_level())

# Object type
print(type(123))
print(type('abc'))
print(type(None))
print(type(abs))
print(type(bike))
print("asd is type string:", type('asd') == types.StringType)
print("111 is type string:", isinstance(111, str))

print("bike isinstance MountainBike:", isinstance(bike, MountainBike))
print("mountainBike isinstance Bike:", isinstance(mountainBike, Bike))

print("dir bike", dir(bike))

print("bike has attr price", hasattr(bike, 'price'))
print("bike has attr road", hasattr(bike, 'road'))
print("bike set attr price")
setattr(bike, 'price', 600)
print("bike has attr road", getattr(bike, 'price', 500))

# slots
print(bike.__slots__)

# Property
bike.color = 'green'
print(bike.color)

# 多重继承
mountainBike.run()

# 定制类, 例如str, iter, getitem,
print(bike)
print("Fib 100:")
for n in Fib():
    print(n)

# getattr
print(Github().user.avater)
print(Github().users('kylingo').repos)

# callable
a = Github()
a()

# Exception
try:
    print('try...')
    r = 10 / 0
except StandardError as e:
    print('exception:', e)
    logging.exception(e)
finally:
    print('finally')


class FooError(StandardError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value: %s", s)
    print("foo", 10 / n)
    return 10 / n


# foo
foo(1)

# File
path = './python.txt'
with open(path, 'w') as f:
    f.write("hello")

with open(path, 'r') as f:
    print("file:", f.read())

# os
print('os name:', os.uname())
print('os environ:', os.environ)
print('os path:', os.getenv('PATH'))

# dir
print('os current path:', os.path.abspath('.'))
new_path = os.path.join('.', 'test')
if not os.path.exists(new_path):
    os.makedirs(new_path)
    os.removedirs(new_path)
else:
    os.removedirs(new_path)

# file split
path_array = os.path.split(path)
suffix_array = os.path.splitext(path)
print('file name:', path_array[1])
print('file suffix:', suffix_array[1])

# shutil
copy_path = './python_copy.txt'
if not os.path.exists(copy_path):
    shutil.copyfile(path, copy_path)
    os.remove(copy_path)
else:
    os.remove(copy_path)

# rename
rename_path = './python_new.txt'
os.rename(path, rename_path)
os.remove(rename_path)

# filter
list_file = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print('current list file:', list_file)

# picking
d = dict(name='blob', age=20, score=88)
dump_file = open('./dump.txt', 'w')
pickle.dump(d, dump_file)
dump_file.close()
print("pickle dump file:", d)

dump_file = open('./dump.txt', 'r')
d = pickle.load(dump_file)
dump_file.close()
print("pickle load file:", d)
# remove dump file
os.remove('./dump.txt')

# Intern module
# namedtuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 2)
print('namedtuple', point)
print(point.x)
print(point.y)

# deque
q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('q')
print(q)

# defaultdict
dd = defaultdict(lambda: 'N/A')
dd['name'] = 'frank'
print(dd['name'])
print(dd['age'])

# OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print('d:', d)
print('od:', od)
print('od.key:', od.keys())

# Counter
counter = Counter()
for ch in 'Hello python':
    counter[ch] = counter[ch] + 1
print(counter)

# base64
b64 = base64.b64encode('kylingo')
print('b64:', b64)


def ba64(ba64_str):
    return base64.b64decode(ba64_str + '=' * (4 - len(ba64_str) % 4))


c64 = ba64('a3lsaW5nbw')
print('c64:', c64)

# struct
str_pack = struct.pack('>I', 10240090)
print('str_pack:', str_pack)

array_unpack = struct.unpack_from('>I', str_pack)
print('int_unpack', array_unpack)

str_bmp = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
array_bmp = struct.unpack('<ccIIIIIIHH', str_bmp)
print('array_bmp:', array_bmp)

# hashlib
md5 = hashlib.md5()
md5.update('kylinggo')
print("kylingo md5:", md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('kylinggo')
print("kylingo sha1:", sha1.hexdigest())

# 加盐，加用户名，实现密码的md5加密，更安全

# itertools
iter_count = itertools.count(1)
print('itertools count')
for i in iter_count:
    print(i)
    if i == 100:
        print('i == 100 break')
        break

cs = itertools.cycle('ABCDEFG')
print('itertools cycle')
for i, c in enumerate(cs):
    print(c)
    if i == 100:
        print('i == 100 break')
        break

ir = itertools.repeat('AB', 10)
print('itertools repeat')
for c in ir:
    print(c)

iter_count = itertools.count(1)
ns = itertools.takewhile(lambda x_count: x_count < 10, iter_count)
print('itertools takewhile')
for n in ns:
    print(n)

print('itertools chain')
for c in itertools.chain('gank', 'carry'):
    print(c)

print('itertools groupby')
for key, group in itertools.groupby('aaacccedddf'):
    print(key, list(group))

print('itertools imap')
for x in itertools.imap(lambda x, y: x * y, [10, 20, 40], itertools.count(1)):
    print(x)
