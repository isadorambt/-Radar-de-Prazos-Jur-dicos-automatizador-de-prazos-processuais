"""
Radar de Prazos Jurídicos - V4
--------------------------------
Interface visual (web local) para consultar e cadastrar prazos,
sem precisar mexer no terminal ou editar o CSV manualmente.

Para rodar:
    streamlit run radar_prazos_v4.py

Autora: Isadora Barreto
"""

import csv
import os
from datetime import date, timedelta

import pandas as pd
import streamlit as st

CAMINHO_CSV = "processos.csv"

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


def situacao_texto(restantes: int) -> str:
    if restantes < 0:
        return f"❌ venceu há {-restantes} dias"
    elif restantes == 0:
        return "🔴 vence HOJE"
    elif restantes <= 3:
        return f"🔴 faltam {restantes} dias"
    elif restantes <= 7:
        return f"🟡 faltam {restantes} dias"
    else:
        return f"🟢 faltam {restantes} dias"


def garantir_csv():
    """Cria o CSV com o cabeçalho se ele ainda não existir."""
    if not os.path.exists(CAMINHO_CSV):
        with open(CAMINHO_CSV, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["processo", "data_inicio", "dias_uteis"])


def carregar_processos() -> pd.DataFrame:
    garantir_csv()
    df = pd.read_csv(CAMINHO_CSV)

    datas_finais = []
    situacoes = []
    restantes_lista = []

    for _, linha in df.iterrows():
        dia, mes, ano = map(int, linha["data_inicio"].split("/"))
        data_inicio = date(ano, mes, dia)
        data_final = calcular_prazo(data_inicio, int(linha["dias_uteis"]))
        restantes = dias_restantes(data_final)

        datas_finais.append(data_final.strftime("%d/%m/%Y"))
        situacoes.append(situacao_texto(restantes))
        restantes_lista.append(restantes)

    df["prazo_final"] = datas_finais
    df["situacao"] = situacoes
    df["_restantes"] = restantes_lista

    df = df.sort_values("_restantes").drop(columns="_restantes")
    return df


def adicionar_processo(numero: str, data_inicio: date, dias_uteis: int):
    with open(CAMINHO_CSV, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([numero, data_inicio.strftime("%d/%m/%Y"), dias_uteis])


# ---------------- Interface ----------------

st.set_page_config(page_title="Radar de Prazos Jurídicos", page_icon="⚖️")
st.title("⚖️ Radar de Prazos Jurídicos")
st.caption("Consulte e cadastre prazos processuais sem sair do navegador.")

st.subheader("📋 Processos cadastrados")
df = carregar_processos()

if df.empty:
    st.info("Nenhum processo cadastrado ainda. Use o formulário abaixo para adicionar o primeiro.")
else:
    st.dataframe(
        df.rename(columns={
            "processo": "Processo",
            "prazo_final": "Prazo final",
            "situacao": "Situação",
        })[["Processo", "Prazo final", "Situação"]],
        use_container_width=True,
        hide_index=True,
    )

st.divider()

st.subheader("➕ Cadastrar novo processo")
with st.form("novo_processo", clear_on_submit=True):
    numero = st.text_input("Número do processo")
    data_inicio = st.date_input("Data de início do prazo")
    dias_uteis = st.number_input("Prazo em dias úteis", min_value=1, step=1)

    enviado = st.form_submit_button("Adicionar")
    if enviado:
        if numero.strip() == "":
            st.error("Preencha o número do processo.")
        else:
            adicionar_processo(numero, data_inicio, int(dias_uteis))
            st.success("Processo adicionado! A lista acima já foi atualizada.")
            st.rerun()
