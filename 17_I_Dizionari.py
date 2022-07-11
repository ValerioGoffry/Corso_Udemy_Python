# I Dizionari

mio_dizionario = {"mia_chiave": "mio_valore", "età": 26, "pi greco": 3.14, "primi": [2, 3, 5, 7]}

# print(mio_dizionario)
# print(type(mio_dizionario))
# print(mio_dizionario["primi"])
# print(mio_dizionario["mia_chiave"])
# print(mio_dizionario["pi greco"])

# mio_dizionario["nazionalità"] = "italiana"
# print(mio_dizionario["nazionalità"])
#
# del mio_dizionario["mia_chiave"]
# print(mio_dizionario)
#
# mio_dizionario["mia_chiave"] = "mio_valore_n_2"
# print(mio_dizionario)
#
# print(mio_dizionario.keys())
# print(mio_dizionario.values())
# print(mio_dizionario.items())

# if "chiave_non_esistente" in mio_dizionario:
#     print(mio_dizionario["chiave_non_esistente"])
# else:
#     print("Chiave non trovata... ci spiace!")

# print(mio_dizionario.get("bacon", "Mi spiace, questa chiave non esiste"))

mio_dizionario.setdefault("bacon", "eggs")

print(mio_dizionario)


