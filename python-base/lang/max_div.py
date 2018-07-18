def max_div(m,n):
    if m < n:
        m,n = n,m
    while(n != 0):
        r = m % n
        m = n
        n = r
    return m
