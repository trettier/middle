def ft_len_num(a):
    n = 0
    while a > 0:
        a //= 10
        n += 1
    return n
