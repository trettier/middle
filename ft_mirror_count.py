import ft_mirror_num

def ft_mirror_count(a):
    n = 0
    for i in range(1, a + 1):
        if ft_mirror_num.ft_mirror_num(i) == "TRUE":
            n += 1
    return n


#print(ft_mirror_count(10))
