print("-"*20)
print("BEM VINDO AO SEU SISTEMA DE PONTOS! VAMOS COMEÇAR?")
print("-"*20)

# Pontuação inicial do jogador
pontos = 100

# Laço onde todo o sistema vai ser constituido, exibindo os pontos atuais, perguntando ao usuário e calculando os pontos.
while pontos > 0:
    print(f"\nPontos atuais: {pontos}")

    resultado = input("Digite 'a' para Acerto ou 'e' para Erro A/E]? ").strip().lower()

    if resultado == "a":
        pontos += 5
        print("Você acertou! +5 pontos")

    elif resultado == "e":
        pontos -= 10
        print("Você errou! -10 pontos")

    else:
        print("Opção inválida, digite 'a' para o acerto ou 'e' para o erro.")

print("\nFim do Jogo! Pontuação zerada.")