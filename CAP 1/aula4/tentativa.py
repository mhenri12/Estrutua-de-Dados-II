# Classe que representa uma pilha
class Pilha:

    # Método construtor da classe
    def __init__(self):
        # Cria uma lista vazia para armazenar as ações
        self.pilha = []

    # Método para adicionar uma ação na pilha
    def empilhar(self, acao):
        self.pilha.append(acao)

    # Método para desfazer a última ação adicionada
    def desfazer(self):
        # Verifica se a pilha não está vazia
        if len(self.pilha) > 0:
            # Remove e retorna o último elemento da pilha
            return self.pilha.pop()
        else:
            # Caso não exista nenhuma ação para desfazer
            return "Nada para desfazer"

    # Método para mostrar os elementos da pilha
    def mostrar(self):
        print(self.pilha)


# Cria um objeto da classe Pilha
pilha = Pilha()

# Adiciona ações na pilha
pilha.empilhar("1")
pilha.empilhar("2")
pilha.empilhar("3")

# Mostra a pilha antes de desfazer
pilha.mostrar()

# Desfaz a última ação adicionada
print("Desfeito:", pilha.desfazer())

# Mostra a pilha depois de desfazer
pilha.mostrar()
```
