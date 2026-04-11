import time
import random
import matplotlib.pyplot as plt
import os
import math

# 1 ALGORITMO QUICKSORT


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # Ordena recursivamente os elementos antes da partição
        quicksort(arr, low, pi - 1)
        # Ordena recursivamente os elementos após a partição
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1       

    for j in range(low, high):
        # Se o elemento atual for menor ou igual ao pivô, move-o para a "esquerda"
        if arr[j] <= pivot:
            i += 1
            # Realiza a troca 
            arr[i], arr[j] = arr[j], arr[i]

    # Por fim, posiciona o pivô logo após os elementos menores que ele
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Retorna o índice onde o pivô foi alocado
    return i + 1

def call_quicksort(arr):
    """
    Função WRAPPER para simplificar a chamada do QuickSort passando apenas o array.
    """
    quicksort(arr, 0, len(arr) - 1)



# 2. EXECUÇÃO DOS TESTES E PLOTAGEM

def executar_testes():
    # Tamanhos: 25, 50, 75, ..., 1000
    tamanhos = list(range(25, 1001, 25))
    tempos = []

    print("Iniciando testes de desempenho do QuickSort...")
    print("-" * 50)
    print(f"{'Tamanho da Lista':<20} | {'Tempo de Execução (s)':<20}")
    print("-" * 50)

    for n in tamanhos:
        # Gera uma lista contendo 'n' inteiros aleatórios entre 1 e 10000
        lista_aleatoria = [random.randint(1, 10000) for _ in range(n)]
        
        # Marca o tempo inicial de alta precisão
        inicio = time.perf_counter()
        
        # Executa a ordenação
        call_quicksort(lista_aleatoria)
        
        # Marca o tempo final e calcula a diferença
        fim = time.perf_counter()
        tempo_execucao = fim - inicio
        
        tempos.append(tempo_execucao)
        print(f"{n:<20} | {tempo_execucao:.6f}")


    # 3. PLOTAGEM DO GRÁFICO (Matplotlib)
    plt.figure(figsize=(10, 6))

    # Curva prática baseada nas medidas reais do teste
    plt.plot(tamanhos, tempos, marker='o', linestyle='-', color='b', label='Tempo Prático (Medido)')

    # Curva teórica ajustada (O(n log n))
    # a curva O(n log n) para a ordem de grandeza do tempo real observado no último tamanho.
    if tempos[-1] > 0:
        ultimo_n = tamanhos[-1]
        c = tempos[-1] / (ultimo_n * math.log(ultimo_n))
        curva_teorica = [c * n * math.log(n) for n in tamanhos]
        plt.plot(tamanhos, curva_teorica, linestyle='--', color='r', label='Curva Teórica O(n log n) Escalonada')

    plt.title('Análise de Complexidade: QuickSort (Listas Aleatórias)')
    plt.xlabel('Tamanho da Lista (N)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)

    
    
    #Salvar
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(pasta_atual, "grafico_quicksort.png")

    plt.savefig(caminho_arquivo)

if __name__ == "__main__":
    executar_testes()
