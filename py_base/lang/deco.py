def deco(func):
    def in_deco(x,y):
        print 'in deco'
        func(x,y)
    print 'call deco'
    return in_deco

@deco
def bar(x,y):
    print 'in bar' , x + y

bar(1,2)
