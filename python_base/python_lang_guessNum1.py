print('猜数字游戏！')
temp = input("你猜的数字是：\n")
num = int(temp)
while num != 8:
    if(num > 8):
        print("大了，大了，请重新猜：")
    else:
        print("小了，小了，请重新猜：")
    temp = input()
    num = int(temp)
print("恭喜你!猜对啦！！！")    
