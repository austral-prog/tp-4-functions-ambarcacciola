# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0

# ---- Función a implementar ----

def classify_number(n):
    if n == 0:
        ans = f"zero"
    elif is_positive(n):
        if is_even(n):
            ans = f"positive even"
        else:
            ans = f"positive odd"
    else:
        if is_even(n):
            ans = f"negative even"
        else:
            ans = f"negative odd"
    return ans
