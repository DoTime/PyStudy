# -*- coding: utf-8 -*-
# a = 2 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 5 * 5 * 5 * 5 * 5 * 5
# print(a)


# 递归实现质子
"""
1.数字除以2 有余数继续除以2,不能 整除  除以3



"""
list = []

def deal_2(num):
    if num % 2 == 0:
        list.append(2)
        num = num / 2
        deal_2(num)
    return num

def deal_3(num):
    if num % 3 == 0:
        list.append(3)
        num = num / 3
        deal_3(num)
    return num

def deal_5(num):
    if num % 5 == 0:
        list.append(5)
        num = num / 5
        deal_5(num)
    return num

deal_5(deal_3(deal_2(3690562500)))
print(list)



print()
print()
print()
print()

#
# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# list1.remove('Taobao')
# print ("列表现在为 : ", list1)
# list1.remove('Baidu')
# print ("列表现在为 : ", list1)


simple_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase

Article => 一个 | 这个
noun => 女人 | 篮球 | 桌子 | 小猫
verb => 看着 | 听着 | 看见
Adj => 蓝色的 | 好看的 | 小小的 | 年轻的"""

Article = ["一个", "这个"]
Adj = ["蓝色的", "好看的", "小小的", "年轻的"]
noun = ["女人", "篮球", "桌子", "小猫"]
verb = ["看着", "听着", "看见"]

from random import choice


def deal(list):
    re = choice(list)
    list.remove(re)
    return re;


# print(deal(Article))

# print('{}{}{}{}{}{}'.format(deal(Article), deal(Adj),deal(noun),deal(verb),deal(Article),deal(noun)))
print((deal(Article) + deal(Adj) + deal(noun) + deal(verb) + deal(Article) + deal(noun)))
