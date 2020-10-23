# -*- coding: utf-8 -*-

"""
面向对象编程基础
"""



class Person:
    def __init__(self,name):
        self.name=name

xiaoming = Person("xiaoming")
xiaohong = Person("xiaohong")

print (xiaoming)
print (xiaohong)
print (xiaoming==xiaohong)


# 按照实例的名称排序 TODO

class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1,key=lambda x:x.name)


# print (L2[0].name())
# print (L2[1].name)
# print (L2[2].name)








# 对象传参 还可接受任意关键字参数，并把他们都作为属性赋值给实例。
class Person(object):
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        self.__dict__.update(kw)


xiaoming = Person('Xiao Ming', 'Male', birth='1990-1-1', job='Student')

print (xiaoming.name)
print (xiaoming.birth)
print (xiaoming.job)


# 访问限制, __双下划线的属性不能被外部访问  以双下划线开头的"__job"不能直接被外部访问。
# 但是，如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，以"__xxx__"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义。
# 以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print (p.name)
try :
    print (p.__score)
except AttributeError:
    print ('attributeerror')




# 类是模板，而实例则是根据类创建的对象。
# 在定义 Person 类时，可以为Person类添加一个特殊的__init__()方法，当创建实例时，__init__()方法被自动调用，我们就能在此为每个实例都统一加上以下属性

# 绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，如果在类上绑定一个属性，则所有实例都可以访问类的属性，并且，所有实例访问的类属性都是同一个！也就是说，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。
# 因为类属性只有一份，所以，当Person类的address改变时，所有实例访问到的类属性都改变了。

class Person(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1

p1 = Person('Bob')
print (Person.count)

p2 = Person('Alice')
print (Person.count)

p3 = Person('Tim')
print (Person.count)






class Person(object):
    __count = 0
    def __init__(self, name):
        self.name = name
        Person.__count += 1
        print (Person.__count)

p1 = Person('Bob')
p2 = Person('Alice')

try:
    print (Person.__count)
except AttributeError:
    print ('attributeerror')


# 一个实例的私有属性就是以__开头的属性，无法被外部访问
# 虽然私有属性无法从外部访问，但是，从类的内部是可以访问的。除了可以定义实例的属性外，还可以定义实例的方法。

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        score = self.__score
        if (score >= 90):
            return "A-优秀"
        elif(score>60):
            return "B-良好"
        else:return "C-及格"


p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print(p1.get_grade())
print(p2.get_grade())
print(p3.get_grade())






# 由于属性可以是普通的值对象，如 str，int 等，也可以是方法，还可以是函数，   p1.get_grade 为什么是函数而不是方法： 表达式


class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print (p1.get_grade)
print (p1.get_grade())






# 和属性类似，方法也分实例方法和类方法。
# 在class中定义的全部是实例方法，实例方法第一个参数 self 是实例本身。

class Person(object):
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1


print (Person.how_many())
p1 = Person('Bob')
print (Person.how_many())













