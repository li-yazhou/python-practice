answer = "python"
temp = input('这是什么语言？')
while True:
    if temp == answer:
        print("猜对了")
        break
    else:
        temp = input('这是什么语言？')
