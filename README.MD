# 💰 Dashboard de Finanças Pessoais Automático

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Interface-FF4B4B.svg)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-Tratamento%20de%20Dados-150458.svg)](https://pandas.pydata.org)

Uma aplicação interativa desenvolvida em Python para automatizar a leitura, limpeza e visualização de extratos bancários (arquivos `.csv`). O projeto transforma dados brutos e desorganizados em insights financeiros claros através de um dashboard web moderno.

> 🔒 **Nota sobre Privacidade:** Este projeto foi desenhado seguindo boas práticas de segurança. Nenhum dado financeiro real ou sensível é enviado para o repositório público (configurado via `.gitignore`). Para fins de demonstração, o sistema carrega uma base de dados fictícia caso nenhum arquivo real seja fornecido localmente.

---

## 🎯 O Problema vs. A Solução

* **O Problema:** Exportar extratos bancários geralmente resulta em arquivos CSV confusos, com textos sujos (ex: `UBER *TRIP RIDE HELP`), formatos de data misturados e valores em formato de texto brasileiro (`R$ 1.250,50`), impossibilitando análises matemáticas rápidas.
* **A Solução:** Um pipeline em Python que detecta o arquivo automaticamente, limpa os caracteres especiais, padroniza os tipos de dados usando **Pandas**, calcula métricas de fluxo de caixa e renderiza gráficos interativos com **Plotly** dentro de uma interface **Streamlit**.

---

## 🛠️ Tecnologias e Ferramentas

* **Python:** Linguagem base do projeto.
* **Pandas:** Manipulação, limpeza e tratamento dos dados textuais e numéricos.
* **Streamlit:** Construção da interface gráfica e estrutura web do dashboard.
* **Plotly Express:** Geração de gráficos dinâmicos e interativos.
* **OS (Python Built-in):** Manipulação de caminhos de arquivos de forma multiplataforma (Windows/Mac/Linux).

---

## 📊 Funcionalidades Recentes

- [x] **Leitura Automática:** Identificação dinâmica de novos arquivos `.csv` na pasta de entrada.
- [x] **Pipeline de Data Cleaning:** Tratamento de strings, remoção de símbolos monetários e conversão de tipos de dados para o padrão computacional.
- [x] **Métricas de Negócio:** Cards dinâmicos com Total de Receitas, Total de Despesas e Saldo Final.
- [x] **Gráficos Interativos:** Linha de tendência de fluxo de caixa diário.
- [x] **Visualizador de Dados:** Tabela expansível para auditoria do extrato já tratado.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Antes de começar, você vai precisar ter o [Python](https://www.python.org/) instalado em sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
   cd NOME_DO_REPOSITORIO