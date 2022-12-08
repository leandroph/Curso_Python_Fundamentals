'''
3) Escreva um script em Python que receba dois números e que seja realizado as seguintes
operações:
• soma dos dois números
• diferença dos dois números
O resultado deverá ser apresentado conforme a seguir - no exemplo foram digitados os números
4 e 2:

------------------------------
Soma: 4 + 2 = 6
Diferença: 4 - 2 = 2
'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
diferenca = numero1 - numero2

print("----------------------------")
print(f"Soma: {numero1} + {numero2} = {soma}")
print(f"Diferença: {numero1} - {numero2} = {diferenca}")
print("----------------------------")
