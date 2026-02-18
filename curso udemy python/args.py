"""
Entendendo o *args

- O *args e um parametro, como outro qualquer, Isso significa que voce podera
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convençao, utilizamos *args para definir-lo

Mais o que e o *args?

O parametro * args utilizado em uma função, coloca os valores extras informados como 
entrada em uma tupla. Entao desde ja lembre-se que tuplas sao imutaveis.

# Exemplos

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4,6)) 

print(soma_todos_numeros(4, 6, 9, 5)) # TypeError

# Entendendo o *args 

def soma_todos_numeros(nome, email, *args): 
    return sum(args)


print(soma_todos_numeros("Samuel", "Batista"))
print(soma_todos_numeros("Manoel", "Gonçalves" ,1))
print(soma_todos_numeros("Manoel", "Gonçalves" ,2, 3))
print(soma_todos_numeros("Manoel", "Gonçalves" ,2, 3, 4))
print(soma_todos_numeros("Manoel", "Gonçalves" ,3, 4, 5, 6,)) 

print(soma_todos_numeros("Manoel", "Gonçalves" ,23.4, 12.5))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if "Geek" in args and "University" in args:
        return "Bem-vindo Geek!"
    return "Eu nao tenho certeza quem voce e..."

print(verifica_info())
print(verifica_info(1, True, "University","Geek"))
print(verifica_info(1, "University", 3.145))


"""

def soma_todos_numeros(*args):
    print(args)
    return sum(args)

# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]


# Desempacotador 
print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma ele sabera
# que precisará desempacotar estes dados.