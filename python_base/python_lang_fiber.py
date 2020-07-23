
def fiber1(n):
    a,b = 1,1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
   # print()


def fiber(n):
    a, b = 1,1
    i = 0
    while i < n:
        print(a, end=' ')
        a, b = b, a+b
        i = i + 1
        

def demo(a, b, c=6):
    print(a, b, c)
