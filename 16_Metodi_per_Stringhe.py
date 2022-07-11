a = [32, 11, 45]
b = [76, 99, 12]

x = "Veni Vidi "
z = "Vici"

# print(x[:4])
#
# caratteri_x = list(x)
# print(caratteri_x)
#
# print("V" in x)
# print("y" in x)
#
# print("Y" in a)
# print(32 in a)
#
# a.append(55)
# print(a)
#
# print(x.startswith(("V")))
# print(x.startswith(("Q")))
#
# print(x.endswith(" "))

nuova_s = "ALPHABRAVOCHARLIE"
nuova_s_b = "345121212123"

num_list = "34512-1231-17826311-123123"

new_one = num_list.split("-")
new_x = x.split(" ")
task = ["Pagare le bollette", "Portare a spasso il cane", "fare la spesa"]
compiti = ", ".join(task)
print("Oggi devo: ", compiti)


# print(nuova_s.isupper())
# print(nuova_s.upper())
#
# print(nuova_s.islower())
# print(nuova_s.lower())

print(nuova_s.isalpha())
print(nuova_s_b.isdecimal())

print(new_one)
print(x)

età = 25
# frase = "Io ho " + str(età) + " anni"
# print(frase)

frase = f"Io ho {età} anni"
print(frase, f"{età}")

