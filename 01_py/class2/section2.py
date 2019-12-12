# -*- coding: utf-8 -*-

"""高阶函数"""


# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
# 依次取出list元素值


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def format_name(s):
    return s[0].upper() + s[1:].lower()
    # return s.capitalize()


print(list(map(format_name, ['adam', 'LISA', 'barT'])))


# reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。

def prod(x, y):
    return x * y


from functools import reduce

print(reduce(prod, [2, 4, 5, 7, 12]))

import math


# 请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：

def is_sqr(x):
    return math.sqrt(x) % 1 == 0


print(list(filter(is_sqr, range(1, 101))))

print("<><><>")


# 对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。

# cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。


def cmp_ignore_case(x, y):
    x = x[0].lower
    y = y[0].lower
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


# print (list ( sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], reverse=False))


print("<><><><><>ffffffff")

def calc_prod(lst):
    def prod():
        # return reduce(lambda x, y: x * y, lst)
        return reduce(lambda x, y: x + y, lst)

    return prod


f = calc_prod([1, 2, 3, 4])
print(f())
print("<><><><><>ffffffff")

"""python中匿名函数
高阶函数可以接收函数做参数，有些时候，我们不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算 f(x)=x2 时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：

>>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
通过对比可以看出，匿名函数 lambda x: x * x 实际上就是：

def f(x):
    return x * x
关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。

filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。



"""


def is_not_empty(s):
    return s and len(s.strip()) > 0


filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

s = "sdfsd"
print(s and len(s.strip()) > 0)

ff = filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
print(list(ff))

print("<><><><><>")
"""装饰器
动态给原函数添加功能: 
    调用时候打印日志
    检测性能 调用时间performance
    数据库事务
    URL路由,函数处理指定URL

"""
print("=======================================")


# 定义单个参数
def log(f):
    def fn(x):
        print('call ' + f.__name__ + '()...')
        return f(x)

    return fn


print()


@log
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))


# 定义多个参数
def log(f):
    def fn(*args):
        print('call ' + f.__name__ + '()...')
        return f(*args)

    return fn


@log
def add(x, y, z, a):
    return x + y + z + a


print(add(1, 2, 3, 5))

print("=======================================")

import time


def performance(f):  # 定义装饰器函数，功能是传进来的函数进行包装并返回包装后的函数
    def fn(*args, **kw):  # 对传进来的函数进行包装的函数
        t_start = time.time()  # 记录函数开始时间
        r = f(*args, **kw)  # 调用函数★★
        t_end = time.time()  # 记录函数结束时间
        print('call %s() in %fs' % (f.__name__, (t_end - t_start)))  # 打印调用函数的属性信息，并打印调用函数所用的时间
        return r  # 返回包装后的函数

    return fn  # 调用包装后的函数


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))

"""
带参数的装饰器
log
"""


def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print('[%s] %s()...' % (prefix, f.__name__))
            return f(*args, **kw)

        return wrapper

    return log_decorator


@log('DEBUG')
def test():
    pass


print(test())

import time

print("=================<><>======================")
import time, functools


def performance(unit):
    def fn(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t0 = time.time()
            back = f(*args, **kw)
            t1 = time.time()
            t = (t1 - t0) if unit == 's' else (t1 - t0) * 1000
            print('call %s() in %s %s' % (f.__name__, t, unit))
            return back

        return wrapper

    return fn;


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(3))

print("=================<><>======================")


def performance(unit):
    def fn(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t0 = time.time()
            back = f(*args, **kw)  # 执行函数
            t1 = time.time()
            t = (t1 - t0) if unit == 's' else (t1 - t0) * 1000
            print('call %s() in %s %s' % (f.__name__, t, unit))
            return back

        return wrapper

    return fn


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))
print(factorial.__name__)


"""
和装饰器一样，它可以扩展函数的功能，但又不完成等价于装饰器。通常应用的场景是当我们要频繁调用某个函数时，其中某些参数是已知的固定值，
通常我们可以调用这个函数多次，但这样看上去似乎代码有些冗余，而偏函数的出现就是为了很少的解决这一个问题。

"""
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
# functools.partial可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低
import functools

#sorted_ignore_case = functools.partial(???)

# sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp_ignore_case(s1.upper(), s2.upper()))
sorted_ignore_case = functools.partial(sorted,key=str.lower)


print (sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))








