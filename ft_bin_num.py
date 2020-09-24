import ft_rev_num


def ft_bin_num(a):
    n = 0
    i = 1
    while a > 0:
        b = a % 2
        a //= 2
        n += b * i
        i *= 10
    return n

# print(ft_bin_num(6))
