import math 


def cos_taylor(x, terms=10):
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        result += term
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

x = float(input("Για πόσες μοίρες θές να βρεις το τόξο εφαπτομένης: "))
