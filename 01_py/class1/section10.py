# -*- coding: utf-8 -*-

"""
列表推导式
"""


# 请编写一个函数，它接受一个 list，然后把list中的所有 字符串变成大写后返回 ，非字符串元素将被忽略。


# range()的情况下，可以加上 if 来筛选：
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]


print(toUppers(['Hello', 'world', 101]))

# 对称三位数


# print("%d%d%d"%  )
print([100 * m + 10 * n + m for m in range(1, 10) for n in range(0, 10)])
L = []
for x in range(1, 10):
    for y in range(10):
        for z in range(1, 10):
            if x == z:
                L.append(100 * x + 10 * y + z)
print(L)
print([100 * x + 10 * y + z for x in range(1, 10) for y in range(10) for z in range(10) if x == z])
print([x for x in range(100, 1000) if str(x)[0] == str(x)[-1]])

print([x for x in range(100, 1000) if x % 10 == int(x / 100)]) #对10取余=对100取整
