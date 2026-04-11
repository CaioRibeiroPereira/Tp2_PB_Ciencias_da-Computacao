import exercicio09

LINHAS = 10000
COLUNAS = 10000
BRILHO = 50

print("Executando versão sequencial...")
tempo_seq = exercicio09.ajustar_brilho_sequencial(LINHAS, COLUNAS, BRILHO)
print(f"Tempo sequencial: {tempo_seq:.4f} segundos")

print()

print("Executando versão paralela com OpenMP...")
tempo_par = exercicio09.ajustar_brilho_paralelo(LINHAS, COLUNAS, BRILHO)
print(f"Tempo paralelo: {tempo_par:.4f} segundos")