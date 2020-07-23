# -*- coding: utf-8 -*-

class User(object):
	def __init__(self,id,name,password):
		self.id = id
		self.name = name
		self.password= name

	def __str__(self):
		s = '用户id是：' + self.id + \
			'用户名是：' + self.name
		return s


class Product(object):
	def __init__(self,id,name,price):
		self.id = id
		self.name = name
		self.price = price

	# 比较两个对象是否相等
	def __eq__(self,other):
		return self.id == other.id

	def __str__(self):
		s = '商品id是：' + str(self.id) + \
			'\t 商品名是：' + self.name + \
			'\t 商品单价是：' + str(self.price) 
		return s

class ProductItem(object):
	def __init__(self,product,count=1):
		self.id = product.id
		self.product = product
		self.count = count

	# 比较两个购物项是否相等
	def __eq__(self,other):
		return self.id == other.id

	# 增加该种类商品购买的数量
	def addNum(self,num):
		self.count = self.count + num

	# 返回单项商品总价
	def amount(self):
		return self.product.price * self.count

# 测试代码
# if __name__ == '__main__':
# 	p1 = Product(1,'衣服1',1000)
# 	p2 = Product(1,'衣服2',2000)
# 	print p1 == p2
# 	#True

# 	pi1 = ProductItem(p1,2)
# 	pi2 = ProductItem(p2,1)
# 	print pi1 == pi2
# 	#True
	