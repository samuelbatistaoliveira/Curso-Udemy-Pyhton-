"""
Defininido  Funçao

- Funções são pequenas partes de codigo que realizam tarefas específicas;
- Pode ou não receber entradas de dados e pode ou não retornar uma saida de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza varias tarefas dentro dela;
e bom fazer uma verificação para que a função seja simplificada.

ja utilizamos varias funçoes desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras


"""

# Exemplo de utilização de funções

# cores = ["verde", "amarelo", "azul", "branco"]

#Utilizando a função integrada (Built-in) do Python print()

# print(cores)

# curso = "Programação em Python: Essencial"

# print(curso)

# cores.append("roxo") 

# print(cores)

# curso.append("Mais dados...") #AttributeError
# print(curso)

# cores.clear()
# print(cores)

# 
# print(help(print))

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu codigo.

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

    
Onde:
nome_da_funcao -> SEMPRE com letras minusculas, e se for nome composto, separado por underline (Snake Case);
parametros de entrada -> Opcionais, onde tendo mais de um, serao separados por virgula;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, onde é escrito o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que 
estamos definindo uma função. Também abrimos o bloco de código com ja conhecido dois pontos : e que e
utilizado em Python para definir blocos.


"""

# Definindo a primeira função

# Definição
def diz_oi():
    print("Oi!")
      
"""
OBS: 

1 - Veja que dentro das funções, podemos utilizar outras funções;
2 - Veja que nossa função so executa 1 tarefa, ou seja, a unica coisa que ela faz e dizer oi;
3 - Veja que esta função não recebe nenhum parametro de entrada;
4 - Veja que esta função não retorna nada;

"""

# Utilizando a função

# Chamanda de execução)
# diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado
diz_oi()

# Certo
diz_oi()

# Errado
diz_oi
"""

# Exemplo 2
def cantar_parabens():
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print("Viva o aniversariante!")


# for n in range(5):
#   cantar_parabens()

# Em Python, podemos inclusive criar variaveis do tipo de uma função e executar esta função através da variavel

canta = cantar_parabens

canta()