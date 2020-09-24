def ft_second_max_num(a):
    n = 0
    n1 = 0
    while a > 0:
        if a % 10 > n:
            n1 = n
            n = a % 10
        if a % 10 == n:
            n1 = n
        a //= 10
    return n1
