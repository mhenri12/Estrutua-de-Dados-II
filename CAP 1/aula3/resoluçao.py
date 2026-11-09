#!1 10,20,30,40
#!2 possui o mesmo resultado, listas são objetos mutáveis e variáveis não guardam o valor direto do objeto, mas sim uma referência (ponteiro) para a memória onde o objeto reside.
#!3 cria uma nova lista em um novo local da memoria, os objetos a e b retornariam numeros diferentes pq agora ocupam um novo local na memoria



#desafio
fila = []

def adicionar_paciente():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    prioridade = input("É prioridade? (s/n): ").lower()
    paciente = {
        "nome": nome,
        "idade": idade,
        "prioridade": prioridade == "s"
    }
    if paciente["prioridade"]:
        #colocar o paciente prioritario em primeiro da lista
        posicao = 0

        while posicao < len(fila) and fila[posicao]["prioridade"]:
            posicao += 1
        fila.insert(posicao, paciente)
    else:
        fila.append(paciente)

    print("Paciente adicionado!")

def listar_pacientes():
    if len(fila) == 0:
        print("A fila está vazia.")
        return

    print("\n--- FILA DE PACIENTES ---")
    for i, paciente in enumerate(fila, 1):
        tipo = "Prioridade" if paciente["prioridade"] else "Normal"

        print(
            f"{i}. {paciente['nome']} - "
            f"{paciente['idade']} anos - {tipo}"
        )
def atender_paciente():
    if len(fila) == 0:
        print("Não há pacientes para atender.")
        return

    paciente = fila.pop(0)
  
    print(
        f"Paciente atendido: {paciente['nome']} - "
        f"{paciente['idade']} anos"
    )
def verificar_vazia():
    if len(fila) == 0:
        print("A fila está vazia.")
    else:
        print("A fila NÃO está vazia.")
def quantidade_pacientes():
    print(f"Quantidade de pacientes: {len(fila)}")
  
while True:
    print("\n===== CLÍNICA =====")
    print("1 - Adicionar paciente")
    print("2 - Listar pacientes")
    print("3 - Atender primeiro paciente")
    print("4 - Verificar se a fila está vazia")
    print("5 - Informar quantidade de pacientes")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_paciente()
    elif opcao == "2":
        listar_pacientes()
    elif opcao == "3":
        atender_paciente()
    elif opcao == "4":
        verificar_vazia()
    elif opcao == "5":
        quantidade_pacientes()
    elif opcao == "6":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida!")
