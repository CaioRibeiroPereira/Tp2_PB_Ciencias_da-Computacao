import time
import random
import matplotlib.pyplot as plt
import os

# ALGORITMO QUICKSELECT


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    """
    Implementação do algoritmo QuickSelect.
    O algoritmo busca o k-ésimo menor elemento de uma lista desordenada.
    
    :param arr: A lista de entrada
    :param low: Índice inicial de busca
    :param high: Índice final de busca
    :param k: A posição no array ordenado (0-indexado) que queremos encontrar
    :return: O valor do k-ésimo menor elemento
    """
    # Condição base: se o array tiver apenas um elemento, retornamos esse elemento
    if low == high:
        return arr[low]

    # Encontra o pivô
    pi = partition(arr, low, high)

    # Se a posição do pivô for exatamente o k que estamos buscando,significa que encontramos o elemento correto
    if pi == k:
        return arr[pi]
    
    # Se k for menor que o índice do pivô, sabemos que o k-ésimo menor elemento deve estar nos elementos à esquerda do pivô
    elif k < pi:
        return quickselect(arr, low, pi - 1, k)
    
    # Se k for maior, o elemento deve estar nos elementos à direita
    else:
        return quickselect(arr, pi + 1, high, k)

def call_quickselect(arr, k):
    """
    Função auxiliar para chamar o QuickSelect sem precisar passar 'low' e 'high'
    """
    return quickselect(arr, 0, len(arr) - 1, k)


# 2. EXECUÇÃO DOS TESTES E PLOTAGEM

def executar_testes():
    tamanhos = list(range(25, 1001, 25))
    tempos = []

    print("Iniciando testes de desempenho do QuickSelect...")
    print("-" * 65)
    print(f"{'Tamanho da Lista':<20} | {'k Buscado':<15} | {'Tempo de Execução (s)':<20}")
    print("-" * 65)

    for n in tamanhos:
        # Cria a lista com números
        lista_aleatoria = [random.randint(1, 10000) for _ in range(n)]
        
        # Escolhe aleatoriamente qual posição k será buscada 
        k_aleatorio = random.randint(0, n - 1)
        
        # Inicia a contagem de tempo
        inicio = time.perf_counter()
        
        call_quickselect(lista_aleatoria, k_aleatorio)
        
        fim = time.perf_counter()
        tempo = fim - inicio
        
        tempos.append(tempo)
        print(f"{n:<20} | {k_aleatorio:<15} | {tempo:.6f}")


    # 3. PLOTAGEM DO GRÁFICO (Matplotlib)
    plt.figure(figsize=(10, 6))

    # Plota a curva prática obtida experimentalmente
    plt.plot(tamanhos, tempos, marker='o', linestyle='-', color='indigo', label='Tempo Prático (Medido)')

    # Plota a curva teórica (O(n))
    if tempos[-1] > 0:
        c = tempos[-1] / tamanhos[-1]
        curva_teorica = [c * n for n in tamanhos]
        plt.plot(tamanhos, curva_teorica, linestyle='--', color='orange', label='Curva Teórica O(n) Escalonada')

    plt.title('Análise de Complexidade: QuickSelect')
    plt.xlabel('Tamanho da Lista (N)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)



    #salvar
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(pasta_atual, "grafico_quickselect.png")

    plt.savefig(caminho_arquivo)
    print("-" * 65)
    print(f"Gráfico gerado e salvo como '{caminho_arquivo}'.")

if __name__ == "__main__":
    executar_testes()
