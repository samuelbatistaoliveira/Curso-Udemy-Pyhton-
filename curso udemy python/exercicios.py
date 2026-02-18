"""

Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.


contador: int = 0
indice: int = 1

while contador < 5:
    if indice % 3 == 0:
        print(f"O número {indice} é múltiplo de 3.")
        contador += 1
    indice += 1

 Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando
em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.


contador: int = 10
while contador >= 0:
    print(contador)
    contador -= 1
print("FIM!")



Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).

for numero in range(0, 100001,1000):
    print(numero)


1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos

lista: list[int] = []

while len(lista) < 6:
    valor = int(input(f"Digite um número inteiro: {len(lista) + 1}/6:"))
    lista.append(valor)

for valor in lista:
    print(valor)


2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
deve executar os seguintes passos:
a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre
na tela esta soma.
c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor da lista A, um em cada linha.

1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.

numero = int(input("Digite um numero?"))


def parametro(numero):
    dobro = numero * 2
    return f"O dobro do valor é {dobro}"

print(parametro(numero))

# 2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
#   imprima ela por extenso como “1 de janeiro de 2024

Meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 
    5: "Maio", 6: "Junho", 7: "Julho",
    8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro",12: "Dezembro",
}

def data_extenso(data):
    partes = data.split("/")
    dia = int(partes[0])
    mes_num = int(partes[1])
    anos = partes[2]

    mes_nome = Meses[mes_num]

    print(f"Hoje e {dia} de {mes_nome} de {anos}")

data_extenso("01/01/2025")
"""

# A: list [int] = [1, 0, 5, -2, -5, 7]

#soma = A[0] + A[1] + A[5]
# print(f"A soma dos valores eh {soma}")

# A[5] = 100





# 3. Faça um programa que tenha uma função que receba uma 
# lista de inteiros e retorne o maior valor.


def inteiro():
    if not lista:
        return None
    
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

lista = [1,2,3,45,6]


print(inteiro())




def data_extenso(data):
    d = data.split("/")


    dia: int = int(d[0])
    mes: int = int(d[1])
    anos: int = int(d[2])


    print(f"{dia} de {mes} de {anos}")

data_extenso("01/01/2025")