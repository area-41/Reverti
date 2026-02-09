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


### Para testar o projeto, utilize o guia criado no arquivo GUIADETESTE.md


## Conclusão Técnica: Arquitetura do Sistema Reverti

O projeto Reverti foi desenvolvido como uma solução full-stack em Python, integrando as competências centrais da pós-graduação para resolver o desafio da logística reversa. A base do sistema utiliza Estruturas de Dados e Algoritmos (Módulo 01) para a manipulação eficiente de históricos e Orientação a Objetos Avançada (Módulo 02) para a modelagem robusta de usuários e transações financeiras. A escalabilidade é garantida por meio de Computação Paralela e Distribuída (Módulo 03) com o uso de Celery, permitindo o processamento assíncrono de tarefas pesadas de visão computacional.

A automação de dados de mercado foi implementada via RPA (Módulo 04), garantindo cotações em tempo real, enquanto a camada de serviços foi exposta através de uma API REST com FastAPI (Módulo 05), seguindo padrões modernos de validação e segurança com Pydantic. Por fim, a arquitetura modular e a suite de testes unitários preparam o ecossistema para uma implantação contínua em Ambientes de Nuvem e Integração Mobile (Módulo 06). O resultado é uma aplicação resiliente, documentada e pronta para o mercado.

