import time
import exercicio01

num_passos = 100_000_000

inicio = time.time()
pi = exercicio01.calcular_pi(num_passos)
fim = time.time()

print(f"Valor aproximado de pi: {pi}")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")