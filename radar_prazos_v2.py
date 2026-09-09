"""
Radar de Prazos Jurídicos - V2
--------------------------------
Lê uma planilha (CSV) com vários processos de uma vez e mostra
os prazos calculados, ordenados por urgência (mais urgente primeiro).

O arquivo CSV precisa ter as colunas:
    processo, data_inicio, dias_uteis

Exemplo (processos.csv):
    processo,data_inicio,dias_uteis
    0001234-56.2025.8.25.0001,01/09/2026,5

Autora: Isadora Barreto
"""

import csv
from datetime import date, timedelta

# Mesmos feriados e regras da V1
FERIADOS_FIXOS = [
    (1, 1), (4, 21), (5, 1), (9, 7),
    (10, 12), (11, 2), (11, 15), (12, 25),
]


def eh_feriado(data: date) -> bool:
    return (data.month, data.day) in FERIADOS_FIXOS


def eh_recesso_forense(data: date) -> bool:
    if data.month == 12 and data.day >= 20:
        return True
    if data.month == 1 and data.day <= 20:
        return True
    return False


def eh_dia_util(data: date) -> bool:
    if data.weekday() >= 5:
        return False
    if eh_feriado(data):
        return False
    if eh_recesso_forense(data):
        return False
    return True


def calcular_prazo(data_inicio: date, dias_uteis: int) -> date:
    data_atual = data_inicio
    contador = 0
    while contador < dias_uteis:
        data_atual += timedelta(days=1)
        if eh_dia_util(data_atual):
            contador += 1
    return data_atual


def dias_restantes(data_final: date) -> int:
    return (data_final - date.today()).days


def emoji_urgencia(restantes: int) -> str:
    """Escolhe um emoji de acordo com a urgência do prazo."""
    if restantes < 0:
        return "❌"  # já venceu
    elif restantes <= 3:
        return "🔴"  # muito urgente
    elif restantes <= 7:
        return "🟡"  # atenção
    else:
        return "🟢"  # tranquilo


def ler_processos(caminho_csv: str) -> list[dict]:
    """Lê o CSV e devolve uma lista de dicionários com os dados de cada processo."""
    processos = []
    with open(caminho_csv, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dia, mes, ano = map(int, linha["data_inicio"].split("/"))
            data_inicio = date(ano, mes, dia)
            dias_uteis = int(linha["dias_uteis"])

            data_final = calcular_prazo(data_inicio, dias_uteis)
            restantes = dias_restantes(data_final)

            processos.append({
                "processo": linha["processo"],
                "data_final": data_final,
                "restantes": restantes,
            })
    return processos


def main():
    caminho = "processos.csv"
    processos = ler_processos(caminho)

    # Ordena do prazo mais urgente (menor número de dias restantes) para o menos urgente
    processos.sort(key=lambda p: p["restantes"])

    print("=== Radar de Prazos Jurídicos (V2) ===\n")
    for p in processos:
        emoji = emoji_urgencia(p["restantes"])
        data_str = p["data_final"].strftime("%d/%m/%Y")

        if p["restantes"] < 0:
            situacao = f"venceu há {-p['restantes']} dias"
        elif p["restantes"] == 0:
            situacao = "vence HOJE"
        else:
            situacao = f"faltam {p['restantes']} dias"

        print(f"{emoji} {p['processo']} | prazo final: {data_str} | {situacao}")


if __name__ == "__main__":
    main()
