# Acumula a soma dos valores informados pelo usuário
total = 0

# Loop principal: lê os números e soma todos até o usuário informar 0
while True:
    num = int(input("Digite um número (0 para encerrar): "))

    if num == 0:
        break

    total += num

print(f"Total da soma: {total}")