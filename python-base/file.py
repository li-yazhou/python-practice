
def readtextfile():
    f = open('F:\\python文本文件.txt','r')
    while True:
        line = f.readline()
        if line == '':
            break
        print(line)
    f.close()

def readtextfile2():
    f = open('F:\\python文本文件.txt','r')
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()

import pickle 
def writeBinFile():
    f = open(r'F:\binary.bat','wb')
    n = 7  #表示后面要写入的文件个数
    i = 130000
    a = 99.0001
    s = '小周周'
    aList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    aTuple = (-15,12,56)
    coll = {1, 3, 5}
    dic = {'a':1, 'b':2, 'c':3}
    try:
        pickle.dump(n,f)  #表示后面要写入的文件个数
        pickle.dump(i,f)  #把i转换成字节串，并写入文件
        pickle.dump(a,f)
        pickle.dump(s,f)
        pickle.dump(aList,f)
        pickle.dump(aTuple,f)
        pickle.dump(coll,f)
        pickle.dump(dic,f)
    except:
        print('写入二进制文件异常')
    finally:
        f.close()

def readBinFile():
    f = open(r'F:\binary.bat','rb')
    n = pickle.load(f)  #读出文件的数据个数
    count = 0
    while count < n:
        x = pickle.load(f)
        print(x)
        count += 1
    f.close()


import struct
def writeBinFileByStruct():
    n = 100001
    x = 19.00012
    b = True
    s = 'python'
    sn = struct.pack('if?',n,x,b)  #把整数n、浮点数x、布尔对象b依次转换为字节串
    f = open(r'F:\binary2.bat','wb')
    f.write(sn)  #写入字节串
    #f.write(s)   #字符串可以直接写入
    f.close()

def readBinFileByStruct():
    f = open(r'F:\binary2.bat','rb')
    sn = f.read(9)
    tu = struct.unpack('if?',sn)  #从字节sn中还原出1个整数、1个浮点数和1个布尔值，并返回元组
    print(tu)
    n = tu[0]
    x = tu[1]
    b = tu[2]
    print('n=',n)
    print('x=',x)
    print('b=',b)
    #  = f.read(9)
    f.close()
    #print('s=',s)

        
