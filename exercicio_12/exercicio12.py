import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

random.seed(42)

LINES = 3  # numero de linhas
N     = 20   # numero de estacoes por linha

# ── Geracao dos valores aleatorios 

# Tempos de montagem: a[linha][estacao]
a = {
    i: [0] + [random.randint(1, 20) for _ in range(N)]
    for i in range(1, LINES + 1)
}

# Tempos de transferencia: t[origem][destino][estacao]
# Apenas para origem != destino; 
t = {}
for src in range(1, LINES + 1):
    t[src] = {}
    for dst in range(1, LINES + 1):
        if src != dst:
            t[src][dst] = [0] + [random.randint(1, 10) for _ in range(N - 1)] + [0]

# Tempos de entrada e saida: e[linha], x[linha]
e = {i: random.randint(1, 10) for i in range(1, LINES + 1)}
x = {i: random.randint(1, 10) for i in range(1, LINES + 1)}


# ── Cache de memoizacao (para viabilizar N=20 com 3 linhas) 
_memo = {}


# ── Solucao Recursiva com Memoizacao
def fastest_way_recursive(i: int, j: int) -> int:
    """
    Retorna o menor tempo para chegar ate a estacao j da linha i.

    A logica implementa exatamente a recorrencia do enunciado.
    O dicionario _memo evita recomputacao de subproblemas identicos,
    tornando a execucao viavel sem alterar a estrutura recursiva.

    Parametros
    ----------
    i : int  -- linha (1, 2 ou 3)
    j : int  -- estacao (1 a N)
    """
    # Verifica cache
    if (i, j) in _memo:
        return _memo[(i, j)]

    # Caso base: primeira estacao
    if j == 1:
        resultado = e[i] + a[i][1]

    else:
        # Opcao 1 permanecer na linha i
        melhor = fastest_way_recursive(i, j - 1) + a[i][j]

        # Opcao 2 vir de qualquer outra linha k
        for k in range(1, LINES + 1):
            if k != i:
                custo = fastest_way_recursive(k, j - 1) + t[k][i][j - 1] + a[i][j]
                if custo < melhor:
                    melhor = custo

        resultado = melhor

    _memo[(i, j)] = resultado
    return resultado


# ── Resolucao e impressao dos resultados
def solve():
    print("=" * 65)
    print("  PROBLEMA DA LINHA DE MONTAGEM COM 3 LINHAS")
    print("  Solucao Recursiva com Memoizacao")
    print(f"  Linhas = {LINES}   Estacoes por linha = {N}")
    print("=" * 65)

    print("\n[Tempos de entrada  e[i]]")
    for i in range(1, LINES + 1):
        print(f"  e[{i}] = {e[i]}")

    print("\n[Tempos de saida  x[i]]")
    for i in range(1, LINES + 1):
        print(f"  x[{i}] = {x[i]}")

    print("\n[Tempos de montagem  a[i][j]]")
    for i in range(1, LINES + 1):
        print(f"  Linha {i}: {a[i][1:]}")

    print("\n[Tempos de transferencia  t[origem->destino][j]]")
    for src in range(1, LINES + 1):
        for dst in range(1, LINES + 1):
            if src != dst:
                print(f"  Linha {src} -> Linha {dst}: {t[src][dst][1:N]}")

    # Calcula o tempo minimo para chegar ao fim de cada linha
    totais = {}
    for i in range(1, LINES + 1):
        totais[i] = fastest_way_recursive(i, N) + x[i]

    print("\n[Resultados]")
    for i in range(1, LINES + 1):
        print(f"  Tempo minimo saindo pela linha {i}: {totais[i]}")

    melhor_linha = min(totais, key=totais.get)
    melhor_tempo = totais[melhor_linha]

    print(f"\n  >> Tempo minimo total : {melhor_tempo}")
    print(f"  >> Saida pela linha   : {melhor_linha}")
    print(f"\n  [Subproblemas calculados: {len(_memo)} de {LINES * N} possiveis]")
    print("=" * 65)


if __name__ == "__main__":
    solve()

"""
============================================================
  Problema da Linha de Montagem com 3 Linhas - Solucao Recursiva


  Extensao do problema classico (exercicio 11) para 3 linhas.

  Notacao:
   LINES     : numero de linhas (3)
   N         : numero de estacoes por linha (20)
   a[i][j]   : tempo de montagem na estacao j da linha i
   e[i]      : tempo de entrada na linha i
   x[i]      : tempo de saida apos a n-esima estacao da linha i
   t[k][i][j]: tempo de transferencia da linha k para a linha i
               apos a estacao j (so para k != i)

"""