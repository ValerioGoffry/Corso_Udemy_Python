def funzione_cerca_palindromi(parola):
    nuova_parola = ""
    try:
        indice = (len(parola) - 1)
        while indice >= 0:
            nuova_parola += parola[indice]
            indice -= 1
    except:
        print("Parametro non valido!")
    else:
        if nuova_parola == parola:
            print(f"SI! La parola '{parola}' è un palindromo!")
        else:
            print(f"NO! La parola '{parola}' non è un palindromo!")


# parola = input("Funzione Cerca-Palindromi: Inserisci la parola da analizzare -> ")
funzione_cerca_palindromi(22)
