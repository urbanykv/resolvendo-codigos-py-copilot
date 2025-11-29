# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

input1 = input("Digite o primeiro dado: ")
input2 = input("Digite o segundo dado: ")

def concatena_dados(dado1, dado2):
    return str(dado1) + str(dado2)

print("Dados concatenados:", concatena_dados(input1, input2))