# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    vocales = count_vowels(text)
    consonantes = count_consonants(text)
    total = vocales + consonantes
    return total

def vowel_percentage(text):
    if total_letters(text) !=0:
        porcentaje = (count_vowels(text) / total_letters(text)) * 100
        return round(porcentaje, 1)
    else:
        return 0.0

def analyze_text(text):
    string = f"V:{count_vowels(text)} C:{count_consonants(text)} T:{total_letters(text)} P:{vowel_percentage(text)}%"
    return string
