
def demo(*p):
    print(p)

def demo2(**p):
    for item in p.items():
        print(item)
        
def demo3(a, b, c):
    print(a + b + c)

def demo4(n = 10):
    global sum #是声明，而不可以在声明时直接赋值
    sum = 0
    for item in range(n):
        sum = sum + item
    return sum
