def obter_nivel(xpHero):
    """
    Determina o nível do herói com base na experiência (xpHero).

    :param xpHero: Experiência do herói
    :return: Nível do herói como uma string
    """
    # Verifica se a experiência é menor que 1000
    if xpHero < 1000:
        return "Ferro"
    # Verifica se a experiência é menor que 2000
    elif xpHero < 2000:
        return "Bronze"
    # Verifica se a experiência é menor que 5000
    elif xpHero < 5000:
        return "Prata"
    # Verifica se a experiência é menor que 7000
    elif xpHero < 7000:
        return "Ouro"
    # Verifica se a experiência é menor que 8000
    elif xpHero < 8000:
        return "Platina"
    # Verifica se a experiência é menor que 9000
    elif xpHero < 9000:
        return "Ascendente"
    # Verifica se a experiência é menor que 10000
    elif xpHero < 10000:
        return "Imortal"
    # Se a experiência for 10000 ou mais
    else:
        return "Diamante"

# Loop principal para entrada contínua de dados
while True:
    # Solicita o nome do herói
    nameHero = input("Digite o nome do seu herói: ")

    # Validação de entrada para xpHero
    while True:
        try:
            # Solicita a experiência do herói e tenta convertê-la para float
            xpHero = float(input("Qual o xp do seu herói: "))
            break  # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            # Informa o usuário se a entrada não for um número válido
            print("Por favor, digite um número válido para a experiência.")

    # Obtém o nível do herói com base na experiência
    nivel = obter_nivel(xpHero)
    # Exibe o nome e o nível do herói
    print(f"O Herói de nome {nameHero} está no nível {nivel}")

    # Pergunta se o usuário quer classificar outro herói
    outroHeroi = input("Quer saber a classificação de outro Herói? [S/N] ").strip().upper()
    # Se o usuário não quiser classificar outro herói, sai do loop
    if outroHeroi == "N":
        print("Até a próxima!")
        break
