print("-"*20)
print("BEM VINDO AO SEU SISTEMA DE PONTOS! VAMOS COMEÇAR?")
print("-"*20)
    
def atualizar_pontos(pontos, resultado):
    
    if resultado == 'a':
        pontos += 5
        print("Você acertou! +5 pontos")

    elif resultado == 'e':
        pontos -= 10
        print("Você errou! -10 pontos")

    else:
        print("Opção inválida, digite 'a' para Acerto ou 'e' para Erro.")

    return pontos

def executar_jogo():

    pontos = 100

    while pontos > 0:
        print(f"\nPontos atuais: {pontos}")
        resultado = input("Começamos com 100 pontos! Digite 'a' para Acerto ou 'e' para Erro [A/E]: ").strip().lower()
        pontos = atualizar_pontos(pontos, resultado)

    print(f"\n Fim do Jogo! Pontuação zerada.")

executar_jogo()