# Calculadora de Ranqueamento de Heróis

Este repositório contém uma série de scripts Python para calcular o ranqueamento de heróis com base em suas vitórias e derrotas, além de classificar os heróis de um jogo fictício.

## Arquivos

1. **calcularRanqueada.py**:
   - Contém uma função chamada `calcular` que calcula o saldo de vitórias e derrotas de um herói e determina seu nível com base no número de vitórias. Também inclui uma função `obter_numero` para validar a entrada do usuário. Um exemplo de uso é fornecido ao final do arquivo.

2. **classificarheroi.py**:
   - Contém uma função chamada `obter_nivel`, que determina o nível do herói com base em sua experiência. Um exemplo de uso não está incluído, pois a função é destinada a ser usada como parte de um script maior.

3. **classofgame.py**:
   - Contém uma classe `Hero` que representa um herói com atributos como nome, idade e tipo. Inclui métodos para atacar e uma representação em string (`__str__`). Um exemplo de uso é fornecido ao final do arquivo.

## Uso

1. **Pré-requisitos**: Certifique-se de ter o Python instalado em seu ambiente. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

2. **Clone o repositório**:
   ```bash
   git clone https://github.com/jefteralex1/classificador-nivel-heroi/
   ```
3. **Execute os scripts**:
- Navegue até o diretório do repositório:
   ````bash
   cd classificador-nivel-heroi
- Execute o script desejado:
   ```bash
   python calcularRanqueada.py
   ```
- ou
   ```bash
   python classificarheroi.py
   ```
- ou
   ```bash
   python classofgame.py
   ```
## Contribuição
Contribuições são bem-vindas! Para contribuir com este projeto, siga os passos abaixo:

- Faça um fork deste repositório.
- Crie uma nova branch (git checkout -b feature/nome-da-feature).
- Faça commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').
- Faça push para a branch (git push origin feature/nome-da-feature).
- Abra um Pull Request.
