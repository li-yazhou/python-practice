##endFlag = 'yes'
##sum = 0
##while endFlag.lower() == 'yes':
##    x = input('输入一个（1,100）之间的整数')
##    if x.isdigit():
##        x = int(x)
##        if  0 < x < 100:
##            sum = sum + x
##        else:
##            print('输入的整数不在范围内')
##    else:
##         print('请输入整数')
##    endFlag = input('继续输入？（yes or no）')
##result = '输入数字之和是：%d' %(sum)
##print(result)


sum = 0
while True:
    x = input('输入一个（1,100）之间的整数,终止计算请输入"yes"')
    if(x.lower() == "yes"):
       break
    if x.isdigit():
        x = int(x)
        if  0 < x < 100:
            sum = sum + x
        else:
            print('输入的整数不在范围内')
    else:
        print('请输入整数')
result = '输入数字之和是：%d' %(sum)
print(result)

