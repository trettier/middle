def ft_hex_num(a):
    n = 0
    i = 1
    while a > 0:
        b = a % 16
        a //= 16
        n += b * i
        i *= 10
    return n
