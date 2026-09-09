"""
Radar de Prazos Jurídicos - V1
--------------------------------
Calcula a data final de um prazo processual, considerando:
- Dias úteis (pula sábados e domingos)
- Feriados nacionais fixos
- Recesso forense (20/dez a 20/jan)

Autora: Isadora Barreto
"""

from datetime import date, timedelta

# Feriados nacionais fixos (mês, dia).
# Depois dá pra adicionar feriados estaduais/municipais aqui também.
FERIADOS_FIXOS = [
    (1, 1),    # Confraternização Universal
    (4, 21),   # Tiradentes
    (5, 1),    # Dia do Trabalho
    (9, 7),    # Independência
    (10, 12),  # Nossa Senhora Aparecida
    (11, 2),   # Finados
    (11, 15),  # Proclamação da República
    (12, 25),  # Natal
]


def eh_feriado(data: date) -> bool:
    """Verifica se a data é um feriado nacional fixo."""
    return (data.month, data.day) in FERIADOS_FIXOS


def eh_recesso_forense(data: date) -> bool:
    """Verifica se a data está dentro do recesso forense (20/dez a 20/jan)."""
    if data.month == 12 and data.day >= 20:
        return True
    if data.month == 1 and data.day <= 20:
        return True
    return False


def eh_dia_util(data: date) -> bool:
    """Um dia é útil se não for sábado, domingo, feriado ou recesso forense."""
    if data.weekday() >= 5:  # 5 = sábado, 6 = domingo
        return False
    if eh_feriado(data):
        return False
    if eh_recesso_forense(data):
        return False
    return True


def calcular_prazo(data_inicio: date, dias_uteis: int) -> date:
    """
    Calcula a data final de um prazo, contando 'dias_uteis' dias úteis
    a partir de data_inicio (o próprio dia de início não é contado).
    """
    data_atual = data_inicio
    contador = 0
    while contador < dias_uteis:
        data_atual += timedelta(days=1)
        if eh_dia_util(data_atual):
            contador += 1
    return data_atual


def dias_restantes(data_final: date) -> int:
    """Quantos dias (corridos) faltam a partir de hoje até a data final."""
    return (data_final - date.today()).days


if __name__ == "__main__":
    print("=== Radar de Prazos Jurídicos (V1) ===\n")

    inicio_str = input("Data de início do prazo (DD/MM/AAAA): ")
    dia, mes, ano = map(int, inicio_str.split("/"))
    data_inicio = date(ano, mes, dia)

    prazo_dias = int(input("Prazo em dias úteis: "))

    data_final = calcular_prazo(data_inicio, prazo_dias)
    restantes = dias_restantes(data_final)

    print(f"\n📅 Prazo final: {data_final.strftime('%d/%m/%Y')}")
    if restantes > 0:
        print(f"⏳ Faltam {restantes} dias corridos até o vencimento.")
    elif restantes == 0:
        print("🚨 O prazo vence HOJE!")
    else:
        print(f"⚠️ Esse prazo já venceu há {-restantes} dias.")
