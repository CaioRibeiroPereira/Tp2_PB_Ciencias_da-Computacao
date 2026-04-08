from cython.parallel import prange
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def calcular_pi(long long num_passos):
    cdef:
        long long i
        double step = 1.0 / num_passos
        double soma = 0.0
        double x
        double pi

    for i in prange(num_passos, nogil=True, schedule='static'):
        x = (i + 0.5) * step
        soma += 4.0 / (1.0 + x * x)

    pi = step * soma
    return pi