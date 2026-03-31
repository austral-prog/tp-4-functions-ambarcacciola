def max_of_two(x, y):
    if x > y:
        maximo = x
    else:
        maximo = y
    return maximo


def max_of_three(x, y, z):
    if x > y and x > z:
        maximo = x
    elif y > x and y > z:
        maximo = y
    else:
        maximo = z
    return maximo
