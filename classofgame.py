class Hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataques = {
            "mago": "usou magia",
            "guerreiro": "usou espada",
            "monge": "usou artes marciais",
            "ninja": "usou shuriken"
        }
        
        ataque = ataques.get(self.tipo, "ataque indefinido")
        mensagem = f"O {self.tipo} {self.nome} atacou usando {ataque}"
        return mensagem

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, {self.tipo}"

# Exemplo de uso
heroi1 = Hero("Gandalf", 200, "mago")
heroi2 = Hero("Aragorn", 35, "guerreiro")
heroi3 = Hero("Bruce Lee", 33, "monge")
heroi4 = Hero("Naruto", 17, "ninja")

print(heroi1.atacar())
print(heroi2.atacar())
print(heroi3.atacar())
print(heroi4.atacar())
