import asyncio
import random
import time


# PRODUTOR (sensor)
async def produtor(fila):
    while True:
        batimento = random.randint(40, 180)

        await fila.put(batimento)
        print(f"[Sensor] Gerado: {batimento}")

        await asyncio.sleep(0.5)


# CONSUMIDOR (monitor)
async def consumidor(fila):
    while True:
        batimento = await fila.get()

        if batimento > 120:
            print(f"ALERTA !: Batimento em {batimento}!")
        else:
            print(f"Normal: {batimento}")

        fila.task_done()


# FUNÇÃO PRINCIPAL
async def main():
    fila = asyncio.Queue(maxsize=10)

    # Criando tarefas
    tarefa_produtor = asyncio.create_task(produtor(fila))
    tarefa_consumidor = asyncio.create_task(consumidor(fila))

    # Rodar por 10 segundos
    await asyncio.sleep(10)

    print("\nEncerrando sistema...")

    # Cancelar tarefas
    tarefa_produtor.cancel()
    tarefa_consumidor.cancel()

    try:
        await tarefa_produtor
    except asyncio.CancelledError:
        print("Produtor encerrado.")

    try:
        await tarefa_consumidor
    except asyncio.CancelledError:
        print("Consumidor encerrado.")


# EXECUÇÃO
asyncio.run(main())