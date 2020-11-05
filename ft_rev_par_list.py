def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return (l)


def ft_rev_par_list(mass):
    if ft_len(mass) % 2 == 0:
        for i in range(1, ft_len(mass), 2):
            mass[i], mass[i - 1] = mass[i - 1], mass[i]

    else:
        for i in range(0, ft_len(mass) - 1, 2):
            mass[i], mass[i + 1] = mass[i + 1], mass[i]
    return mass
