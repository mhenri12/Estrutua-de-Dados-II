# AVL Balance Challenge

## 1. Identificação do projeto

**Disciplina:** Estruturas de Dados 2
**Tema:** Design de Jogos Educativos sobre Árvores Avançadas por meio da Engenharia Reversa e Reuso de Modelos

### 1.1 Integrantes

* Gabriella Rocha Gonçalves Cardoso
* Miguel Henrico de Araujo França
* Juan Carlos Siqueira de Lima
* Arthur Ferreira Silva

## 2. Visão geral

O **AVL Balance Challenge** é uma proposta de upgrade pedagógico baseada no módulo **Binary Search Tree / AVL Tree do VisuAlgo**.

O VisuAlgo permite visualizar operações realizadas em Árvores Binárias de Busca (BST) e Árvores AVL, acompanhando inserções, remoções, buscas, fatores de balanceamento e rotações.

Nossa proposta parte desse modelo de visualização e o transforma em uma experiência de **aprendizagem ativa**.

Em vez de apenas observar o algoritmo identificar um desequilíbrio e realizar automaticamente a rotação necessária, o jogador passa a ser responsável por:

1. acompanhar a inserção dos nós;
2. analisar a estrutura formada;
3. identificar quando existe desequilíbrio;
4. localizar o primeiro nó desbalanceado;
5. analisar seu Fator de Balanceamento;
6. reconhecer o caso de desequilíbrio;
7. escolher e executar a rotação correta.

Assim, o conhecimento de Árvores AVL deixa de ser apenas conteúdo apresentado pela ferramenta e passa a constituir a **mecânica central do jogo**.

## 3. Modelo reutilizado

### 3.1 Ferramenta base

**VisuAlgo: Binary Search Tree / AVL Tree**

Referência oficial:

https://visualgo.net/en/avl

O VisuAlgo foi desenvolvido como uma plataforma interativa para auxiliar o aprendizado de estruturas de dados e algoritmos por meio de visualizações e animações.

### 3.2 Reuso proposto

Este projeto realiza **reuso conceitual e pedagógico do modelo**, e não reutilização do código fonte do VisuAlgo.

A proposta utiliza como referência:

* a representação visual dos nós;
* a organização de uma BST;
* as operações de inserção;
* o cálculo de altura;
* o Fator de Balanceamento;
* as rotações de uma AVL;
* a visualização passo a passo.

Esses elementos são reorganizados em uma mecânica de jogo baseada na tomada de decisões pelo estudante.

### 3.3 Upgrade proposto

O upgrade consiste em transformar o processo de rebalanceamento em um **desafio interativo**.

Quando uma inserção gerar um desequilíbrio, a execução automática será interrompida e o jogador deverá diagnosticar a situação e escolher a operação correta.

No VisuAlgo, o usuário acompanha visualmente a execução do algoritmo.

No AVL Balance Challenge, o usuário passa a participar diretamente da resolução do problema.

O fluxo deixa de ser:

```text
Inserção
    ↓
Detecção automática
    ↓
Rotação automática
    ↓
Usuário observa
```

e passa a ser:

```text
Inserção
    ↓
Desequilíbrio
    ↓
Jogador analisa
    ↓
Jogador escolhe a rotação
    ↓
Sistema verifica
    ↓
Árvore é corrigida
```

## 4. Estrutura de Dados escolhida

### 4.1 Árvore AVL

A estrutura escolhida para o upgrade é a **Árvore AVL**.

Uma Árvore AVL é uma **Árvore Binária de Busca auto balanceada**.

Em uma BST comum, dependendo da ordem de inserção dos elementos, a estrutura pode ficar excessivamente desbalanceada.

Exemplo:

```text
10
  \
   20
     \
      30
        \
         40
```

Apesar de continuar sendo uma BST válida, a árvore passa a se comportar de maneira semelhante a uma lista.

A Árvore AVL busca impedir esse problema mantendo a diferença de altura entre suas subárvores dentro de um limite.

### 4.2 Fator de Balanceamento

Cada nó possui um **Fator de Balanceamento**, representado por `FB`.

A fórmula utilizada é:

```text
FB = altura da subárvore esquerda - altura da subárvore direita
```

Em uma Árvore AVL balanceada, cada nó deve possuir:

```text
FB = -1, 0 ou +1
```

A interpretação é:

| Fator de Balanceamento | Situação                                                 |
| ---------------------- | -------------------------------------------------------- |
| `0`                    | As duas subárvores possuem a mesma altura                |
| `+1`                   | A subárvore esquerda possui uma unidade de altura a mais |
| `-1`                   | A subárvore direita possui uma unidade de altura a mais  |
| `+2`                   | Existe desequilíbrio para a esquerda                     |
| `-2`                   | Existe desequilíbrio para a direita                      |

Quando um nó atinge `+2` ou `-2`, é necessário realizar uma operação de balanceamento.

### 4.3 Casos de desbalanceamento

Existem quatro principais situações de desbalanceamento.

#### 4.3.1 Caso LL

O crescimento ocorreu pela esquerda da esquerda.

```text
      30
     /
   20
  /
10
```

Caminho:

```text
Esquerda → Esquerda
```

Correção:

```text
Rotação à direita
```

Resultado:

```text
    20
   /  \
 10    30
```

#### 4.3.2 Caso RR

O crescimento ocorreu pela direita da direita.

```text
10
  \
   20
     \
      30
```

Caminho:

```text
Direita → Direita
```

Correção:

```text
Rotação à esquerda
```

Resultado:

```text
    20
   /  \
 10    30
```

#### 4.3.3 Caso LR

O crescimento ocorreu pela esquerda e depois pela direita.

```text
      30
     /
   10
     \
      20
```

Caminho:

```text
Esquerda → Direita
```

Correção:

```text
Rotação à esquerda no filho
Rotação à direita no nó desbalanceado
```

Resultado:

```text
    20
   /  \
 10    30
```

#### 4.3.4 Caso RL

O crescimento ocorreu pela direita e depois pela esquerda.

```text
10
  \
   30
  /
20
```

Caminho:

```text
Direita → Esquerda
```

Correção:

```text
Rotação à direita no filho
Rotação à esquerda no nó desbalanceado
```

Resultado:

```text
    20
   /  \
 10    30
```

## 5. Mecânica fundamental de balanceamento

A principal mecânica do **AVL Balance Challenge** será o balanceamento dos nós de uma Árvore AVL.

Durante a partida, a árvore será construída automaticamente a partir de uma sequência predefinida de valores.

Cada valor será inserido seguindo normalmente as regras de uma Árvore Binária de Busca.

Após cada inserção, o jogo verificará o estado da árvore.

Enquanto todos os nós apresentarem Fator de Balanceamento dentro do intervalo permitido:

```text
-1, 0 ou +1
```

a execução continuará normalmente.

Quando uma nova inserção provocar um desequilíbrio e algum nó apresentar:

```text
+2 ou -2
```

a execução será pausada.

Nesse momento, o jogador deverá analisar a árvore e realizar a correção necessária.

### 5.1 Fluxo principal

```text
Novo valor é apresentado
        ↓
Inserção automática na árvore
        ↓
Cálculo do Fator de Balanceamento
        ↓
Árvore continua balanceada?
       /        \
     Sim        Não
      ↓          ↓
Próxima      Execução é pausada
inserção          ↓
             Jogador analisa
                  ↓
          Identifica o caso
                  ↓
          Escolhe a rotação
                  ↓
          Sistema verifica
                  ↓
             Correto?
            /       \
          Sim       Não
           ↓         ↓
      Árvore é     Feedback
      corrigida    de erro
           ↓
     Próxima inserção
```

### 5.2 Responsabilidade do jogador

O jogador não será responsável por construir manualmente toda a árvore.

A inserção será realizada automaticamente pelo sistema.

A responsabilidade do jogador será:

1. observar o resultado da inserção;
2. identificar se algum nó ficou desbalanceado;
3. analisar o Fator de Balanceamento;
4. identificar o caso LL, RR, LR ou RL;
5. selecionar a rotação correta.

Essa escolha permite concentrar a experiência no principal conteúdo que queremos ensinar: **o balanceamento de Árvores AVL**.

## 6. Mapeamento dos conceitos em mecânicas de gameplay

| Conceito teórico de ED II  | Mecânica correspondente no jogo                                |
| -------------------------- | -------------------------------------------------------------- |
| **Nó da Árvore / Chave**   | Cada valor apresentado pelo sistema é inserido como um novo nó |
| **Altura da Árvore**       | Influencia o estado de equilíbrio da estrutura                 |
| **Fator de Balanceamento** | Funciona como indicador do estado de cada nó                   |
| **FB -1, 0 ou +1**         | Indica que o nó está balanceado                                |
| **FB +2 ou -2**            | Indica que o jogador precisa realizar uma correção             |
| **Caso LL**                | Desafio que exige rotação à direita                            |
| **Caso RR**                | Desafio que exige rotação à esquerda                           |
| **Caso LR**                | Desafio que exige rotação dupla esquerda direita               |
| **Caso RL**                | Desafio que exige rotação dupla direita esquerda               |
| **Rotação**                | Principal ação realizada pelo jogador                          |
| **Árvore balanceada**      | Estado necessário para continuar a partida                     |
| **Árvore desbalanceada**   | Estado que interrompe a progressão até ser corrigido           |

## 7. Exemplo de rodada

Considere a sequência:

```text
30 → 20 → 10
```

Primeiro, o sistema insere:

```text
30
```

Depois:

```text
    30
   /
 20
```

Nesse momento, a árvore ainda está balanceada.

Quando o valor `10` é inserido:

```text
      30
     /
   20
  /
10
```

o nó `30` passa a apresentar:

```text
FB = +2
```

A execução é interrompida.

O jogador deverá observar que o caminho que causou o desequilíbrio foi:

```text
30 → esquerda → 20 → esquerda → 10
```

Portanto:

```text
Esquerda → Esquerda
LL
```

O jogo apresenta as opções:

```text
[ Rotação à esquerda ]

[ Rotação à direita ]

[ Rotação esquerda direita ]

[ Rotação direita esquerda ]
```

A resposta correta é:

```text
Rotação à direita
```

Depois da escolha correta:

```text
     20
    /  \
  10    30
```

A árvore volta ao estado balanceado e a partida continua.

## 8. Feedback ao jogador

O jogo fornecerá feedback imediatamente após cada decisão.

### 8.1 Resposta correta

Exemplo:

```text
Rotação correta

Caso LL identificado

Árvore balanceada
```

O jogador avança para a próxima inserção.

### 8.2 Resposta incorreta

Exemplo:

```text
Rotação incorreta

O nó continua desbalanceado

Tente novamente
```

O sistema poderá permitir uma nova tentativa e apresentar uma explicação sobre o erro.

O objetivo é que o erro também faça parte do processo de aprendizagem.

## 9. Core Loop

O ciclo principal do jogo será:

```text
Receber uma nova chave
        ↓
Inserção automática
        ↓
Analisar a árvore
        ↓
Verificar o balanceamento
        ↓
Identificar um possível desequilíbrio
        ↓
Reconhecer LL, RR, LR ou RL
        ↓
Selecionar a rotação
        ↓
Receber feedback
        ↓
Continuar a partida
```

O jogador repetirá esse processo durante toda a fase.

## 10. Condição de vitória

O jogador vence quando consegue concluir todas as inserções previstas para a fase mantendo a árvore dentro das propriedades de uma AVL.

Para isso, deverá:

* identificar corretamente os desequilíbrios;
* reconhecer os casos LL, RR, LR e RL;
* executar as rotações corretas;
* manter a estrutura balanceada.

## 11. Condição de derrota

A condição de derrota estará associada à incapacidade de manter a árvore balanceada.

Caso o jogador acumule erros ou deixe a estrutura permanecer desbalanceada, a partida poderá ser encerrada.

Essa condição representa a degradação da estrutura.

Exemplo:

```text
10
  \
   20
     \
      30
        \
         40
```

Uma BST excessivamente desbalanceada começa a se aproximar do comportamento de uma lista.

Assim, a derrota não será apenas um elemento visual do jogo, mas estará diretamente relacionada a um problema real de Estruturas de Dados.

## 12. Objetivos pedagógicos

Ao final da experiência, espera se que o jogador consiga:

* compreender o objetivo de uma Árvore AVL;
* reconhecer quando uma árvore está desbalanceada;
* interpretar o Fator de Balanceamento;
* identificar o primeiro nó problemático;
* diferenciar os casos LL, RR, LR e RL;
* selecionar a rotação adequada;
* compreender por que o balanceamento é importante;
* relacionar a altura da árvore com a eficiência das operações.

## 13. Diferencial da proposta

O projeto não busca simplesmente adicionar Árvores AVL ao VisuAlgo, pois essa estrutura já está presente na ferramenta.

O diferencial está na nossa forma de interação.

No VisuAlgo, o jogador acompanha visualmente o funcionamento do algoritmo.

No **AVL Balance Challenge**, o aluno precisa tomar a decisão necessária para corrigir a estrutura.

A proposta transforma:

```text
visualizar o balanceamento
```

em:

```text
realizar o balanceamento
```

Dessa forma, o estudante deixa de apenas observar a solução e passa a aplicar os conceitos de Estruturas de Dados 2 para conseguir avançar no jogo.

## 14. Resumo da proposta

O **AVL Balance Challenge** reutiliza o modelo visual de BST e AVL apresentado pelo VisuAlgo e transforma o processo de rebalanceamento em uma mecânica ativa.

A árvore é construída automaticamente por meio de inserções sucessivas.

Quando um desequilíbrio ocorre, o jogo pausa e transfere a responsabilidade para o jogador.

O estudante deve analisar o Fator de Balanceamento, identificar se o caso é LL, RR, LR ou RL e selecionar a rotação correta.

Dessa forma, conceitos teóricos de Árvores AVL passam a fazer parte diretamente da jogabilidade.
