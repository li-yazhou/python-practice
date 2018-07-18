def max_div(m,n):
    if m < n:
        m,n = n,m
    while(n != 0):
        r = m % n
        m = n
        n = r
    return m


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - r.p * self.q, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
        
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        return '%s/%s' %(self.p/max_div(self.p,self.q), self.q/max_div(self.p,self.q))
        
    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
