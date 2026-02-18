"""
Ranges
-precisamos conhecer o lopo for para usar os range.
- precisamos conhecer o range par trabalhar melhor com loops for.

range são utilizados para gerar sequências numéricas, que são frequentemente usadas em loops for para iterar sobre uma série de números.

range(valor_de_parada)
OBS: valor_de_parada não inclusive (inicio padrão 0, passo padrão 0, e passo de 1 em 1)

# Forma 1 

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, passo padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, passo padrão 0, e passo de 1 em 1)

# Exemplo Forma 2
for num in range(1,11):
    print(num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 3
for num in range(5,55,5):
    print(num)

# Forma 4 (Inversa)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (valor_de_inicio especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 4 (Inversa)
for num in range (10,0,-1):
    print(num)
"""