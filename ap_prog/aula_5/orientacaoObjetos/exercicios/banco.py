class Cliente():
    def __init__(self, nome, endereco, cpf):
        self.__nome = nome 
        self.__endereco = endereco
        self.__cpf = cpf
        self.__situacao = False
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.nome__ = nome
    
    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self):
        self.__endereco = endereco
        
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self):
        self.__cpf = cpf 
        
class Conta():
    def __init__(self, nome, endereco, cpf, numero_conta):
        self.cliente = Cliente(nome, endereco, cpf)
        self.saldo = 0.0
        self.numero_conta = numero_conta
    
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor)->bool:
        if(self.saldo>=valor):
            self.saldo -= valor 
            return True
        return False
    
    def transferir(self, Conta, valor):
        teste = self.sacar(valor)
        if(teste==True):
            Conta.depositar(valor)
            
    def exibir_saldo(self):
        print("Cliente: " + self.cliente.get_nome())
        print(self.saldo)
        
conta_maria = Conta("Maria", "Rua 123 de oliverira 4", "123456789", 1)
print("Cliente: " + conta_maria.cliente.get_nome())

conta_jose = Conta("José", "Rua 123 de oliveira 4", "123456789", 2)
print("Cliente: " + conta_jose.cliente.get_nome())

conta_jose.depositar(1000)
conta_maria.depositar(2000)

conta_jose.sacar(500)
conta_maria.sacar(1000)

conta_maria.exibir_saldo()
conta_jose.exibir_saldo()

conta_jose.transferir(conta_maria, 100)

conta_maria.exibir_saldo()
conta_jose.exibir_saldo()
