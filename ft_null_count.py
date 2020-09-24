def ft_null_count(a):
    n = 0
    while a > 0:
        if a % 10 == 0:
            n += 1
        a //= 10
    return n

# print(ft_null_count(1020))
