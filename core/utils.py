"""
Módulo de Utilidades - Projeto Reverti (UTFPR)
Focado no Módulo 01: Estrutura de Dados e Algoritmos.
"""

from typing import List, Dict, Any


def ordenar_residuos_por_valor(residuos: List[Dict[str, Any]], decrescente: bool = True) -> List[Dict[str, Any]]:
    """
    Ordena uma lista de dicionários de resíduos com base no valor financeiro.

    Aplica o conceito de ordenação (Módulo 01) para exibir os itens
    mais valiosos primeiro no dashboard do usuário.

    Args:
        residuos (List[Dict]): Lista de registros de resíduos.
        decrescente (bool): Se True, ordena do maior para o menor.

    Returns:
        List[Dict]: A lista devidamente ordenada.
    """
    return sorted(residuos, key=lambda x: x.get('valor', 0), reverse=decrescente)


def filtrar_por_material(residuos: List[Dict[str, Any]], material_alvo: str) -> List[Dict[str, Any]]:
    """
    Filtra a estrutura de dados para retornar apenas um tipo específico de resíduo.

    Args:
        residuos (List[Dict]): Lista contendo todos os registros.
        material_alvo (str): O material desejado (ex: 'Alumínio').

    Returns:
        List[Dict]: Subconjunto de dados filtrados.
    """
    return [r for r in residuos if r.get('material') == material_alvo]


def calcular_estatisticas_basicas(residuos: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Realiza cálculos agregados sobre a estrutura de dados (Módulo 01).

    Returns:
        Dict: Dicionário com peso total, valor total e média de qualidade.
    """
    if not residuos:
        return {"peso_total": 0, "valor_total": 0, "media_qualidade": 0}

    total_peso = sum(r.get('peso', 0) for r in residuos)
    total_valor = sum(r.get('valor', 0) for r in residuos)
    media_qualidade = sum(r.get('qualidade', 0) for r in residuos) / len(residuos)

    return {
        "peso_total": total_peso,
        "valor_total": round(total_valor, 2),
        "media_qualidade": round(media_qualidade, 2)
    }