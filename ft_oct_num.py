def ft_oct_num(a):
    n = 0
    i = 1
    while a > 0:
        b = a % 8
        a //= 8
        n += b * i
        i *= 10
    return n


#print(ft_oct_num(8))