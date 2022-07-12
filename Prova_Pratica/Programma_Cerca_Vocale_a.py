def cerca_vocali(messaggio):
    lista_vocali = ["a", "e", "i", "o", "u"]
    if messaggio in lista_vocali:
        messaggio = f"Il carattere '{messaggio}' è una vocale!"
    else:
        messaggio = f"Il carattere '{messaggio}' non è una vocale!"
    return messaggio

messaggio = str(input("Funzione Cerca-Vocali: Inserisci il carattere da analizzare --> "))
print(cerca_vocali(messaggio))
