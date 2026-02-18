"""
Documentando funções com docstrings em Python.

# OBS: Podemos ter acesso a documentação de uma função em Phyton
Utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()
"""
def diz_oi():
    """Uma função simples que retorna a string "Oi!"""
    return "Oi!"


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' informada.    
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gerar o exponencial. Por padrao e 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia

