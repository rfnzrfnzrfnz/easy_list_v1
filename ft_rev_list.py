def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return (l)


def ft_rev_list(mass):
    x = []
    for i in range(ft_len(mass) - 1, -1, -1):
        x += [mass[i]]
    return x
