"""
Listas (List)

Listas em Python Funcional coomo vetores/matrizes (arrays) em outras linguagns, com a diferença
de serem DINAMICO e tambem de podermos colocar QUALQUER tipo de dado.

linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo
    - Ou seja, nestas linguagens se voce criar um array do tipo int e com tamanho 5, este array
    sera sempre do tipo inteiro e podera ter sempre no  maximo 5 valores

Ja em Python

- Dinamico: Não possui tamanho fixo: Ou seja, podemos criar a lista e simplemente ir adicionando elementos:
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

Listas são mutaveis: ou seja, elas podem mudar constantemente 

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 44, 27]

lista2 = ["G", "e", "e", "k"," ", "U", "n", "i", "v", "e", "r", "s", "i", "t", "y"]


lista3 = []

lista4 = list(range(11))

lista5 = list("Geek University")

# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f"Encontrei o numero {num}")
else:
    print(f"Não encontrei o numero {num}")

# Podemos facilmente ordenar uma lista
print(lista1.sort())
print(lista1)

# Podemos facilmente contar o número de ocorrencia de um valor em uma lista
print(lista1.count(1))
print(lista5.count("e"))

# Adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

#OBS: Com append, nos so conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56) #Erro

lista1.append([8, 3, 1]) # Coloca cada elemento como unico (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

# Podemos inserir novo elemento na lista informada a posiçao do indice
#OBS: Isso não substitui o valor inicial. O mesmo serã deslocada para a direita da lista.
lista1.insert(2, "Novo valor")
print(lista1)

# Podemos facilmente juntar duas listas

lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista

# Forma 1 
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista1[::-1])

# Copiar uma lista 

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista5))

# Podemos remover facilmente o ultimo elemento de uma lista
#OBS: o pop não somente remove o ultimo elemento mais tambem retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos á direita deste indice seráo deslocados para a esquerda.
# OBS: Se não houver elemento no indice informado,teremos o IndexError.

lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmete repetir elementos em uma lista

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = "Programaçao em Python: Essencial"
curso.split()
print(curso)

#OBS: Por padráo, o split separa os elemento da lista pelo espaço entre elas.

# Exemplo 2
curso = "Programaçao em Python: Essencial"
curso = curso.split(",")
print(curso)

# Convertendo uma lista em uma string

lista6 = ["Programaçao", "em ", "Python", "Essencial"]
print(lista6)

# Abaixo estamos falando: Pega a Lista6, coloca espaço entre cada elemento e transforma em uma string
curso = " ".join(lista6)
print(curso)

# Abaixo estamos falando: Pega a Lista6, coloca cifrão entre cada elemento e transforma em uma string
curso = "$".join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, "Geek", "d", [1,2,3], 45546464]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - utilizando for

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - utilizando while

carrinho = []
produto = ""

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)


for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#           0       1       2         3
cores = ['verde','amarelo','azul','branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pense na lista como um circulo, onde
# o final de um elemento esta ligado ao inicio da lista

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
# print(cores[-5]) # Erro, pois não existe indice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice,cor in enumerate(cores):
    print(indice,cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista está o valor 6?
print(numeros.index(6))
# Em qual indice da lista está o valor 9?
print(numeros.index(9))

# print(numeros.index(19)) # Gera ValueError

# OBS: Caso não tenha este elemento na lista, será apresentando erro ValueError

#OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5,1)) # buscando a partir do indice 1
print(numeros.index(5,2)) # buscando a partir do indice 2
print(numeros.index(5,3)) # buscando a partir do indice 3
# print(numeros.index(5,4)) # buscando a partir do indice 4
# OBS: Caso não tenha este elemento na lista, será apresentando erro ValueError

# Podemos fazer busca dentro de um range,inicio/fim
print(numeros.index(8, 3, 6)) #Buscar o indice do valor 8, entre os indices 3 a 8  

# Revisão de slicing

# lista[inicio:fim passo]
# range(inicio:fim passo)

# Trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parametro 'fim'

print(lista[:2]) #começa em 0, pega ate o indice 2 - 1

print(lista[:4]) #começa em 0, pega ate o indice 4 - 1

print(lista[1:3]) #começa em 0, pega ate o indice 3 - 1

# Trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2]) # Começa em 1, vai ate o final, de 2 em 2

print(lista[::2]) # Começa em 0, vai ate o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

nomes.reverse
print(nomes)

# Soma*,Valor Maximo*,Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # maximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista
    
#Transformar uma lista em tupla

lista =  [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista [1, 2, 3]

num1, num2 ,num3 = lista

print(num1)
print(num2)
print(num3)
#OBS: Se tivermos um número diferente de elementos na lista ou variaveis para receber os dados,teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy() #copia
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizar lista.copy() copiamos os dados da lista para uma nova lista,mas ela
# FIcaram totalmente independentes,ou seja, modificando uma lista,não afeta a outra.Isso em python
# é chamado de Depp Copy (cópia profunda)


# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista #copia

print(nova)

nova.append(4)

print(lista)
print(nova)


# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista,mas
# após realizar modificaçao em uma das listas,essa modificaçáo se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
"""


# Soma*,Valor Maximo*,Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # maximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista