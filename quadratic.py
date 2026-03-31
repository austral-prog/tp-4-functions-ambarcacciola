def roots(a, b, c):
    discriminante = (b**2 - 4*a*c)
    if discriminante < 0:
        raices = "( )"
    elif discriminante > 0:
        caso_uno = ((-b) + discriminante**0.5) / 2*a
        caso_dos = ((-b) - discriminante**0.5) / 2*a
        raices = f"({caso_uno}, {caso_dos})"
    else:
        raices = f"({((-b)) / 2*a})"
    return raices

def value_y(a, b, c, x):
    cuadratica = a*x**2 + b*x + c
    return cuadratica

def to_string(a, b, c):

    if a == 0 and b == 0:
        funcion = f"f(x) = {c}"
    elif a == 0 and c == 0:
        funcion = f"f(x) = {b} * X"
    elif b==0 and c == 0:
        funcion = f"f(x) = {a} * X^2"
    elif a == 0 and b != 0 and c != 0:
        funcion = f"f(x) = {b} * X + {c}"
    elif b == 0 and a != 0 and c != 0:
        funcion = f"f(x) = {a} * X^2 + {c}"
    elif c == 0 and a != 0 and b !=0:
        funcion = f"f(x) = {a} * X^2 + {b} * X"
    else:
        funcion = f"f(x) = {a} * X^2 + {b} * X + {c}"

    return funcion

def derivation(a, b, c):
    derivada = f"f'(x) = {2*a} * X + {b}"
    if a == 0:
        derivada = f"f'(x) = {b}"
    elif b == 0:
        derivada = f"f'(x) = {2*a} * X"
    return derivada"ANSWER HERE"
