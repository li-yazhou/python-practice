#coding=utf-8
# print ('aaa')
# print '123'

# print 1.1/2
# print 1.1//2

# print('axxxx')

# content
# start.py  end
# start.java  end
# start.c end
# C
# Java 
# Python

# def find_start_start(fname):
# 	f = open(fname)
# 	for line in f:
# 		if line.startswith('start'):
# 			print line
# # find_start_start('test.txt')

# def find_in_start_end(fname):
# 	f = open(fname)
# 	for line in f:
# 		if line.startswith('start') and line[:-1].endswith('end'):  # 去掉换行符
# 			print line
# #find_in_start_end('test.txt')	

# import re
# pa = re.compile(r'first')
# ma = pa.match('first re')
# print ma.group()	# first 所要匹配的字符串
# print ma.span()  	# (0, 5) 所在位置
# print ma.string		# first re  原字符串
# print ma.re			# <_sre.SRE_Pattern object at 0x013BB840> 编译对象

# print '----------------\n'

# pa1 = re.compile(r'first',re.I)  # re.I Ignore忽略大小写
# ma1 = pa1.match('First re match')
# print ma.group()
# print ma.span()

import urllib2
req = urllib2.urlopen('http://www.imooc.com/course/list')
buf = req.read()
print buf
print '\n----------------\n'
import re
listurl = re.findall(r'http:.+\.jpg', buf)
print listurl

i = 0
for url in listurl:
	f = open(str(i) + '.jpg', 'w')
	req = urllib2.urlopen(url)
	buff = req.read()
	f.write(buff)
	i += 1
