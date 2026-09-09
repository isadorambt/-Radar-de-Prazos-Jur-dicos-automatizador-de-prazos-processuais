"""
Testes automatizados do Radar de Prazos Jurídicos.

Rodar com: pytest test_radar_prazos.py -v
"""

from datetime import date
from radar_prazos_v1 import eh_dia_util, eh_feriado, eh_recesso_forense, calcular_prazo


def test_dia_de_semana_normal_eh_util():
    # Terça-feira, 08/09/2026, sem feriado
    assert eh_dia_util(date(2026, 9, 8)) is True


def test_sabado_nao_eh_util():
    # Sábado, 05/09/2026
    assert eh_dia_util(date(2026, 9, 5)) is False


def test_domingo_nao_eh_util():
    # Domingo, 06/09/2026
    assert eh_dia_util(date(2026, 9, 6)) is False


def test_feriado_nacional_nao_eh_util():
    # 7 de setembro (Independência) é sempre feriado
    assert eh_feriado(date(2026, 9, 7)) is True
    assert eh_dia_util(date(2026, 9, 7)) is False


def test_dia_normal_nao_eh_feriado():
    assert eh_feriado(date(2026, 9, 8)) is False


def test_recesso_forense_dezembro():
    # 25 de dezembro está dentro do recesso forense
    assert eh_recesso_forense(date(2026, 12, 25)) is True


def test_recesso_forense_janeiro():
    # 10 de janeiro está dentro do recesso forense
    assert eh_recesso_forense(date(2026, 1, 10)) is True


def test_fora_do_recesso_forense():
    # 21 de janeiro já está fora do recesso
    assert eh_recesso_forense(date(2026, 1, 21)) is False


def test_calcular_prazo_exemplo_conhecido():
    # Caso validado manualmente: 01/09/2026 + 15 dias úteis = 23/09/2026
    inicio = date(2026, 9, 1)
    resultado = calcular_prazo(inicio, 15)
    assert resultado == date(2026, 9, 23)


def test_calcular_prazo_pula_fim_de_semana_e_feriado():
    # Sexta-feira (04/09/2026) + 1 dia útil deve pular sábado, domingo
    # E o feriado de 7 de setembro (segunda), indo parar na terça (08/09)
    sexta = date(2026, 9, 4)
    resultado = calcular_prazo(sexta, 1)
    assert resultado == date(2026, 9, 8)
