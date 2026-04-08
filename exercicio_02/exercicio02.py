import asyncio
import random
import time

async def baixar_arquivo(nome_arquivo):
    try:
        print(f"Iniciando download de {nome_arquivo}...")

        if nome_arquivo == "virus.exe":
            raise Exception("Arquivo bloqueado por segurança.")

        tempo_download = random.randint(1, 5)
        await asyncio.sleep(tempo_download)

        print(f"Download concluído: {nome_arquivo} ({tempo_download}s)")
        return nome_arquivo

    except Exception as e:
        print(f"Erro ao baixar {nome_arquivo}: {e}")
        return None


async def main():
    inicio = time.time()

    arquivos = [
        "foto.jpg",
        "musica.mp3",
        "documento.pdf",
        "video.mp4",
        "virus.exe",
        "planilha.xlsx"
    ]

    tarefas = [baixar_arquivo(arquivo) for arquivo in arquivos]

    resultados = await asyncio.gather(*tarefas)

    arquivos_baixados = [arquivo for arquivo in resultados if arquivo is not None]

    fim = time.time()

    print("\nArquivos baixados com sucesso:")
    for arquivo in arquivos_baixados:
        print(f"- {arquivo}")

    print(f"\nTempo total de execução: {fim - inicio:.2f} segundos")


asyncio.run(main())