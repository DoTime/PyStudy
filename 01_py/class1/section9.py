# -*- coding: utf-8 -*-

# 迭代
for i in range(1, 101)[6::7]:
    print(i)

print("<><>")
print(x for x in range(1, 101)[6::7])

print("===")  # https://www.runoob.com/python/python-strings.html
print("\n".join("%s" % i for i in range(7, 101, 7)))

# 索引迭代
# Python中，迭代永远是取出元素本身，而非元素的索引。
# 对于有序集合，元素确实是有索引的。有的时候，我们确实想在 for 循环中拿到索引，怎么办？

print("enumerate")

L = ['Adam', 'Lisa', 'Bart', 'Paul']

for x, y in enumerate(L):
    print(x + 1, y)

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L) + 1), L):  # zip合并连接list
    print(index, '-', name)

print("-----------------")
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}

print(d.values())
print(1.0 * sum(d.values()) / len(d))

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }


print("-----------------")

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print (k,":",v)
    print("%s:%d" % (k, v))
print ('average', ':', sum*0.1/len(d))


#字符串格式化输出
# 字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.items()]
print ('<table border="1">')
print ('<tr><th>Name</th><th>Score</th><tr>')
print ('\n'.join(tds))
print ('</table>'())