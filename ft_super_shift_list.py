def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return (l)


def ft_rshift_list(mass):
    c = mass[-1]
    for i in range(ft_len(mass)):
        i = ft_len(mass) - i - 1
        mass[i] = mass[i - 1]
    mass[0] = c
    return mass


def ft_super_shift_list(mass, n):
    if n > 0:
        for i in range(n):
            mass = ft_rshift_list(mass)
        return mass
    else:
        for i in range(ft_len(mass) + n):
            mass = ft_rshift_list(mass)
        return mass
