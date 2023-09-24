class Hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "ataque indefinido"
        
        mensagem = f"O {self.tipo} atacou usando {ataque}"
        return mensagem

# Exemplo de uso
heroi1 = Hero("Gandalf", 200, "mago")
heroi2 = Hero("Aragorn", 35, "guerreiro")
heroi3 = Hero("Bruce Lee", 33, "monge")
heroi4 = Hero("Naruto", 17, "ninja")

print(heroi1.atacar())
print(heroi2.atacar())
print(heroi3.atacar())
print(heroi4.atacar())
