def ft_len(str):
    n = 0
    for i in str:
        n += 1
    return (n)


def ft_positive_list(mass):
    n = ft_len(mass)
    c = 0
    for i in range(0, n):
        elem = mass[i]
        index = i
        if elem > 0:
            c += 1

    return c
