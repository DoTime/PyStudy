# -*- coding: utf-8 -*-
"""类的继承"""


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course


t = Teacher('Alice', 'Female', 'English')
print(t.name)
print(t.course)

# python中判断类型
# 这说明在继承链上，一个父类的实例不能是子类类型，因为子类比父类多了一些属性和方法。
print()
print(isinstance(t, Person))
print(isinstance(t, Student))
print(isinstance(t, Teacher))
print(isinstance(t, object))

"""多态 """
# https://www.imooc.com/code/6247

# 由于Python是动态语言，所以，传递给函数 who_am_i(x)的参数 x 不一定是 Person 或 Person 的子类型。任何数据类型的实例都可以，只要它有一个whoAmI()的方法即可：
# 动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用。


import json


class Students(object):
    def __init__(self, strlist):
        self.strlist = strlist

    def read(self):
        return (self.strlist)


s = Students('["Tim", "Bob", "Alice"]')

print(json.load(s))

# 多重继承
class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(BasketballMixin,Student):
    pass

class FTeacher(FootballMixin,Teacher):
    pass

s = BStudent()
print (s.skill())

t = FTeacher()
print (t.skill())



# 希望除了 name和gender 外，可以提供任意额外的关键字参数，并绑定到实例，请修改 Person 的 __init__()定义，完成该功能。


class Person(object):

    def __init__(self, name, gender, **kw):
        self.name=name
        self.gender=gender
        # self.__dict__.update(kw)
        for k, v in kw.items():
            setattr(self, k, v)


p = Person('Bob', 'Male', age=18, course='Python',score='60')
print (p.age)
print (p.course)
print(p.score)