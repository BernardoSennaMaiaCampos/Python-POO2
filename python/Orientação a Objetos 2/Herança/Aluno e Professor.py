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
    
