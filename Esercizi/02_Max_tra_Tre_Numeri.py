"""Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!"""


def max_tra_tre_Numeri(input):
    a = int(input("Scrivi il primo numero: "))
    b = int(input("Scrivi il secondo numero: "))
    c = int(input("Scrivi il terzo numero: "))
    print("Il primo numero è:", a, "\nIl secondo numero è:", b, "\nIl terzo numero è:", c)

    if a == b == c:
        print("I numeri sono identici.")
    elif a >= b and a >= c:
        print("Il numero più grande è a:", a)
        return a
    elif b >= a and b >= c:
        print("Il numero più grande è b:", b)
        return b
    else:
        print("Il numero più grande è c:", c)
        return c

max_tra_tre_Numeri(input)
