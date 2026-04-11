def regua_recursiva(n):
    """
    Desenha uma régua de ordem n recursivamente.
    O traço no ponto médio tem comprimento n, os subintervalos têm comprimento n-1 e assim por diante.
    """
    if n > 0:
        # Desenha a parte superior (subintervalo superior)
        regua_recursiva(n - 1)
        
        # Desenha o traço do ponto médio
        print('-' * n)
        
        # Desenha a parte inferior (subintervalo inferior)
        regua_recursiva(n - 1)

if __name__ == "__main__":
    # Testando com a régua de ordem 4 conforme o exemplo
    print("Régua de ordem 4:")
    regua_recursiva(4)
