# ♻️ Reverti - Inteligência Artificial na Reciclagem

O **Reverti** é um projeto de síntese desenvolvido para consolidar o aprendizado do curso de **Pós-Graduação em Python da UTFPR**. A aplicação utiliza Visão Computacional para identificar resíduos domésticos, calcular recompensas financeiras e gerenciar o destino correto dos materiais.

---

## Integração com a Grade Curricular (UTFPR)

O projeto foi dividido em módulos que acompanham a evolução das disciplinas:

### MÓDULO 01 & 02: Fundamentos e OO
* **Lógica & Estrutura de Dados:** Implementação de algoritmos para gestão de histórico e processamento de listas de resíduos.
* **Orientação a Objetos:** Modelagem das classes `Usuario`, `Conta`, `Residuo` e `Instituicao`, utilizando herança e composição.
* **Visualização de Dados:** Geração de dashboards com `Matplotlib` e `Pandas` para exibir o impacto ambiental do usuário.

### MÓDULO 03 & 04: Escalabilidade e Automação
* **Computação Paralela/Distribuída:** Estrutura preparada para processamento assíncrono de imagens de alta resolução.
* **Acesso a Banco de Dados:** Persistência de dados utilizando SQLite/PostgreSQL.
* **RPA (Robot Process Automation):** Bot de automação que realiza web scraping para atualizar os preços das commodities (alumínio, plástico) em tempo real.

### MÓDULO 05 & 06: Web, Mobile e Nuvem
* **Web Back-end:** API robusta construída com `FastAPI` para comunicação entre o App e o Banco de Dados.
* **Dispositivos Móveis:** Interface desenvolvida para dispositivos móveis com foco na captura de imagem via câmera.
* **Cloud:** Configuração de deploy em nuvem para garantir disponibilidade global.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Web Framework:** FastAPI / Uvicorn
* **Data Science:** Pandas / Matplotlib
* **RPA:** BeautifulSoup4 / Requests
* **Data Validation:** Pydantic

---

## Como Executar (Exemplo em Colab/Local)

1. **Instale as dependências:**
   ```bash
   pip install fastapi uvicorn matplotlib pandas requests beautifulsoup4
