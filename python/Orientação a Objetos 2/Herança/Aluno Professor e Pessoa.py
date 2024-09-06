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
    
# Exemplo – classes herdadas de “Pessoa”
# classe Aluno
class Aluno(Pessoa): # Indica que a classe Aluno herda da classe Pessoa
    def __init__(self, nome, login, senha, curso):
        super().__init__(nome, login, senha) # Invoca o método init da super classe (ou classe base, Pessoa).
        self.__curso=curso
 
    def consulta_curso(self):
        return self.__curso
# classe Professor
class Professor(Pessoa): # Indica que a classe Professor herda da classe Pessoa
    def __init__(self, nome, login, senha, titulacao):
        super().__init__( nome, login, senha) # Invoca o método init da super classe (ou classe base, Pessoa).
        self.__titulacao=titulacao
    def consulta_titulacao(self):
        return self.__titulacao

aluno1 = Aluno('Victor','victor@rj.senac.br', '12345', 'Programação')
aluno2 = Aluno('Thamires','thamires@rj.senac.br', '12345', 'Banco de Dados I')
prof1 = Professor('Roberto', 'roberto.harkovsky@rj.senac.br', '12345', 'MsC')
print(aluno1.consulta_dados())
print(aluno1.consulta_curso())
print(aluno2.consulta_dados())
print(aluno2.consulta_curso())
print(prof1.consulta_nome())
print(prof1.consulta_titulacao())   