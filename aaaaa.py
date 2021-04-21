'''
#!/usr/bin/env python3  这行注释可以让代码在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-   表示文件使用标准UTF-8编码
github 是否可以检测到文件发生变化

list() 列表   tuple() 元组   dict() 字典
type()
lambda  函数可省略定义函数
filter(过滤标准，过滤对象)              map(函数关系，定义域) 

递归
id(a)   查看变量a的地址
help(object)
dir(object) 查看对象的所有属性和方法
set()   创建集合，集合的唯一性，会把重复元素删除
open('文件路径和名称用双斜杠','打开方式')
pickle


斐波拉契数列
def fibo(n):
    i,a,b=0,0,1
    while i<n:
        print(b)
        t=(b,a+b)
        a=t[0]
        b=t[1]
        i+=1
        
fibo(7)    

杨辉三角形
def  triangles():
    L=[1]
    while 1:
        yield L[:]
        L.append(0)
        L=[L[n]+L[n-1] for n in range(len(L))]
n=0
for i in triangles():
    if n==5:
        break
    else:
        print (i)
        n+=1
将任意数字字符串转换成数字 '123.456' to 123.456
def str2float(s):
    n=s.index('.')
    s0=[i for i in s]
    s0.remove('.')
    s1=list(map(int,s0))
    y=0
    for x in range(len(s)-1):
        y=y+s1[x]*10**(n-1-x)
    return y

'''






import unittest

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):

        if 80>self.score >= 60:
            return 'B'
        elif 100>=self.score >= 80:
            return 'A'
        elif 60>self.score >= 0:
            return 'C'
        else:
            raise ValueError('wrong value')


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()





































