"""
Esercizio 001: Max tra Due Numeri
Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.
"""


def max_tra_due_numeri(a, b):
    if a == b:
        print("I numeri sono identici")
    elif a > b:
        print("a è più grande di b ")
    else:
        print("b è più grande di a ")



max_tra_due_numeri(20,2)

