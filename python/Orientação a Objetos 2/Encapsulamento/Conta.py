class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
    def consulta_saldo(self):
        return self.__saldo
conta1234 = Conta(1234, 750.84)
conta1234.consulta_saldo()

