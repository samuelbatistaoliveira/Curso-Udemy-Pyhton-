"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos 
por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados:

    
#Criando dicionários

# Forma 1 (Mais comum)

paises = {"br": "BRasil", "eua": "Estados Unidos", "py": "Paraguai"}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br="BRasil", eua="Estados Unidos", py="Paraguai")
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que listas e tuplas
print(paises["br"])
# print(paises["py"])

# OBS: Caso tentemos acessar uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendado
print(paises.get("br"))
print(paises.get("ru"))

# Caso o get não encontre o objeto com a chave informada sera retornado o valor None e não sera gerado keyError

pais = paises.get("ru")

if pais:
    print('Encontrei o pais')
else:
    print('Não encontrei o pais')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get("py","Não encontrado")

print(f'Encontrei o pais {pais}')


# Podemos verificar se determinada chave já existe no dicionáriov

print("br" in paises)  
print("ru" in paises)  
print("Estados Unidos" in paises)

if "ru" in paises:
    russia = paises["ru"]

    # Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive listas, tuplas e dicionários como chaves de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutáveis

localidades = {
    (19.8157, 43.9542): "Belo Horizonte",
    (21.8157, 41.9542): "Rio de Janeiro",
    (23.8157, 45.9542): "São Paulo",
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {"jan": 100, "fev": 120, "mar": 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita["abr"] = 350

print(receita)

# Forma 2 - Menos comum

novo_dado = {"mai": 500}

receita.update(novo_dado) #receita.update({"mai": 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1 - Mais comum

receita["mai"] = 550

print(receita)

# Forma 2 - Menos comum
receita.update({"mai": 600})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas. Se tentarmos adicionar uma nova chave com o mesmo nome, o valor antigo será sobrescrito pelo novo valor. 

# Remover dados de um dicionário

receita = {"jan": 100, "fev": 120, "mar": 300}

print(receita)

# Forma 1 - Mais comum
ret = receita.pop("mar")
print(ret)

print(receita)
#OBS: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, teremos o erro KeyError 
#OBS: Ao remover um objeto, o valor do objeto removido é retornado

# Forma 2 - Menos comum
del receita["fev"]

print(receita)

# Se a chave não existir, teremos o erro KeyError
# OBS: Neste caso o valor removido não é retornado  
"""

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho de compras:
    Produto 1:
        - nome: 
        - quantidade: 
        - preço: 
    Produto 2:
        - nome:
        - quantidade:
        - preço:

# Poderiamos utilizar uma lista para isso? Sim, poderíamos. Mas como faríamos para saber qual é o nome, a quantidade e o preço de cada produto? Sim

carrinho= []

produto1 = ["Playstation 4", 1, 2300.00]
produto2 = ["God of War 4", 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teria que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma tupla para isso? Sim
produto1 = ("Playstation 4", 1, 2300.00)
produto2 = ("God of War 4", 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

# Terioamos que saber qual é o índice de cada informação no produto.

# 3 - Poderíamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {"nome": "Playstation 4", "quantidade": 1, "preço": 2300.00}
produto2 = {"nome": "God of War 4", "quantidade": 1, "preço": 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Dessa forma, facilmente adicionamos ou removemos produtos no carrinho, e para cada produto  sabemos exatamente 
# podemos ter quantos produtos quisermos no carrinho.

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)
d.clear()

print(d)

 Copiando um dicionário para outro

# Forma 1 - Deep Copy
novo = d.copy() 

print(novo)

novo["d"] = 4

print(d)
print(novo)

# Forma 2 - Shallow Copy

novo = d

print(novo)

novo["d"] = 4

print(d)
print(novo)
"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys("a", "b")

print(outro)
print(type(outro))

usuario = {}.fromkeys(["nome", "pontos", "email", "profile"], "desconhecido")
print(usuario)
print(type(usuario))

# O metodo fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave no dicionário e irá atribuir a essa chave o valor informado

veja = {}.fromkeys("teste", "valor")
print(veja)

veja = {}.fromkeys(range(1, 11), "novo")

print(veja)