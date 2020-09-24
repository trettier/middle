import ft_len_num


def ft_mirror_num(a):
    n = ft_len_num.ft_len_num(a)
    i = 10 ** (n - 1)
    if n % 2 == 1:
        for j in range((n - 1) // 2):
            if a % 10 != (a // i) % 10:
                return "FALSE"
            i //= 100
            a //= 10
        return "TRUE"
    for j in range(n // 2):
        if a % 10 != (a // i) % 10:
            return "FALSE"
        i //= 100
        a //= 10
    return "TRUE"


#print(ft_mirror_num(1))
