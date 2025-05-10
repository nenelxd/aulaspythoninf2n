# idade1 = int(input('Digite a idade 1: '))
# idade2 = int(input( 'Digite a idade 2: '))

# print(f'''
#       idades iguais? {idade1==idade2}
#       Idade 1 é maior que a idade 2? {idade1 > idade2}
#       Idade 2 é menor que a idade 2? {idade1 < idade2}
#       ''')

# # Atividade 2
# palavra1 = input('Digite a 1ª palavra: ')
# palavra2 = input('Digite a 2ª palavra: ')

# print(f'São iguais:? {palavra1==palavra2}')

#Condicionais 

# if 5 < 4:
#     print('É maior')
# elif 10 < 3:
#     print('Olá')
# else:
#     print('igual')

# numero = float(input('Digite um número: '))

# if numero %2 == 0:
#     print('Esse número é par')
# else:
#     print('Esse número é ímpar')

#Atividade 2 

# nota = float(input('Digite uma nota: '))

# if nota >= 6:
#     print('Aprovado')
# else:
#     print('Reprovado')  

#Atividade 12

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))

# imc = (peso / altura **2)

# if peso / altura **2 <= 18:
#     print('Abaixo do peso')
# elif peso / altura **2 <= 24:
#     print('Peso normal')
# elif peso / altura **2 <= 29:
#     print('Sobrepeso')
# elif peso / altura **2 <= 34:
#     print('Obesidade 1')
# elif peso / altura **2 <= 39:
#     print('Obesidade 2')
# else:
#     print('Obesidade 3')

# print(imc)

# professor 

peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 19.1:
    print('Abaixo do peso')
elif 19.1 <= imc < 25.8:
    print('Peso normal')
elif 25.8 <= imc < 27.3:
    print('Pouco acima do peso')
elif 27.3 <= imc < 32.3:
    print('Acima do peso')
else:
    print('Obesidade')

print(f'{imc:.2f}')