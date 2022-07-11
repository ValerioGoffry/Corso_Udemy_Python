# Tuple e set
# tuple lista dove non si possono cancellare gli elementi

a = (2, 3, 5, 7, 11)
b = 7, 1, 90, 3

print("a:", type(a))
print("b:", type(a))

print(a[0])

# set deve avere elementi unici
lista_a = [2, 3, 4, 2, 4, 5, 6, 7]
unici = set(lista_a)
print(type(unici))
print(unici)
unici.add(46)
print(unici)
