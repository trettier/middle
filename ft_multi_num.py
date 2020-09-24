def ft_multi_num(a):
    n = 1
    if a == 0:
        n = 0
    while a > 0:
        n *= a % 10
        a //= 10
    return n
