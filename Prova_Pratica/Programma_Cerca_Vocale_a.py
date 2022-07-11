def cerca_vocali(input):
    a = str(input("Funzione Cerca-Vocali: Inserisci il carattere da analizzare --> "))
    lista_vocali = ["a", "e", "i", "o", "u"]
    if a in lista_vocali:
        print(f"Il carattere {a} è una vocale")
    else:
        print(f"Il carattere {a} non è una vocale")


cerca_vocali(input)
