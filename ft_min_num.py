def ft_min_num(a):
    n = 10
    if a == 0:
        return 0
    while a > 0:
        if a % 10 < n:
            n = a % 10
        a //= 10
    return n


#print(ft_min_num(4351364))