#Le Liste

# elenco = [2, 5, "bacon", 3.14, "eggs"]
#
# print(elenco)
# print(elenco[2])
# print(elenco[4])
# print(elenco[0])
# print(elenco[-2])
# print(type(elenco))

# elenco = [2, 5, "bacon", 3.14, "eggs", "asd", 55, 23]
# print(elenco[2:6])
# print(elenco[:6])
# print(elenco[2:])
# print(type(elenco))
#
# for elemento in elenco:
#     print(elenco)

# mia_lista = list(range(49, 155))
# # print(mia_lista)

altra_lista = [2, 5, "bacon", 3.14,["eggs", "asd", 55, 23]]
print(altra_lista[4][1])
altra_lista[1] = 6
print(altra_lista)

del altra_lista[1] # eliminare un elemento in una lista tramite indice
print(altra_lista)

altra_lista.remove(3.14)# eliminare un elemento in una lista tramite l elemento/valore
print(altra_lista)

altra_lista.append("spam") #aggiungere un elemento in una lista
print(altra_lista)

altra_lista.reverse() # inverte la lista
print(altra_lista)

lista_numerica = [3,2,6,7,1,77] #ordina una lista
lista_numerica.sort()
print(lista_numerica)