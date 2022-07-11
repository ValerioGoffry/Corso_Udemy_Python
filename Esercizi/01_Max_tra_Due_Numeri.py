"""
Esercizio 001: Max tra Due Numeri
Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.
"""


def max_tra_due_numeri(a, b):
    if a == b:
        print("I numeri sono identici")
    elif a > b:
        print("Il numero a:", a, "è più grande del numero b:", b)
        return a
    else:
        print("Il numero b:", b, "è più grande del numero a:", a)
        return b


max_tra_due_numeri(20, 2)
