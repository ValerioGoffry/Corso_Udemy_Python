# Le Funzioni

# Funzione senza parametri
def print_tre_volte():
    print("Hello World")
    print("Hello World")
    print("Hello World")


print_tre_volte()


# Funzione con parametri
def my_max(a, b):
    if a == b:
        print("I numeri sono identici!")
    elif a > b:
        print("Il numero più grande tra i due è a: ", a)
    else:
        print("Il numero più grande tra i due è b: ", b)


my_max(10, 5)


# Funzione con parametri Opzionale
def macchina_nuova(produttore, modello, accessori=False):
    print("Acquisto macchina nuova; Caratteristiche: ")
    print("Produttore: ", produttore)
    print("Modello: ", modello)
    if accessori == True:
        print("La macchina è accessoriata!")


macchina_nuova("Tesla", "Model 3", accessori=True)


# Funzione con return
def sommatrice(x, y):
    risultato = x + y
    return risultato

print(sommatrice(3, 5))
