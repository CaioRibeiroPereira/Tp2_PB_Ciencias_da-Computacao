def calcular_tamanho_pasta(estrutura):
    """
    Função recursiva para calcular o tamanho total ocupado por uma pasta,
    representada por um dicionário aninhado.
    """
    tamanho_total = 0
    
    for nome, conteudo in estrutura.items():
        # Se o conteúdo for um dicionário, faz a chamada recursiva
        if isinstance(conteudo, dict):
            tamanho_total += calcular_tamanho_pasta(conteudo)
        # Se for um número (tamanho do arquivo), soma ao total
        elif isinstance(conteudo, (int, float)):
            tamanho_total += conteudo
            
    return tamanho_total

if __name__ == "__main__":
    # Exemplo fornecido
    sistema_arquivos = {
      "Documentos": {
        "Trabalho": {"projeto1.pdf": 500, "projeto2.pdf": 300},
        "Pessoal": {"receitas.txt": 10},
      },
      "Imagens": {
        "Ferias": {"foto1.jpg": 2000, "foto2.jpg": 3000},
        "logo.png": 150
      },
      "README.txt": 5
    }

    tamanho = calcular_tamanho_pasta(sistema_arquivos)
    print(f"O tamanho total da estrutura de pastas é: {tamanho}")
