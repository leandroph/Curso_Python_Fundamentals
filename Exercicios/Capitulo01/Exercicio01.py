'''
1) Em muitos programas, nos é solicitado o preenchimento de algumas informações como
nome, CPF, idade e unidade federativa. Escreva um script em Python que solicite as
informações cadastrais mencionadas e que em seguida as apresente da seguinte forma:

-----------------------------
Confirmação de cadastro:
Nome: Guido Van Rossum
CPF: 999.888.777/66
Idade: 65
-----------------------------
'''

nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
idade = input("Digite sua idade: ")
unidade_federativa = input("Digite sua unidade federativa: ")

print("----------------------------")
print("Confirmação de cadastro:")
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Idade: {idade}")
print(f"Unidade Federativa: {unidade_federativa}")
print("----------------------------")