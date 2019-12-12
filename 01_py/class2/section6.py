# -*- coding: utf-8 -*-

"""
python特殊方法
"""


# python中 __str__和__repr__
# 如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)


# Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员。
# 输出toString
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '<Student: %s, %s ,%s>' % (self.name, self.gender, self.score)
        __repr__ = __str__


s = Student('Bob', 'male', 88)
print(s)


# 修改 Student 的 __cmp__ 方法，让它按照分数从高到底排序，分数相同的按名字排序。
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score < s.score:
            return -1
        elif self.score > s.score:
            return 1
        else:
            return 0


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
# print(sorted(L))

c = []
c.append("dsa")
c.append("jksdfds")
print(c)


# 请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)


f = Fib(10)
print(f)
print(len(f))



from functools import reduce


class Fib(object):

    def __init__(self, num):
        fib = [0, 1]
        for i in range(10):
            fib.append(reduce(lambda x, y: x + y, fib[i:i + 2]))  # 截取最后两个数字
        self.num = fib[:-2]

    def __str__(self):
        return str(self.num)

    def __len__(self):
        return len(self.num)


f = Fib(10)
print(f)
print(len(f))

print()
print()
print("Rational类虽然可以做加法，但无法做减法、乘方和除法，请继续完善Rational类，实现四则运算。")

"""就是整数的“比”。与之相对，“无理数”就是不能精确表示为两个整数之比的数   有理数为整数（正整数、0、负整数）和分数的统称 [2]  。" 
"正整数和正分数合称为正有理数，负整数和负分数合称为负有理数。因而有理数集的数可分为正有理数、负有理数和零。" 
"由于任何一个整数或分数都可以化为十进制循环小数，反之，每一个十进制循环小数也能化为整数或分数，因此，有理数也可以定义为十进制循环小数。"""


def gcs(a, b, c=1):
    if 0 == a % 2 and 0 == b % 2:
        return gcs(a / 2, b / 2, c * 2);

    s = abs(a - b)
    m = min(a, b)
    if s == m:
        return m * c
    return gcs(s, m, c)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        c = gcs(self.p, self.q)
        return '%s/%s' % (self.p / c, self.q / c)
    # 1/2 /  3/5

    # def __str__(self):
    #     return '%s/%s' % (self.p, self.q)

    __repr__ = __str__


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print('{} {}'.format(r1, r2))
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
# print(r1 / r2)




print()
print()
# 类型转换
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return float(self.p) / self.q


print (float(Rational(7, 2)))
print (float(Rational(1, 3)))




#  python中 @property

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score < 60:
            return 'C'
        if self.score < 80:
            return 'B'
        return 'A'
s = Student('Bob', 59)
print(s.grade)
s.score = 60
print( s.grade)
s.score = 99
print(s.grade)
s.name="BBBBB"
print(s.name)

s.ss="ss"
print(s.ss)





class Person(object):
    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    __slots__ = ('score',)

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)#传入子类 Student ★★
        self.score = score


s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print(s.score)







print()
# 请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
class Fib(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        return L

f = Fib()
print( f(10))