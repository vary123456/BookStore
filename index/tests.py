# it is test for git commit
# commit second 20230214-2
# def score_grade(score):
#     if not isinstance(score,int):
#         raise TypeError("你应该输入一个整数类型")
#     if not (0<=score<=100):
#         raise Exception("你输入的整数范围应该在0-100之间")
#     if 0<=score<60:
#         return "D"
#     elif 60<=score<=75:
#         return 'C'
#     elif 75<score<=85:
#         return 'B'
#     else:
#         return 'A'
#
#
# import unittest
# class TestScore(unittest.TestCase):
#     def test_exception(self):
#         with self.assertRaises(TypeError):
#             score_grade('x')
#
#     def test_score(self):
#         self.assertEqual(score_grade(86),'A')
#         self.assertNotEqual(score_grade(86),'A', '这是第二个测试')
#         self.assertTrue(score_grade(86) is 'A')
#
# import sys
# import unittest
# from django.test import TestCase, tag
# from index.models import *
# class TestPub(TestCase):
#     def test_pub_create(self):
#         pub1 = Pub.objects.create(name='', addr='地址test1')
#         self.assertIsNotNone(pub1, '出版社1创建失败')
#         pub2 = Pub.objects.create(name='', addr='地址test2')
#         self.assertIsNotNone(pub2, '出版社2创建失败')
#         # book = Book.objects.create(title='书test1')
#         # self.assertIsNotNone(book, 'book创建失败')
#
#     @tag('tag2')
#     def test_pub_get(self):
#         pub1 = Pub.objects.filter(name__contains='海南')
#         self.assertIsNotNone(pub1)

# def func(a=1):
# 	b = 2
# 	print(locals())#打印当前函数（方法）的局部命名空间
# 	'''
# 	locs = locals()#只读，不可写。将报错！
# 	locs['c'] = 3
# 	print(c)
# 	'''
# 	return a+b
# func()
# glos = globals()
# glos['d'] = 4
# print('d:',d)
#
# print(globals())#打印当前模块namespace_test.py的全局命名空间

# #print(__dict__)
# print(__doc__)
# print(__package__)
# print(__path__)

import sys
#from index.models import Book
# from . import models
# import models


# import time
#
# time1 = time.time()
# #print(time1)
# time.sleep(1)
# time2 = time.time()
# print(time2 - time1)

# from index.models import *
#
# Author.objects.create(id='1', name='lili', email='lili@163.com')
# Author.objects.create(name='lili', email='lili@163.com')


# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirst.settings')

# import django
# django.setup()

# sum = 0
# for n in range(1000000000):
#     sum = sum + n
# print(sum)

#from models import UserInfo
#from django.contrib.auth import authenticate
