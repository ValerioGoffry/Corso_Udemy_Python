# I Decoratori

def funzione_decoratore(funzione_parametro):
    def wrapper():
        print("... codice da eseguire prima di funzione_parametro ...")
        funzione_parametro()
        print("... codice da eseguire dopo la funzione_parametro ...")

    return wrapper()


@funzione_decoratore
def mia_funzione():
    print("Hello World")


# mia_funzione = funzione_decoratore(mia_funzione)
mia_funzione()
