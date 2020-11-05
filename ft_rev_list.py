def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return (l)


def ft_rev_list(mass):
    c = ft_len(mass)
    for i in range(0, c // 2):
        a = mass[i]
        mass[i] = mass[-i - 1]
        mass[-i - 1] = a
    return mass
