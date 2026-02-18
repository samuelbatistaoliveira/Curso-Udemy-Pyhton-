"""
Funções com Parâmetros Padrão (Default Parameters)

- Funções onde a passagem de parâmetros seja opcional.

# Exemplo de função onde a passagem de parâmetro seja opcional

# Exemplo de função onde a passagem de parametro seja obrigatoria

def quadrado(numero):
    return numero ** 2

print(quadrado(3)) 
print(quadrado()) # TypeError

def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva á potencia informado pelo usuário

# OBS

# Se o usuário passar somente 1 argumentos, este será atribuído ao parâmetro numero, e sera calculado o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro numero e o segundo ao parâmetro potencia. Então 
# será calculada a potência.

print(exponencial()) 

# OBS: Em funções python, os parâmetros com valores default (padrão) DEVEM estar ao final da declaração.

# ERRO!
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1=5,num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) 
print(soma()) 

# Exemplo mais complexo

def mostra_informacao(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return "Bem-vindo instrutor Geek!"
    elif nome == "Geek":
        return "Eu pensei que você fosse o instrutor"
    return f"Olá {nome}"


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao("Ozzy"))
print(mostra_informacao(nome="Samuel"))

# Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos; 
- Nos permite trabalhar com exemplos mais legíveis de código.

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado: 
    -Números, strings, floats,booleanos, listas, tuplas, dicionários, funções e etc.

# Exemplos

def soma(num1,num2):
    return num1 + num2

def mat(num1,num2,funcao=soma):
    return funcao(num1,num2)

def subtracao(num1,num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,2,subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = "Geek" # Variável global

def diz_oi():
    instrutor = "Python" # Variável local
    return f"Oi {instrutor}"

print(diz_oi())

#OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local terá preferência

def diz_oi():
    prof = "Geek" # Variável local
    return f"Ola {prof}"

print(diz_oi())

print(prof) # NameError

# Atenção com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError (A variável local está sendo utilizada para processamento antes de ser inicializada)
    return total

print(incrementa())

# Atenção com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável global

    total = total + 1 # UnboundLocalError (A variável local está sendo utilizada para processamento antes de ser inicializada)
    return total

print(incrementa())
print(incrementa())
print(incrementa())


"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável.

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())