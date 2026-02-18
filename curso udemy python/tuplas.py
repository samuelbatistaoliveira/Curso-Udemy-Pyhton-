"""""
Tuplas (tuple)

Tuplas são bastantes parecidas com listas.

Existem basicamente duas diferença básicas:

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutaveis: isso significa que ao criar um tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6,)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6,
print(tupla2)

print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # Isso é uma tuplaa!  
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))


# CONCLUSÂO: Podemos concluir que tuplas são definidas pela virtula e não pelo uso do paranteses

(4) -> Não é tupla
(4,) -> E tupla
4, -> E tupla

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla 

tupla = ("Geek University", "Programação em Python: Essencial")

escola,curso = tupla

print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um numero diferente de elementos para desempacotar.

# Metodos para: adição, e remoção de elementos para tuplas não existem, dado o fato das tuplas serem imutaveis.

# SOma*, Valor Máximo*, Valor Mínimo e Tamanho

# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6,)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas 

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutaveis


print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # Tuplas são imutaveis, mais podemos sobreescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na Tupla

tupla = (1, 2, 3)

print(3 in tupla)

# Iterando sobre uma tupla
Tupla = (1, 2, 3)

for n in Tupla:
    print(n) 

for indice, valor in enumerate(Tupla):
    print(indice,valor)

# Contando elementos dentro de uma tupla

tupla = ("a", "b", "c", "d", "a", "b")

print(tupla.count("c"))

escola = tuple("Geek University")
print(escola)

print(escola.count("e")


# O acesso a elementos de uma tupla tambem é semelhante a de uma lista

print(meses[5])

# Iterar com o while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1 

# Verificamos em qual indice um elemento esta na tupla

print(meses.index("Junho",6))

# OBS: Caso o elemento não exista, serã gerdado ValueError.

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Junho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])

# Por que utilizar tuplas?

# - Tuplas são mais rapidas do que listas.
# - Tuplas deixamo seu codigo mais seguro*.

# * Isso porque trablhar com elementos imutaveis traz seguraça para o código.

# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla 

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = tupla # Na tupla nçao temos o produto de Shallow Copy
print(nova)
print(tupla)
"""""

