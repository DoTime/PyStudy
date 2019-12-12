# -*- coding: utf-8 -*-

"""
循环相关
"""
# 缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。
#

score = 75
if score > 60:
    print ( 'passed')

print ("aa")

score = 85

if score >= 90:
    print ( 'excellent')
elif score >= 80:
    print ( 'good')
elif score >= 60:
    print ( 'passed')
else:
    print ( 'failed')

# for循环

L = [75, 92, 59, 68]
sum = 0.0
for l in L:
    sum += l
print ( sum / 4)

# 利用while循环计算100以内奇数的和。
#
print ("=====")
sum = 0
x = 1
while x < 100:
    if x % 2 == 1:
        sum += x
    x += 1
print ( sum)

sum = 0
x = 1
while x < 100:
    sum += x
    x += 2
print ( sum)

# 利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。


sum = 0
x = 1
n = 1
while True:
    sum += x
    x = x * 2
    n += 1
    if n > 20:
        break
print ( sum)

sum = 0
x = 1
n = 1
while True:
    sum += x
    x = x * 2
    n = n + 1
    if n > 20:
        break
print ( sum)

# continue


sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x

print ( sum)

sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if not x % 2:
        continue
    sum = sum + x
print ( sum)

# 多重循环
# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。

for x in range(10, 100):
    s = int(x / 10)  # 十位
    g = x - s * 10
    if s < g:
        print (str(x) + "( "+ str(s)+ "<"+ str(g)+ ")" )
        print ('{} ({}<{})'.format(x,s,g))

print ("====")

for x in range(1, 10):
    for y in range(0, 10):
        if x < y:
            print (x * 10 + y)

        # print ((x (s < g))
