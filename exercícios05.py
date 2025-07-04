"""
Exercício:
 01 - Utilize os conceitos de Docstrings para documentar a calculadora padrão do windows
 criada no Exercício #4
 
 """

def somar(a, b):
    """
    Calcula a soma de dois números.

    Args:
        a (float): Primeiro número.
        b (float): Segundo número.

    Returns:
        float: Resultado da soma entre a e b.
    """
    return a + b

def subtrair(a, b):
    """
    Calcula a subtração de dois números.

    Args:
        a (float): Minuendo.
        b (float): Subtraendo.

    Returns:
        float: Resultado da subtração entre a e b.
    """
    return a - b

def multiplicar(a, b):
    """
    Calcula a multiplicação de dois números.

    Args:
        a (float): Primeiro fator.
        b (float): Segundo fator.

    Returns:
        float: Resultado da multiplicação entre a e b.
    """
    return a * b

def dividir(a, b):
    """
    Calcula a divisão de dois números.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float: Resultado da divisão entre a e b.

    Raises:
        ValueError: Se b for 0, retorna erro para evitar divisão por zero.
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b
