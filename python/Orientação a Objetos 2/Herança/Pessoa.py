# Exemplo – classe pai “Pessoa”
class Pessoa:
    num_pessoas = 0
    def __init__(self, nome, login, senha):
        self.__nome=nome
        self.__login=login
        self.senha=senha
        Pessoa.num_pessoas +=1
    def consulta_nome(self):
        return self.__nome
    def consulta_dados(self):
        record = 'nome:'+str(self.__nome) + ' - login:'+str(self.__login)
        return record