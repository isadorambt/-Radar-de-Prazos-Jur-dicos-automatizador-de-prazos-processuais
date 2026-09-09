<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Radar%20de%20Prazos%20Jur%C3%ADdicos&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Direito%20%2B%20C%C3%B3digo%20%3D%20nunca%20mais%20perder%20um%20prazo&descAlignY=55&descSize=16"/>

<a href="https://readme-typing-svg.demolab.com">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=A78BFA&center=true&vCenter=true&width=600&lines=Automatizando+prazos+processuais+com+Python;De+script+simples+a+interface+visual;Feito+por+uma+advogada+aprendendo+a+programar" alt="Typing SVG" />
</a>

<br><br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Ativo-3ddc84?style=for-the-badge)
![License](https://img.shields.io/badge/Licença-MIT-informational?style=for-the-badge)

</div>

<br>

## 📌 Sobre o projeto

Um script em Python que calcula automaticamente a data final de um prazo processual, considerando dias úteis, feriados nacionais e o recesso forense.

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
