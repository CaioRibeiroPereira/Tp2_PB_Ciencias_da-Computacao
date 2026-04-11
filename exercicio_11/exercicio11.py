import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

random.seed(42)  # semente fixa

N = 20  # número de estações

# ── Geração dos valores aleatórios
a = {
    1: [0] + [random.randint(1, 20) for _ in range(N)],
    2: [0] + [random.randint(1, 20) for _ in range(N)],
}

# t[i][j]: i ∈ {1,2}, j ∈ {1..N-1}  
t = {
    1: [0] + [random.randint(1, 10) for _ in range(N - 1)] + [0],
    2: [0] + [random.randint(1, 10) for _ in range(N - 1)] + [0],
}

# e[i] e x[i]: i ∈ {1,2}
e = {1: random.randint(1, 10), 2: random.randint(1, 10)}
x = {1: random.randint(1, 10), 2: random.randint(1, 10)}


# ── Solução Recursiva (sem memoização) 
def fastest_way_recursive(i: int, j: int) -> int:
    """
    Retorna o menor tempo para chegar até a estação j da linha i.

    Parâmetros
    ----------
    i : int  — linha (1 ou 2)
    j : int  — estação (1 a N)
    """
    other = 2 if i == 1 else 1   # índice da outra linha

    # primeira estação
    if j == 1:
        return e[i] + a[i][1]

    # Permanecer na mesma linha (sem custo de transferência)
    stay     = fastest_way_recursive(i,     j - 1)             + a[i][j]

    # Vir da outra linha (com custo de transferência)
    transfer = fastest_way_recursive(other, j - 1) + t[other][j - 1] + a[i][j]

    return min(stay, transfer)


def solve():
    """Resolve o problema e exibe os resultados."""
    print("=" * 60)
    print("  PROBLEMA DA LINHA DE MONTAGEM — Solução Recursiva")
    print(f"  n = {N} estações por linha")
    print("=" * 60)

    # Tempos acumulados ao chegar à última estação de cada linha
    f1_n = fastest_way_recursive(1, N)
    f2_n = fastest_way_recursive(2, N)

    # Acrescenta o tempo de saída
    total1 = f1_n + x[1]
    total2 = f2_n + x[2]

    # Melhor tempo total
    best_total = min(total1, total2)
    best_exit  = 1 if total1 <= total2 else 2


    print("\n[Tempos de entrada]")
    print(f"  e[1] = {e[1]}   e[2] = {e[2]}")

    print("\n[Tempos de saída]")
    print(f"  x[1] = {x[1]}   x[2] = {x[2]}")

    print("\n[Tempos de montagem  a[i][j]]")
    print("  Linha 1:", a[1][1:])
    print("  Linha 2:", a[2][1:])

    print("\n[Tempos de transferencia  t[i][j]]")
    print("  Linha 1 -> 2:", t[1][1:N])
    print("  Linha 2 -> 1:", t[2][1:N])

    # ── Resultados
    print("\n[Resultados]")
    print(f"  Tempo mínimo saindo pela linha 1: {total1}")
    print(f"  Tempo mínimo saindo pela linha 2: {total2}")
    print(f"\n  >> Tempo minimo total : {best_total}")
    print(f"  >> Saida pela linha   : {best_exit}")
    print("=" * 60)


if __name__ == "__main__":
    solve()
    
""" 
============================================================
  Problema da Linha de Montagem - Solucao Recursiva


  Notação:
   n        : número de estações por linha
   a[i][j]  : tempo de montagem na estação j da linha i  (1-indexed)
   e[i]     : tempo de entrada na linha i
   x[i]     : tempo de saída da linha i
   t[i][j]  : tempo de transferência da linha i para a outra,
               após a estação j

  f(i, j)  = menor tempo para chegar até a estação j da linha i

 ============================================================
"""