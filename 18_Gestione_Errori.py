# Gestioni Errori

def divisore(x, y):
    try:
        risultato = x / y
        # print(risultato)
    except TypeError:
        print("Hai inserito un tipo di dato non corretto!")
    except ZeroDivisionError:
        print("Hai eseguito una divisione per zero!")
    except:
        print("I dati inseriti non sono supportati!")
    finally:
        print("Questo codice verrà eseguito in ogni caso!")
    # else:
    #     print(risultato)


divisore(9, 3)
