
"""计算文本文件中最长行的长度"""
#方法一
def maxLen():
    f = open(r'f:\python文本文件.txt','r')
    allLineLens = [len(line.strip()) for line in f]  #strip()函数可以去掉字符串两端的空白字符
    longest = max(allLineLens)
    print(longest)
    f.close()

#方法二
def maxLen2():
    f = open(r'f:\python文本文件.txt','r')
    longest = max(len(line.strip()) for line in f)
    print(longest)
    f.close()


"""读取文本文件"""    
def readtext():
    f = open(r'f:\python文本文件.txt','r')
    for line in f:
        print(line)
    f.close()

    
"""计算字符串MD5值"""
import hashlib
import md5
def md5value():
    md5value = hashlib.md5()
    md5value.update('123')
    md5value = md5value.hexdigest()
    print(md5value)
    
    
