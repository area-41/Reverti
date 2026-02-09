"""
Módulo de Visualização - Projeto Reverti (Pós UTFPR)
Focado no Módulo 02: Visualização de Dados com Matplotlib e Pandas.
"""

import matplotlib.pyplot as plt
import pandas as pd
from typing import List
from core.models import Residuo


def gerar_dashboard_usuario(nome_usuario: str, lista_residuos: List[Residuo]):
    """
    Gera um dashboard visual do impacto ambiental do usuário no sistema Reverti.

    Args:
        nome_usuario (str): Nome para exibir no título.
        lista_residuos (List[Residuo]): Lista de objetos da classe Residuo.
    """
    if not lista_residuos:
        print(f"[Reverti] Sem dados para gerar dashboard de {nome_usuario}.")
        return

    # 1. Conversão para DataFrame (Padrão para análise de dados)
    dados = [
        {"material": r.material, "peso": r.peso, "valor": r.valor}
        for r in lista_residuos
    ]
    df = pd.DataFrame(dados)

    # 2. Preparação dos subplots (Gráfico de Barras e Pizza)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle(f"Dashboard de Sustentabilidade - Reverti ({nome_usuario})", fontsize=18)

    # Gráfico 1: Total de Peso por Material
    resumo_peso = df.groupby('material')['peso'].sum()
    resumo_peso.plot(kind='bar', ax=ax1, color=['#2ecc71', '#3498db', '#f1c40f', '#e74c3c'])
    ax1.set_title("Volume Reciclado por Material (g)")
    ax1.set_xlabel("Material")
    ax1.set_ylabel("Peso (gramas)")
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    # Gráfico 2: Distribuição de Valor Gerado (Pizza)
    resumo_valor = df.groupby('material')['valor'].sum()
    resumo_valor.plot(kind='pie', ax=ax2, autopct='%1.1f%%', startangle=140, shadow=True,
                      colors=['#2ecc71', '#3498db', '#f1c40f', '#e74c3c'])
    ax2.set_title("Distribuição Financeira das Recompensas")
    ax2.set_ylabel("")  # Remove label lateral do gráfico de pizza

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Salva o gráfico para ser exibido no App ou Web (Módulo 05 e 06)
    plt.savefig(f"assets/dashboard_{nome_usuario.lower().replace(' ', '_')}.png")
    plt.show()


def plotar_tendencia_rpa(historico_precos: dict):
    """
    Visualiza a variação de preços coletados pelo RPA (Módulo 04).
    """
    # Exemplo de expansão futura para visualização de séries temporais
    pass