# Ereditariet√†

class AnimaleDomestico:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def mangia(self):
        print(self.nome, "sta mangiando!")

    def dormi(self):
        print(self.dormi, "sta dormendo!")


class Cane(AnimaleDomestico):

    def __init__(self, nome, anni, razza):
        super().__init__(nome, anni)
        self.razza = razza

    def abbaia(self):
        print(self.nome, "sta abbaiando!")


class Gatto(AnimaleDomestico):

    def __init__(self, nome, anni, tipo):
        super().__init__(nome, anni)
        self.tipo = tipo

    def fusa(self):
        print(self.nome, "sta facendo le fusa!")


mio_gatto = Gatto("Palla", 2, "Maschio")
mio_cane = Cane("Charlie", 4, "Maremmano")

mio_gatto.fusa()
mio_gatto.mangia()

mio_cane.dormi()
mio_cane.abbaia()

print(type(mio_cane))
print(type(mio_gatto))
