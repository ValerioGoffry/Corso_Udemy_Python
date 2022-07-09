#Controllo del Flusso
#IF
#ELIF
#ELSE

età = 18
patente = False
# età = int(input("Quanti anni hai? "))
# print("Hai", età, "anni")
# patente = str(input("(Rispondi solo con True o False) \nHai la patente? "))


#IF
print("--- IF  ---")
if età >= 18:
    print("Sei Maggiorenne")

# ELSE
print("--- ELSE  ---")
if età >= 18:
    print("Sei Maggiorenne")
else:
    print("Sei minorenne")

# ELIF
print("--- ELIF ---")

if età >= 18 and patente == True:
    print("Puoi noleggiare una Ferrari!")
elif età >= 18 and patente == False:
    print("Niente patente...niente Ferrari")
else:
    print("Torneremo a parlare di macchina da corsa tra qualche anno...")


