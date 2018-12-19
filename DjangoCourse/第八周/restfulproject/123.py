import copy


# a = [1, 2, 3, 4, ["a", "b"]]
#
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
#
# a.append(5)  # a = [1, 2, 3, 4, ["a", "b"], 5]
# a[4].append("c")  # a = a = [1, 2, 3, 4, ["a", "b", "c"], 5]

# print(a)  # [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# print(b)  # [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# print(c)  # [1, 2, 3, 4, ['a', 'b', 'c']]
# print(d)  # [1, 2, 3, 4, ['a', 'b']]

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]


# print(list(dedupe(a)))

def dedupe(items):
    items.reverse()
    for x in items:
        while items.count(x) > 1:
            a.remove(x)
    items.reverse()
    return items


# print(dedupe(a))


a_list = [1, 4, 4, 2, 1, 7]
b_list = []
for a in a_list:
    if a not in b_list:
        b_list.append(a)
# print(b_list)
# import collections
# collections 是Python内建的一个集合模块，提供了许多有用的集合类。
# d = dict()
# d["a"] = "1"
# d["c"] = "3"
# d["b"] = "2"
# # dict的Key是无序的
# a = collections.OrderedDict()
# a["a"] = "1"
# a["c"] = "3"
# a["b"] = "2"
# for x, y in d.items():
#     print(x, y)
# for x, y in a.items():
#     print(x, y)
# 将[{1:”a”},{2:”b”}]转换为[{"value":"a", "key":1},{"value":"b", "key":2}]
"""
#d = {key: value for (key, value) in iterable}
d1 = {'x': 1, 'y': 2, 'z': 3}
d2 = {k: v for (k, v) in d1.items()}
print(d2)
"""
# a = [{1:"a"},{2:"b"}]
# print([next({'value':value,'key':key} for key,value in a[x].items()) for x in range(len(a))])
# # print([next({"value": v, "key": k} for k, v in a[x].items()) for x in range(len(a))])
# # c = [{'value': value, 'key': key} for key, value in a[].items()]
# # print(c)
#
# import collections
# #
# d={}
# d['a']='A'
# d['b']='B'
# d['c']='C'
# for k,v in d.items():
#     print (k,v)
#
# print ("\nOrder dictionary")
# d1 = collections.OrderedDict()
# d1['a'] = 'A'
# d1['b'] = 'B'
# d1['c'] = 'C'
# d1['1'] = '1'
# d1['2'] = '2'
# for k,v in d1.items():
#     print(k,v)
#
# dd = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
# res=dd.items()
# print(res)
# #按key排序
# kd = collections.OrderedDict(sorted(dd.items(), key=lambda t: t[0]))
# print(kd)
# vd = (sorted(dd.items(),key=lambda t:t[1]))
# print(vd)
#
# dict1 = {'1':2, '3': 3}
# dict2 = dict(tuple(dict1.items()))
# a=tuple(dict1.items())
# # print(dict2)
# dict3=list(dict1.items())
# dict4=dict(set(dict1.items()))
# print("++",dict3)
# list_1=[1,2,3,4]
# b=tuple(list_1)
# list__2=list(b)
# # print(list__2)
# list_1=[1,1,2,3,4,5,6,6]
# list_2=tuple(list_1)
# print(list_2)
#
# tuple1=(1,23,4,5,6,7,[1,2],1)
# tuple2=tuple(list(tuple1))
# tuple3=(set(tuple1))
# print(tuple3)
# a = "abcdef"


# b=list(a)
# b.reverse()
# c=''.join(b)
# print(c)
# def string_reverse(x):
#     return x[::-1]
#
#
# b = string_reverse(a)
# print(b)
#
#
# # type(object_or_name, bases, dict)
# People = type("People", (object, ), {"name": "zhangsan"})
#
# a = People()
# # print(a.name)

# def add(x, y, func):
#     return func(x) + func(y)
# print(add(-2, 14, abs))
# class A:
#     name='a'
# class B(A):
#     pass
# b=B()
# b.name='b'
# print(B.name)
# a=[1,2,3,4,5,[1,2]]
# b=copy.deepcopy(a)
# a[-1].append(1)
# a[0]=11
# print(b)
# print(a)
# import pandas as pd
# df1 = pd.DataFrame(
#     data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#     index=[1, 2, 3],
#     columns=['a', 'b', 'c']
# )
# df2 = pd.DataFrame(
#     data=[[11, 22, 33], [44, 55, 66], [77, 88, 99]],
#     index=[4, 5, 6],
#     columns=['a', 'b', 'c']
# )

# for x in range(0,5):
#     print(x)

# dict1 = {'name': 'zhangsan', 'age': 20}
# dict1 = dict(tuple(dict1.items()))
# print(dict1)
#
# a = 10
#
#
# def func(a):
#     a = 20
#
# func(a)
# print(a)
# A = 10
# B = 10
# print(A == B)
# print(A is B)

import datetime
def dayofyear():
    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入天：")
    date1=datetime.date(year=int(year),month=int(month),day=int(day))
    date2=datetime.date(year=int(year),month=1,day=1)
    return (date1 -date2).days

# res=dayofyear()
# print(res)
# alist=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
# def sort_by_age(list1):
#     return sorted(alist,key=lambda x:x['age'],reverse=True)
# res=sort_by_age(alist)
# print(res)
from operator import itemgetter
# dict1 = [
#     {'name': 'zhangsan', 'age': 20},
#     {'name': 'lisi', 'age': 30},
#     {'name': 'wangwu', 'age': 25},
#     {'name': 'zhangfei', 'age': 12},
#     {'name': 'zhaoliu', 'age': 42},
# ]
# sort_by_age = sorted(alist, key=itemgetter('age'), reverse=True)
# print(sort_by_age)
# res = itemgetter("age")

import json
str1 = "k:1|k1:2|k2:3|k3:4"
str1 = str1.replace('|', '","')
str1 = str1.replace(':', '":"')
str2 = '{"'+str1+'"}'
# print(str2)
# print(json.loads(str2))

from urllib import parse


a = "李少辉"
b = parse.quote(a)
c = parse.unquote(b)
# print(b)


# def a():
#     for x in range(0, 10):
#         yield x
#
#
# print(a())
# for x in a():
#     print(x)


b=[1,2,3]
d={a for a in b}
# print(d)
# result = []
# for x in range(10):
#     result.append(x ** 2)
# print(result)
result = [x ** 2 for x in range(10)]
# print(result)

def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    # print(id(l))
    # print(l)
    # print('****')
# f(2)
# f(3,[3,2,1])
# f(3)
# A11=zip('a','b','c','d','e')
# print(list(A11))
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print('A0',A0,'--A1',A1,'--A2',A2,'--A3',A3,'--A4',A4,'--A5',A5,'--A6',A6)

# a = zip(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5])
# print(list(a))

# import datetime
# datetime.datetime.now="123"
# res=datetime.datetime.now()
# print(res)

#Xpath\lxml\css\正则\Beautifulsoup