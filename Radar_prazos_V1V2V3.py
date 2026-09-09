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

## 📊 V2 — vários processos de uma vez

A partir da V2, é possível ler vários processos de uma planilha (`processos.csv`) e ver todos ordenados por urgência.

### Formato da planilha

O arquivo `processos.csv` precisa ter as colunas `processo`, `data_inicio` e `dias_uteis`:

```
processo,data_inicio,dias_uteis
0001234-56.2025.8.25.0001,01/09/2026,5
0007891-23.2025.8.25.0002,03/09/2026,15
```

### Como rodar

1. Coloque `radar_prazos_v2.py` e `processos.csv` na mesma pasta.
2. Edite o `processos.csv` com seus processos reais.
3. Rode:

```bash
python3 radar_prazos_v2.py
```

O resultado aparece ordenado do prazo mais urgente para o menos urgente, com emojis indicando o nível de atenção (🔴 muito urgente, 🟡 atenção, 🟢 tranquilo, ❌ já venceu).

## 📧 V3 — alertas automáticos por e-mail

A partir da V3, o script verifica os processos e envia um e-mail automático de alerta para os que estão com prazo próximo do vencimento (padrão: 3 dias ou menos).

### Configuração de e-mail (uma vez só)

Por segurança, as credenciais de e-mail **não** ficam no código — elas são lidas de variáveis de ambiente.

1. Ative a verificação em duas etapas na sua conta Google, em [myaccount.google.com/security](https://myaccount.google.com/security).
2. Gere uma senha de app em [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
3. Antes de rodar o script, defina as variáveis no terminal:

**Mac/Linux:**
```bash
export EMAIL_REMETENTE="seuemail@gmail.com"
export EMAIL_SENHA_APP="a senha de 16 letras gerada pelo Google"
```

**Windows (cmd):**
```cmd
set EMAIL_REMETENTE=seuemail@gmail.com
set EMAIL_SENHA_APP=a senha de 16 letras gerada pelo Google
```

> ⚠️ Nunca coloque sua senha normal do Gmail ou a senha de app diretamente no código — use sempre variáveis de ambiente, como mostrado acima.

### Como rodar

1. Coloque `radar_prazos_v3.py` e `processos.csv` na mesma pasta.
2. Configure as variáveis de ambiente (passo acima).
3. Rode, no mesmo terminal:

```bash
python3 radar_prazos_v3.py
```

Se algum processo estiver com prazo de 3 dias ou menos, você recebe um e-mail automático com a lista. Se não houver nada urgente, o script apenas avisa no terminal e não envia e-mail.

## 🗺️ Próximos passos (roadmap)

- [x] **V2:** ler vários processos de uma planilha de uma vez.
- [x] **V3:** enviar alertas automáticos por e-mail quando um prazo estiver próximo do vencimento.
- [ ] **V4:** interface visual simples (com Streamlit) para consultar os prazos sem precisar mexer no código.

## 🛠️ Tecnologias

- Python 3
- Módulos nativos: `datetime`, `csv`, `smtplib`, `email`, `os`

## 👩‍💻 Autora

Isadora Barreto — advogada em transição para o mundo da tecnologia, aprendendo a programar para automatizar tarefas do dia a dia jurídico.
