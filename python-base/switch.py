def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

operator = {'+':add, '-':sub, '*':mul, '/':div}

def compute(x,o,y,*args,**kwords):
    return operator.get(o)(x,y)

x = 1
y = 2
o = '/'
result = {
    '+': x + y,
    '-': x - y,
    '*': x * y,
    '/': x / y
    }
print(result.get(o))

