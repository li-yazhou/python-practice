# -*- coding: utf-8 -*-
from Product import Product

class ProductItem(object):
	def __init__(self,product,count=1):
		self.id = product.id
		self.product = product
		self.count = count

	# 比较两个购物项是否相等
	def __eq__(self,other):
		return self.id == other.id

	## 可以直接从购物车中取出并运算
	# 增加该种类商品购买的数量
	# def addNum(self,num):
	# 	self.count = self.count + num

	# 返回单项商品总价
	def amount(self):
		return self.product.price * self.count

	# 打印对象
	def __str__(self):
		s = 'product`s No is ' + str(self.id) + \
			', \t product name is ' + self.product.name + \
			', \t price per product is ' + str(self.product.price) + \
			', \t product number is ' + str(self.count) + \
			', \t amount is ' + str(self.amount())
		return s

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
	