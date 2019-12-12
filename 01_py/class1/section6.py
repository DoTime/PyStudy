# -*- coding: utf-8 -*-
# Dict和Set类型


# 字典是另一种可变容器模型，且可存储任意类型对象。


d = {'Adam': 95,
     'Lisa': 85,
     'Bart': 59
     }
d["Paul"] = 75
print(d)
d.update()

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict['Name']  # 删除键 'Name'
dict.clear()  # 清空字典
del dict  # 删除字典

for key in d.keys():
    print('{}:{}'.format(key, d[key]))
    print("%s: %d" % (key, d[key]))

"""
dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。 
    不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。
    由于dict是按 key 查找，所以，在一个dict中，key不能重复。 
 dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样： 
 dict的第三个特点是作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。
{
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', 'b'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}
 
"""

d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart',
}

d[72] = "Paul";
print(d)

for key in d.keys():
    print(key, ":", d[key])
print("------")
# 默认遍历key
for fuck in d:
    print(fuck, ':', d[fuck])

s = set(["Adam", "Lisa", "Bart", "Paul"])

ss = set(("Adam", "Lisa", "Bart", "Paul"))
s.add("Alis")

s = set([name.lower() for name in ['Adam', 'Lisa', 'Bart', 'Paul']])
s = s.union(name.upper() for name in s)

print('adam'.lower() in s)
print('bart' in s)

print(s)
print(ss)

"""
set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
最后，set存储的元素也是没有顺序的。
"""

# 由于 set 里面的每一个元素都是 tuple 类型数据，所以可以对每个 set 里面的元素使用tuple 元素访问方式访问并读取
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59), "fdsf"])
for m in s:
    print(m[0], ":", m[1])

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']

for x in L:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print(s)

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']

m = set(L)
p = s - m
q = m - s
s = p | q
print(s)

print("----")

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
# l=set(L)
s = s.union(L) - (s.intersection(L))
print(s)

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
l = set(L)
print("++++++")
m = s - l
n = l - s
print(m.union(n))
print(m | n)
