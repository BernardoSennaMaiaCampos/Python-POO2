class personagemMarvel:
    def __init__(self, nome):
        self.nome=nome
    def __str__(self):
        return self.nome
personagem1 = personagemMarvel("Thor")

personagem2 = personagemMarvel("IronMan")
print(personagem1)
print(personagem2)