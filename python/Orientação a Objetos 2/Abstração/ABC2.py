from abc import ABC, abstractmethod
class Absclass(ABC): # Classe abstrata
    def print(self,x):
        print("Valor passado: ", x)
    @abstractmethod
    def task(self):
        pass

class teste_class(Absclass): # classe herdada de classe abstrata Absclass
    def task(self):
        print("Dentro de test_class task")

class exemplo_class(Absclass): # classe herdada de classe abstrata Absclass
    def task(self):
        print("Dentro de example_class task")
