import statistics

# Nome do arquivo de log
ARQUIVO_LOG = "log_treinamento.txt"


def ler_tempos_execucao(caminho_arquivo):
    """Lê tempos de execução de um arquivo de log e retorna uma lista de valores numéricos."""
    tempos = []
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                # Exemplo esperado: "Epoch 1 - Tempo: 12.34s"
                if "Tempo:" in linha:
                    try:
                        # Extrai o valor numérico antes do 's'
                        parte_tempo = linha.split("Tempo:")[1].strip().replace("s", "")
                        tempo = float(parte_tempo)
                        tempos.append(tempo)
                    except ValueError:
                        continue
        return tempos
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
        return []


def calcular_estatisticas(tempos):
    """Calcula e exibe a média e o desvio padrão dos tempos."""
    if not tempos:
        print("Nenhum tempo válido encontrado.")
        return

    media = statistics.mean(tempos)
    desvio_padrao = statistics.pstdev(tempos)  # pstdev = desvio padrão populacional

    print("=== Estatísticas de Treinamento ===")
    print(f"Total de execuções: {len(tempos)}")
    print(f"Média dos tempos: {media:.2f} s")
    print(f"Desvio padrão: {desvio_padrao:.2f} s")


def main():
    print("Lendo dados de log...")
    tempos = ler_tempos_execucao(ARQUIVO_LOG)
    calcular_estatisticas(tempos)


main()


# Epoch 1 - Tempo: 12.34s
# Epoch 2 - Tempo: 11.98s
# Epoch 3 - Tempo: 13.20s
# Epoch 4 - Tempo: 12.85s
# Epoch 5 - Tempo: 12.50s
