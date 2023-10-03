# Paradigma da linguagem orientada à objetos ~
A ideia da orientação a objetos pe desenvolver programas baseados em objetos do mundo real.
Para onde você olhar irá se deparar com objetos, sejam eles animados ou inanimados: pessoas, animais,
carros, motos, etc.
Os objetos possuem:
- Características - tamanho, forma, cor, etc
- Comportamentos – andar, falar, comer, etc. 

Na linguagem O.O a unidade de programação é a classe a partir do qual os objetos são instanciados (criados)

## Classes
A classe é o projeto para a crisção de objetos
- Atributos (variáveis) que são as cracterísticas 
- Métodos (semelhantes a funções) que são os comportamentos do objeto a ser criado

Seguindo um modelo inpirado numa receita de bolo temos:
- Classe = receitas 
- Objeto = bolo
levando em conta que: pode-se fazer muitos bolos com uma única receita, não comemos o bolo e sim a receita.

Para definir uma classe em python, basta utilizar a palava 'class' - por covenção, classes são sempre definidas com maiúsculas. Em caso de nome composto utilizamos o camelCase. 
ex:
```
class Cliente():
```

## Declaração de atributos
Para declarar os atributos de uma classe, basta especificar o nome do atributo por meio de variáveis em um método construtor.
ex:
```
def __init__(self, nome, endereco, cpf):
    self.nome = nome
    self.endereco = endereço
    self.cpf = cpf
```
O contrutor é o método de inicialização do objeto.
nota: O método '__init__' define o contrutor da classe, ou seja, é onde definimos como uma nova pessoa seria criada no programa.


## Objetos 
Para instância de objetos, evocamos a classe e passamos os valores para os atributos definidos no construtor. 
ex:
```
cliente_jose = Cliente("José", "Rua 123 de oliveira 4", "123456789")
print("Cliente: " + cliente_jose.nome)
print("Endereço: " + cliente_jose.endereco)

cliente_maria = Cliente("Maria", "Rua 123 de oliveira 4", "123456789")
print("Cliente: " + cliente_maria.nome)
print("Endereço: " + cliente_maria.endereco)
```


## Declaração de métodos 
Os métodos são declarados por meio de funções. Imaginando que cada cliente criado tem um atributo "situação" que é definido com o valor booleano False no construtor. 
ex:
```
class Cliente():

    def __init__(self, nome, endereco, cpf):
    self.nome = nome
    self.endereco = endereco 
    self.cpf = cpf
    self.situacao = false
```
Vamos precisar de métodos para ativar e desativar o cliente quando necessário. 
ex:
```
def ativar(self):
    self.situacao = True
    print("Cliente: ", self.nome + "ativado(a) com sucesso.")

def desativar(self):
    self.siuacao = False
    print("Cliente: ", self.nome + "desativado(a) com sucesso.")
```


## Execução de métodos
Para executar, basta usar a variável que guarda a referência ao objeto e chamar/evocar o metódo escolhido. 
ex:
```
cliente_jose = Cliente("José", "Rua 123 de oliveira 4", "123456789")
print("Cliente: " + cliente_jose.nome)
print("Endereço: " + cliente_jose.endereco)

cliente_jose.ativar()

cliente_maria = Cliente("Maria", "Rua 123 de oliveira 4", "123456789")
print("Cliente: " + cliente_maria.nome)
print("Endereço: " + cliente_maria.endereco)

cliente_maria.ativar()
```


## Encapsulamento
Podemos encapsular (proteger) os atributos de uma classe, desse mode só é possivél manipular os atributos através de regras bem definidas implementadas nos métodos>

Existem 3 tipos de modificadores de acessor nas linguagens arientadas a objetos, que são:
> 
