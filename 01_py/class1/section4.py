# -*- coding: utf-8 -*-


'''
list相关
元组
'''

L = ["Adam", 95.5, "Lisa", 85, "Bart", 59]
print(L)

L = [95.5, 85, 59]
print(L[0])
print(L[1])
print(L[2])
print(L[-1])

L = ['Adam', 'Lisa', 'Bart']
L.insert(2, "Paul")
print(L)

# 插入
L = ['Adam', 'Lisa', 'Bart']
# 方法一
L.insert(2, 'Paul')
print(L)

# 移除首位
L = ['Adam', 'Lisa', 'Paul', 'Bart']
print(())
pop = L.pop(1)
print(pop)
print(L)
print(">>>")
L.pop(2)
print(L)

# 替换list位置
L = ['Adam', 'Lisa', 'Bart']
L[0], L[-1] = L[-1], L[0]
print(L)

# tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。

tp = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9);

print(tp)
t = tuple(x for x in range(0, 10))
print(t)

# for循环使用 range范围取值
# 创建列表
l=list(range(5))
print(l)
[0, 1, 2, 3, 4]

for x in range(0, 10):
    print(x)


print("---")
def addTuple( ):
    t = ()
    for v in range(0, 10):
        t += (v,)
    return t
print(addTuple())

def addTuple2( ):
    l = list(range(5))
    t = ()
    for v in l:
        t += (v,)
    return t
print(addTuple2())


# 单元素tuple
t = ('Adam',)
print(t)

# tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
#
# 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。

t = ('a', 'b', ('A', 'B'))
print(t)
