# No slide nomeado como 'loop_while.py'

print("Por favor, insira seu nome de usuário")
username = input()
print("Por favor, insira sua senha")
password = input()

login_realizado = False
tentativas = 0

while(login_realizado is False):
    tentativas = tentativas + 1
    if(username.upper() == "ADMIN" and password.upper() == "123"):
        print("Você está logado no sistema")
        login_realizado = True
    else:
        print("Dados de acesso incorretos")
        print("Por favor, insira seu nome de usuário")
        username = input()
        print("Por favor, insira sua senha")
        password = input()
print(f"Para acessar o sistema foram utilizadas {tentativas} tentativas!")
