def funzione_cerca_vocali(carattere):
    vocali = ["a", "e", "i", "o", "u"]
    if carattere in vocali:
        messaggio = f"Il carattere '{carattere}' è una vocale!"
    else:
        messaggio = f"Il carattere '{carattere}' non è una vocale!"
    return messaggio

carattere = str(input("Funzione Cerca-Vocali: Inserisci il carattere da analizzare --> "))
print(funzione_cerca_vocali(carattere))
