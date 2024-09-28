def calcular(vitorias: int, derrotas: int) -> tuple:
    """
    Calcula o saldo de vitórias e derrotas e determina o nível do herói com base nas vitórias.
    
    :param vitorias: Número de vitórias
    :param derrotas: Número de derrotas
    :return: Tupla contendo o saldo de vitórias e derrotas e o nível do herói
    """
    saldo = vitorias - derrotas  # Calcula o saldo

    # Definição dos níveis
    niveis = [
        (10, "Ferro"),
        (20, "Bronze"),
        (50, "Prata"),
        (80, "Ouro"),
        (90, "Diamante"),
        (100, "Lendário")
    ]

    # Determinação do nível
    nivel = "Imortal"  # Nível padrão para mais de 100 vitórias
    for limite, nome_nivel in niveis:
        if vitorias <= limite:
            nivel = nome_nivel
            break

    return saldo, nivel


def obter_numero(prompt: str) -> int:
    """
    Obtém um número inteiro do usuário, com validação de entrada.
    
    :param prompt: Mensagem a ser exibida ao usuário
    :return: Número inteiro válido fornecido pelo usuário
    """
    while True:
        try:
            valor = int(input(prompt))
            if valor < 0:
                raise ValueError("O número não pode ser negativo.")  # Validação para não permitir números negativos
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, digite um número inteiro válido.")


def main():
    vitorias = obter_numero("Digite a quantidade de vitórias: ")
    derrotas = obter_numero("Digite a quantidade de derrotas: ")

    saldo, nivel = calcular(vitorias, derrotas)
    print(f"O Herói tem um saldo de {saldo} e está no nível de {nivel}.")


if __name__ == "__main__":
    main()  # Chama a função principal
