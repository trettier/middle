def ft_sum_num(a):
    n = a % 10
    while a > 0:
        a //= 10
        n += a % 10
    return n
