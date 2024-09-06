# Importar a classe date do módulo datetime para trabalhar com datas
from datetime import date
# Define uma classe chamada "Pessoa" para representar uma pessoa com atributos # de nome, país e data de nascimento
class Pessoa:
    # Inicialize o objeto Pessoa com um nome, país e data de nascimento
    def __init__(self, nome, pais, dataNasc):
        self.nome = nome
        self.pais = pais
        self.dataNasc = dataNasc

# Calcula a idade da pessoa com base na data de nascimento
    def calcula_idade(self):
        hoje = date.today()
        idade = hoje.year - self.dataNasc.year
        if hoje < date(hoje.year, self.dataNasc.month, self.dataNasc.day):
            idade -= 1
        return idade
# imprime dados da pessoa
    def imprime_dados(self):
        print("Nome:", self.nome)
        print("pais:", self.pais)
        print("Data de nascimento:", self.dataNasc)
        print("idade:", self.calcula_idade())