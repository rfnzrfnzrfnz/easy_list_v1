def ft_len(str):
    n = 0
    for i in str:
        n += 1
    return (n)


def ft_even_parts_list(mass):
    n = ft_len(mass)
    c = []
    for i in range(0, n):
        elem = mass[i]
        index = i
        if elem % 2 == 0:
            c += [elem]

    return c
