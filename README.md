# ⚖️ Radar de Prazos Jurídicos

Um script em Python que calcula automaticamente a data final de um prazo processual, considerando dias úteis, feriados nacionais e o recesso forense.

## 💡 Por que criei esse projeto

Como advogada, sei o quanto perder um prazo processual pode ser grave. Criei esse projeto como meu primeiro passo em programação, unindo minha área de atuação (Direito) com automação — para transformar um problema real do dia a dia jurídico em uma solução simples e prática.

## ⚙️ O que o script faz

- Calcula a data final de um prazo a partir de uma data de início e um número de dias úteis.
- Pula automaticamente sábados, domingos e feriados nacionais fixos.
- Considera o recesso forense (20/dezembro a 20/janeiro).
- Mostra quantos dias faltam até o vencimento do prazo.

## 🚀 Como rodar

### Pré-requisitos
- Ter o [Python](https://www.python.org/downloads/) instalado (versão 3.8 ou superior).

### Passo a passo

1. Clone este repositório ou baixe o arquivo `radar_prazos_v1.py`.
2. Abra o terminal (ou Prompt de Comando) na pasta onde o arquivo está salvo.
3. Rode o comando:

```bash
python radar_prazos_v1.py
```

No Mac ou Linux, pode ser necessário usar `python3` no lugar de `python`:

```bash
python3 radar_prazos_v1.py
```

4. O programa vai perguntar a data de início do prazo e o número de dias úteis. Exemplo:

```
=== Radar de Prazos Jurídicos (V1) ===

Data de início do prazo (DD/MM/AAAA): 01/09/2026
Prazo em dias úteis: 15

📅 Prazo final: 23/09/2026
⏳ Faltam 14 dias corridos até o vencimento.
```

## 🗺️ Próximos passos (roadmap)

- [ ] **V2:** ler vários processos de uma planilha de uma vez.
- [ ] **V3:** enviar alertas automáticos por e-mail ou Telegram quando um prazo estiver próximo do vencimento.
- [ ] **V4:** interface visual simples (com Streamlit) para consultar os prazos sem precisar mexer no código.

## 🛠️ Tecnologias

- Python 3
- Módulo `datetime` (nativo do Python)

## 👩‍💻 Autora

Isadora Barreto — advogada em transição para o mundo da tecnologia, aprendendo a programar para automatizar tarefas do dia a dia jurídico.
