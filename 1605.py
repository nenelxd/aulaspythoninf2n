# def saudacao(nome):
#     mensagem = "Olá, " + nome
#     print(mensagem)

# saudacao("Lucas")

# def calcular_media(n1, n2, n3):
#     media = (n1 + n2 + n3) / 3
#     print(f"A média é: {media:.0f}")

# calcular_media(7, 8, 9)


# def verificar_par_impar(numero):
#     if numero %2 == 0:
#         print("Número par")
#     else:
#         print("Número impar")

# verificar_par_impar(7)

# def contar_ate(n):
#     i = 1
#     while n <= i:
#         i + 1
#         print(i)

# contar_ate(5)


##### CONTAGEM DE 1 ATÉ 10

# contar = 1

# while contar <= 10:
#     print(contar)
#     contar += 1


##### SOMA DE NUMEROS ATE 100

# total = 0
# num = 1

# while num <= 100:
#     total += num
#     num += 1
# print(f"A soma dos números de 1 a 100 é: {total}")

#### TABUADA DE UM NUMERO

# numero = int(input("Digite um número: "))
# total = 0

# while total <= numero * 10:
#     print (total)
#     total += numero

#CONTAGEM REGRESSIVA - FELIZ ANO NOVO

# i = 10

# while i >= 0:
#     print(i)
#     i -= 1
# print("Feliz Ano Novo")

###### CONTAGEM ATÉ NÚMERO INSERIDO, EXIBINDO APENAS OS IMPARES

# numero = int(input("Insira um número: "))
# total = 1

# while total != numero:
#     if total %2 != 0:
#         print(total)
#     total += 1
# if total %2 != 0:
#     print(total)


### Somar números até digitar um número negativo, em seguida exibir a quantidade de números positivos digitados.

# numero = int(input("Digite um número: "))


# while numero >= 0:
#         if numero >= 0:
#                 print(numero)
#                 numero += int(input("Insira outro número: "))
#         else:
#                 print("Número negativo")



# numero = int(input("Digite um número: "))
# total = 0

# while numero >=0:
#         total += numero
#         numero = int(input("Digite um número: "))
# print(f"Você digitou um número negativo, o acumulado foi {total}")

## Mostrar tabuada de um numero, porem apenas os multiplos de 3

# numero = int(input("Digite um número: "))
# total = 1
# soma = 0

# while total <= 10:
#         soma = numero * total
#         if soma %3 == 0:
#                 print(f"{numero} * {total} = {soma}")
#         total += 1


####### Digitar notas até digitar "-1", após parar contabilizar o número de notas e a média final.

# nota = float(input("Insira uma nota: "))
# total = 0
# alunos = 0 

# while nota != -1:
#     total += nota
#     alunos += 1
#     nota = float(input("Insira uma nota: "))
# if alunos > 0:
#     media = total / alunos
#     print(f"Foram contabilizadas {alunos} notas e a média geral é de  {media}")
# else:
#     print("Nenhuma nota foi digitada") 

###### Contagem de números de 1 a 10, chegando a 10 para.

# contagem = 1

# while contagem <= 10:
#     print(contagem)
#     contagem += 1

###### Soma de números consecutivos iniciando em 1 até atingir ou ultrapassar 50

# numero = 1
# total = 0

# while total < 50:
#     total += numero
#     numero += 1

# print(f"Soma final: {total}")
# print(f"(Último número somado: {numero - 1})")


# ####### Entrada válida de números entre 1 e 10

# entrada = int(input("Digite um número de 1 a 10: "))

# while entrada > 10 or entrada < 1:
#     entrada = int(input("Número inválido, tente novamente: "))
# print("Você digitou um número válido")





############### AULA 1705

# numero = 1
# total = 0

# while numero <= 100:
#     total += numero
#     numero += 1
# print(f"A soma dos números é {total}")


# numero = int(input("Digite um número: "))
# total = 0

# while total <= 10:
#     print(f"{numero} x {total} = {numero * total}")
#     total += 1

################## RESOLVER
# numero = 15
# palpite = ''
# while palpite!=numero:
#     int(input("Digite um número: "))
#     if palpite>numero:
#         print("O número é maior que o escolhido")
#     elif palpite<numero:
#         print("O número é menor que o escolhido")
#     else:
#         print(f"Você acertou o número é {numero}")

# numero = 15
# palpite = ''
# while palpite!=numero:
#     int(input("Digite um número: "))
#     if palpite>numero:
#         print("O número é menor que isso")
#     elif palpite<numero:
#         print("O número é maior que isso")
#     else:
#         print("Você acertou")


# numero = int(input("Digite um número: "))
# contador = 1

# while contador != numero:
########################## resolve

