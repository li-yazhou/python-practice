# -*- coding: utf-8 -*-

class Product(object):
	def __init__(self,id,name,price):
		self.id = id
		self.name = name
		self.price = price

	# 比较两个对象是否相等
	def __eq__(self,other):
		return self.id == other.id

	def __str__(self):
		s = '商品id是:' + str(self.id) + \
			'\t 商品名是：' + self.name + \
			'\t 商品单价是：' + str(self.price) 
		return s

