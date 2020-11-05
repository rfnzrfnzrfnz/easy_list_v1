def ft_len(str):
    n = 0
    for i in str:
        n += 1
    return (n)


def ft_same_parts_list(mass):
    n = ft_len(mass)
    c = 0
    for i in range(1, n):
        index = i
        if mass[i] * mass[i - 1] > 0:
            return True
    return False
