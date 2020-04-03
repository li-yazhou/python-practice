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
	