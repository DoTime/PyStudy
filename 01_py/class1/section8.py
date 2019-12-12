# -*- coding: utf-8 -*-


# 第三个参数表示每N个取一个，上面的 L[::2] 会每两个元素取出一个来，也就是隔一个取一个。


# 1. 前10个数；
# 2. 3的倍数；
# 3. 不大于50的5的倍数。

L = list(range(1, 101))

print(L)
print(L[0:10])
print(L[2::3])
print(L[4:50:5])

# 倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。


print(L[-10:])
print(L[-46::5])
print(L[4::5][-10:])  # 截两次


# 字符串截取
def firstCharUpper(s):
    return s[0:1].upper()+s[1:]

print (firstCharUpper('hello'))
print (firstCharUpper('sunday'))
print (firstCharUpper('september'))