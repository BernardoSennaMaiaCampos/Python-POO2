class Empregado:
# Variavel de Classe
    company_name = 'ACME'
# constructor 
    def __init__(self, nome, salario):
    # Variaveis de instancia
        self.nome = nome
        self.salario = salario
# instance method
    def show(self):
        print('Empregado:', self.nome, self.salario, self.company_nome)
emp1 = Empregado("Bob", 12000)
emp1.show()