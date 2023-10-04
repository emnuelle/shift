class Cliente():
    def __init__(self, nome, endereco, cpf, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_endereco(self):
        return  self.__endereco
    def set_endereco(self, endereco):
        self.__endereco = endereco
    def get_cpf(self):
        return self.__cpf
    def set_cpf(self, cpf):
        self.__cpf = cpf
    def get_telefone(self):
        return self.__telefone
    def set_telefone(self, telefone):
        self.__telefone = telefone

class Conta():
    def __init__(self,numero, saldo ,nome, endereco, cpf, telefone):
        self.cliente = Cliente(nome, endereco, cpf, telefone)
        self.numero = numero
        self.saldo = saldo


cliente_jose = Conta("001","0", "Jose", "Rua Dez ","33906244814","11964366590")