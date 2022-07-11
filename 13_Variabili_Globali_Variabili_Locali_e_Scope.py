#Variabili Globali , Variabili Locali e Scope

x = 50 #Questa è una variabile

def mia_funzione():
    # global x
    #x = 50 è una variabile locale perchè sta in una funzione
    z = x
    z += 50
    return z

print(mia_funzione())
# print(z)

