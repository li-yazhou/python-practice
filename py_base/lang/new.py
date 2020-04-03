class Capstr(str):
    # 重写 __new__()函数
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls,string)

class Test:
    def __init__(self):
        print('__init__方法被调用')

    def __del__(self):
        print('__del__方法被调用')

class New_int(int):
    # 重写__add__()函数
    def __add__(self,other):
        return int.__sub__(self,other)

    # 覆写__sub__()函数
    def __sub__(self,other):
        return int.__add__(self,other)

class Nint(int):
    def __radd__(self,other):
        return int.__sub__(self,other)


from tkinter import *

master = Tk()

v = IntVar()
v.set(2)

Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)
Radiobutton(master, text="Three", variable=v, value=3).pack(anchor=W)

mainloop()
