def calcular(vitorias, derrotas):
    """
    Calcula o saldo de vitórias e derrotas e determina o nível do herói com base nas vitórias.
    
    :param vitorias: Número de vitórias
    :param derrotas: Número de derrotas
    :return: Tupla contendo o saldo de vitórias e derrotas e o nível do herói
    """
    saldo = vitorias - derrotas  # Calcula o saldo subtraindo derrotas de vitórias

    # Definição dos níveis
    niveis = [
        (10, "Ferro"),      # Até 10 vitórias, nível é "Ferro"
        (20, "Bronze"),     # Até 20 vitórias, nível é "Bronze"
        (50, "Prata"),      # Até 50 vitórias, nível é "Prata"
        (80, "Ouro"),       # Até 80 vitórias, nível é "Ouro"
        (90, "Diamante"),   # Até 90 vitórias, nível é "Diamante"
        (100, "Lendário")   # Até 100 vitórias, nível é "Lendário"
    ]

    # Determinação do nível
    nivel = "Imortal"  # Define nível padrão como "Imortal" para mais de 100 vitórias
    for limite, nome_nivel in niveis:  # Itera sobre os pares (limite, nome_nivel) na lista niveis
        if vitorias <= limite:  # Se o número de vitórias for menor ou igual ao limite atual
            nivel = nome_nivel  # Define o nível como o nome_nivel correspondente
            break  # Sai do loop, pois o nível foi encontrado

    return saldo, nivel  # Retorna o saldo e o nível como uma tupla

# Validação de entrada
def obter_numero(prompt):
    while True:  # Loop infinito até uma entrada válida ser fornecida
        try:
            return int(input(prompt))  # Tenta converter a entrada para inteiro e retornar
        except ValueError:  # Se ocorrer um erro de valor (entrada não é um inteiro)
            print("Por favor, digite um número inteiro válido.")  # Exibe mensagem de erro

vitorias = obter_numero("Digite a quantidade de vitórias: ")  # Obtém o número de vitórias do usuário
derrotas = obter_numero("Digite a quantidade de derrotas: ")  # Obtém o número de derrotas do usuário

saldo, nivel = calcular(vitorias, derrotas)  # Calcula o saldo e o nível chamando a função calcular
print(f"O Herói tem um saldo de {saldo} e está no nível de {nivel}")  # Exibe o saldo e o nível do herói
