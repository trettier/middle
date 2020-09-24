def ft_max_num(a):
    n = 0
    while a > 0:
        if a % 10 > n:
            n = a % 10
        a //= 10
    return n
