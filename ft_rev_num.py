import ft_len_num

def ft_rev_num(a):
    n = 0
    i = ft_len_num.ft_len_num(a)
    i = 10 ** i // 10
    while a > 0:
        n += (a % 10) * i
        i //= 10
        a //= 10
    return n
