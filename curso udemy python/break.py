"""
Saindo de loops com break

Funciona da mesma forma  que nas linguagens C e Java.

Utilizamos o break para sair de loops de maneira projetada.
"""

for numero in range(1,11):
    if numero == 11:
        break
    else:
         print(numero)
print('Sai do loop')

# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break