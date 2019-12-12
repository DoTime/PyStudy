# -*- coding: utf-8 -*-


'''

Python之什么是函数
我们知道圆的面积计算公式为：

S = πr²
当我们知道半径r的值时，就可以根据公式计算出面积。假设我们需要计算3个不同大小的圆的面积：

r1 = 12.34
r2 = 9.08
r3 = 73.1
s1 = 3.14 * r1 * r1
s2 = 3.14 * r2 * r2
s3 = 3.14 * r3 * r3
当代码出现有规律的重复的时候，你就需要当心了，每次写3.14 * x * x不仅很麻烦，而且，如果要把3.14改成3.14159265359的时候，得全部替换。

有了函数，我们就不再每次写s = 3.14 * x * x，而是写成更有意义的函数调用 s = area_of_circle(x)，而函数 area_of_circle 本身只需要写一次，就可以多次调用。

抽象是数学中非常常见的概念。举个例子：

计算数列的和，比如：1 + 2 + 3 + ... + 100，写起来十分不方便，于是数学家发明了求和符号∑，可以把1 + 2 + 3 + ... + 100记作：

100
∑n
n=1
这种抽象记法非常强大，因为我们看到∑就可以理解成求和，而不是还原成低级的加法运算。

而且，这种抽象记法是可扩展的，比如：

100
∑(n²+1)
n=1
还原成加法运算就变成了：

(1 x 1 + 1) + (2 x 2 + 1) + (3 x 3 + 1) + ... + (100 x 100 + 1)
可见，借助抽象，我们才能不关心底层的具体计算过程，而直接在更高的层次上思考问题。

写计算机程序也是一样，函数就是最基本的一种代码抽象的方式。

Python不但能非常灵活地定义函数，而且本身内置了很多有用的函数，可以直接调用。



'''

l = list(x * x for x in range(1, 101, 1))

print(sum(l))


def square_of_sum(L):
    for l in L:
        print(l)


# print square_of_sum([1, 2, 3, 4, 5])
# print square_of_sum([-5, 0, 5, 15, 25])

'''
'''

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


# 请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。


def square_of_sum_a(L):
    summ = 0
    for x in L:
        # print(x)
        summ += x * x
    return summ;


def square_of_sum(L):
    return sum([i * i for i in L])


print(square_of_sum_a([1, 2, 3, 4, 5]))

print(square_of_sum([1, 2, 3, 4, 5]))
print(square_of_sum([-5, 0, 5, 15, 25]))

# 请编写一个函数，返回一元二次方程的两个解。 一元二次方程的定义是：ax² + bx + c = 0


import math


def quadratic_equation(a, b, c):
    de = b ** 2 - 4 * a * c
    if de >= 0:
        x1 = (-b + math.sqrt(de)) / (2 * a)
        x2 = (-b - math.sqrt(de)) / (2 * a)
        return x1, x2
    else:
        return


print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))

# TODO 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。


"""
我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
如果a只有一个圆盘，可以直接移动到c；
如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
"""


# move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到b柱子上面去

def move(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
        return
    move(n - 1, x, z, y)  # 将前n-1个盘子从x移动到y上
    move(1, x, y, z)  # 将最底下的最后一个盘子从x移动到z上
    move(n - 1, y, x, z)  # 将y上的n-1个盘子移动到z上


move(4, 'A', 'B', 'C')


def greet(xxx = "world."):
    print ("hello,",xxx)

greet()
greet('Bart')



def average(*args):
    if len(args)==0:
        return 0.0
    else:
        return sum(args)*1.0/len(args)

print(average(1,2,3,4))
