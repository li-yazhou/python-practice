class Fib(object):

    def __init__(self, num):
        self.num = num

    def __str__(self):
        r_list = [0,1]
        for i in range(self.num-2):
            r_list.append(r_list[i] + r_list[i+1])
        return str(r_list)
    
    def __len__(self):
        return self.num

f = Fib(10)
print f
print len(f)
