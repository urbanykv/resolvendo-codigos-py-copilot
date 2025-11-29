# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

input_num1 = float(input("Digite o primeiro número: "))
input_num2 = float(input("Digite o segundo número: "))
input_operacao = input("Digite a operação desejada (soma, subtracao, multiplicacao, divisao): ").lower()

def operacao_matematica(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Erro: Operação inválida."
    
resultado = operacao_matematica(input_num1, input_num2, input_operacao)
print("O resultado da operação é:", resultado)