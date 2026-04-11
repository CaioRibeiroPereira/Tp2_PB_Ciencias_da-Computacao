import os

class NoTexto:
    """Nó da lista duplamente encadeada que armazena uma linha de texto."""
    def __init__(self, texto=""):
        self.texto = texto
        self.anterior = None
        self.proximo = None

class TextoDuplamenteEncadeado:
    """
    Estrutura de Lista Duplamente Encadeada para representar texto.
    Resolve o Exercício 5.
    """
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def inserir_apos(self, indice, texto):
        """Insere uma nova linha de texto após a linha de índice fornecido (1-based)."""
        novo_no = NoTexto(texto)
        if self.tamanho == 0:
            self.primeiro = novo_no
            self.ultimo = novo_no
        elif indice <= 0:
            novo_no.proximo = self.primeiro
            self.primeiro.anterior = novo_no
            self.primeiro = novo_no
        elif indice >= self.tamanho:
            novo_no.anterior = self.ultimo
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no
        else:
            atual = self.obter_no(indice)
            novo_no.proximo = atual.proximo
            novo_no.anterior = atual
            if atual.proximo:
                atual.proximo.anterior = novo_no
            atual.proximo = novo_no
        self.tamanho += 1

    def obter_no(self, indice):
        """Retorna o nó da posição específica (1-based)."""
        if indice < 1 or indice > self.tamanho:
            return None
        atual = self.primeiro
        if indice <= self.tamanho // 2:
            # Percorre do início
            for _ in range(1, indice):
                atual = atual.proximo
        else:
            # Percorre do fim
            atual = self.ultimo
            for _ in range(self.tamanho, indice, -1):
                atual = atual.anterior
        return atual

    def excluir_intervalo(self, inicio, fim):
        """Exclui as linhas do intervalo [inicio, fim]."""
        if self.tamanho == 0:
            return
        inicio = max(1, inicio)
        fim = min(self.tamanho, fim)
        if inicio > fim:
            return

        no_inicio = self.obter_no(inicio)
        no_fim = self.obter_no(fim)

        ant = no_inicio.anterior
        prox = no_fim.proximo

        if ant:
            ant.proximo = prox
        else:
            self.primeiro = prox

        if prox:
            prox.anterior = ant
        else:
            self.ultimo = ant

        self.tamanho -= (fim - inicio + 1)

    def listar(self, inicio=1, fim=None):
        """Imprime as linhas no console no intervalo fornecido."""
        if fim is None:
            fim = self.tamanho
        
        inicio = max(1, inicio)
        fim = min(self.tamanho, fim)
        if inicio > fim or self.tamanho == 0:
            return

        atual = self.obter_no(inicio)
        for i in range(inicio, fim + 1):
            if atual:
                print(f"{i:4d} | {atual.texto}")
                atual = atual.proximo
                
    def obter_linhas(self, inicio, fim):
        """Retorna as strings no intervalo fornecido como uma lista de Python."""
        linhas = []
        inicio = max(1, inicio)
        fim = min(self.tamanho, fim)
        if inicio > fim or self.tamanho == 0:
            return linhas

        atual = self.obter_no(inicio)
        for i in range(inicio, fim + 1):
            if atual:
                linhas.append(atual.texto)
                atual = atual.proximo
        return linhas


# =====================================================================
# SOLUÇÃO PARA O EXERCÍCIO 6
# =====================================================================

def exibir_ajuda():
    print("--- Comandos Disponíveis ---")
    print("  I <n>          : Inserção a partir da linha <n> (usa corrente se vazio).")
    print("  E <i>,<f>      : Exclui da linha <i> até <f> (usa corrente se vazio).")
    print("  D <i>,<f>,<p>  : Duplica linhas de <i> até <f> e insere após <p>.")
    print("  L <i>,<f>      : Lista linhas de <i> até <f> (lista tudo se vazio).")
    print("  C <arq>,<n>    : Carrega arquivo txt após <n> (usa corrente se vazio).")
    print("  S <arq>,<i>,<f>: Salva de <i> a <f> no arquivo (salva tudo se não especificar).")
    print("  A <n>          : Altera a linha <n> (usa corrente se vazio).")
    print("  F              : Finaliza execução.")
    print("----------------------------")

def iniciar_editor():
    texto = TextoDuplamenteEncadeado()
    linha_corrente = 0
    
    # Pre-carregando o texto do Exercício 5 como demonstração
    linhas_iniciais = [
        "A natureza,",
        "dizem-nos,",
        "é apenas o hábito...",
        "",
        "(Rousseau)"
    ]
    for i, linha in enumerate(linhas_iniciais):
        texto.inserir_apos(i, linha)
    linha_corrente = texto.tamanho

    print("\nEditor de Texto (Lista Duplamente Encadeada) Iniciado!")
    print("Texto base do Exercício 5 carregado automaticamente.")
    exibir_ajuda()
    
    while True:
        try:
            # Mostra a linha corrente apenas com indicador
            entrada = input(f"\n[{linha_corrente}] > ").strip()
            if not entrada:
                continue
            
            # Separar o comando dos argumentos
            partes = entrada.split(' ', 1)
            cmd = partes[0].upper()
            
            # Formatar argumentos (separa por vírgula em uma string, ex: "1,2")
            args = [a.strip() for a in partes[1].split(',')] if len(partes) > 1 and partes[1].strip() else []
            
            if cmd == 'I':
                n = int(args[0]) if args else linha_corrente
                print("Modo de Inserção. Insira seu texto.")
                print("Digite apenas um ponto final (.) numa linha vazia para encerrar.")
                while True:
                    nova_linha = input()
                    if nova_linha == '.':
                        break
                    texto.inserir_apos(n, nova_linha)
                    n += 1
                    linha_corrente = n

            elif cmd == 'E':
                if len(args) == 2:
                    i, f = int(args[0]), int(args[1])
                elif len(args) == 0:
                    i = f = linha_corrente
                else:
                    print("Uso incorreto. Exemplo: E 2,4 ou E")
                    continue
                texto.excluir_intervalo(i, f)
                linha_corrente = min(i, texto.tamanho) if texto.tamanho > 0 else 0

            elif cmd == 'D':
                if len(args) == 3:
                    i, f, p = map(int, args)
                    linhas_para_duplicar = texto.obter_linhas(i, f)
                    for linha in linhas_para_duplicar:
                        texto.inserir_apos(p, linha)
                        p += 1
                    linha_corrente = p
                else:
                    print("Uso incorreto. Exemplo: D 1,3,5")

            elif cmd == 'L':
                if len(args) == 2:
                    i, f = int(args[0]), int(args[1])
                else:
                    i, f = 1, texto.tamanho
                texto.listar(i, f)
                # Mantém a linha corrente inalterada na listagem ou movimenta para o final da leitura?
                # Opcional mantermos.

            elif cmd == 'C':
                if len(args) >= 1:
                    arq_nome = args[0]
                    
                    # Resolve a pasta atual exata onde este arquivo script está contido
                    pasta_base = os.path.dirname(os.path.abspath(__file__))
                    arq = os.path.join(pasta_base, arq_nome)
                    
                    n = int(args[1]) if len(args) > 1 else linha_corrente
                    try:
                        with open(arq, 'r', encoding='utf-8') as arquivo:
                            linhas_arq = arquivo.readlines()
                            for linha in linhas_arq:
                                texto.inserir_apos(n, linha.rstrip('\n'))
                                n += 1
                        linha_corrente = n
                        print(f"{len(linhas_arq)} linhas carregadas de '{arq_nome}' (Caminho: {arq}).")
                    except FileNotFoundError:
                        print(f"Erro: Arquivo '{arq_nome}' não encontrado no caminho:\n{arq}")
                else:
                    print("Uso incorreto. Exemplo: C dados.txt,2 ou C dados.txt")

            elif cmd == 'S':
                if len(args) >= 1:
                    arq_nome = args[0]
                    
                    # Resolve a pasta atual exata onde este arquivo script está contido
                    pasta_base = os.path.dirname(os.path.abspath(__file__))
                    arq = os.path.join(pasta_base, arq_nome)
                    
                    if len(args) == 3:
                        i, f = int(args[1]), int(args[2])
                    else:
                        i, f = 1, texto.tamanho
                        
                    linhas_salvar = texto.obter_linhas(i, f)
                    try:
                        with open(arq, 'w', encoding='utf-8') as arquivo:
                            for linha in linhas_salvar:
                                arquivo.write(linha + '\n')
                        print(f"Texto ({len(linhas_salvar)} linhas) salvo em '{arq_nome}' (Caminho: {arq}).")
                    except Exception as e:
                        print(f"Erro ao salvar arquivo: {e}")
                else:
                    print("Uso incorreto. Exemplo: S dados.txt,1,5 ou S dados.txt")

            elif cmd == 'A':
                n = int(args[0]) if args else linha_corrente
                no = texto.obter_no(n)
                if no:
                    print(f"Texto antigo [{n}]: {no.texto}")
                    novo_texto = input(f"Novo texto  [{n}]: ")
                    no.texto = novo_texto
                    linha_corrente = n
                else:
                    print("Erro: Linha inexistente.")

            elif cmd == 'F':
                print("Finalizando o editor de textos...")
                break

            elif cmd == 'H' or cmd == 'AJUDA':
                exibir_ajuda()
                
            else:
                print("Comando inválido. Digite 'H' para ver as opções.")
                
        except ValueError:
            print("Erro numérico: Verifique se os argumentos de linhas passados são números inteiros e corretos.")
        except KeyboardInterrupt:
            print("\nFinalizando execução (Crtl+C).")
            break
        except Exception as e:
            print(f"Erro inesperado durante execução do comando: {e}")

if __name__ == "__main__":
    iniciar_editor()
