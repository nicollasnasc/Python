# Recebendo o nome do usuário
nome = input("Digite o nome: ")

# Recebendo as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verificando a situação do aluno
if media >= 7:
    print("Aprovado!")
elif media >= 5 and media < 7:
    print("Em recuperação!")
else:
    print("Reprovado!")
