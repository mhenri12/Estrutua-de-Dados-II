# Classe que representa uma fila
class Fila:

    # Método construtor da classe
    def __init__(self):
        # Cria uma lista vazia para armazenar os documentos
        self.fila = []

    # Método para adicionar um documento na fila
    def entrar(self, documento):
        # Adiciona o documento no final da fila
        self.fila.append(documento)

    # Método para imprimir o primeiro documento da fila
    def imprimir(self):
        # Verifica se existe algum documento na fila
        if len(self.fila) > 0:
            # Remove o primeiro documento da fila
            documento = self.fila.pop(0)

            # Mostra qual documento foi impresso
            print("Imprimido:", documento)

        else:
            # Caso não exista nenhum documento
            print("Nada para imprimir")

    # Método para mostrar todos os documentos da fila
    def mostrar(self):
        print(self.fila)


# Cria o spooler da impressora
spooler = Fila()

# Adiciona documentos na fila
spooler.entrar("1")
spooler.entrar("2")
spooler.entrar("3")
spooler.entrar("4")

# Mostra a fila antes das impressões
spooler.mostrar()

# Imprime os dois primeiros documentos
spooler.imprimir()
spooler.imprimir()

# Mostra a fila depois das impressões
spooler.mostrar()
```
