# cython: boundscheck=False, wraparound=False
from cython.parallel import prange
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def ajustar_brilho_sequencial(int linhas, int colunas, int brilho):
    cdef int i, j
    cdef unsigned char[:, :] matriz

    import numpy as np
    import time

    matriz_np = np.random.randint(0, 256, size=(linhas, colunas), dtype=np.uint8)
    matriz = matriz_np

    inicio = time.perf_counter()

    for i in range(linhas):
        for j in range(colunas):
            if matriz[i, j] + brilho > 255:
                matriz[i, j] = 255
            else:
                matriz[i, j] += brilho

    fim = time.perf_counter()
    return fim - inicio


@cython.boundscheck(False)
@cython.wraparound(False)
def ajustar_brilho_paralelo(int linhas, int colunas, int brilho):
    cdef int i, j
    cdef unsigned char[:, :] matriz

    import numpy as np
    import time

    matriz_np = np.random.randint(0, 256, size=(linhas, colunas), dtype=np.uint8)
    matriz = matriz_np

    inicio = time.perf_counter()

    for i in prange(linhas, nogil=True, schedule='static'):
        for j in range(colunas):
            if matriz[i, j] + brilho > 255:
                matriz[i, j] = 255
            else:
                matriz[i, j] += brilho

    fim = time.perf_counter()
    return fim - inicio