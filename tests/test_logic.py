"""
Testes Unitários Reverti - Projeto Pós UTFPR
Focado na validação de regras de negócio e integridade de dados.
"""

import pytest
from core.models import Usuario, Conta, Residuo
from core.utils import calcular_estatisticas_basicas, ordenar_residuos_por_valor


# --- FIXTURES (Configuração de dados para os testes) ---

@pytest.fixture
def usuario_exemplo():
    """Cria um ambiente de teste com usuário e conta zerada."""
    conta = Conta(id_conta=1)
    return Usuario(id_usuario=123, nome="Carlos Teste", email="carlos@teste.com", conta=conta)


# --- TESTES DE MODELOS (Módulo 02) ---

def test_registro_residuo_credita_saldo(usuario_exemplo):
    """Verifica se ao registrar um resíduo, o saldo da conta é atualizado corretamente."""
    residuo = Residuo(
        codigo="SCAN-001", material="Alumínio", peso=100.0,
        altura=10.0, largura=5.0, qualidade=1.0, valor=5.50
    )

    usuario_exemplo.registrar_residuo(residuo)

    assert usuario_exemplo.conta.saldo_acumulado == 5.50
    assert len(usuario_exemplo.residuos_registrados) == 1
    assert usuario_exemplo.residuos_registrados[0].material == "Alumínio"


def test_historico_transacoes_registro(usuario_exemplo):
    """Garante que cada crédito gera uma entrada no histórico de transações."""
    residuo = Residuo(
        codigo="SCAN-002", material="PET", peso=200.0,
        altura=20.0, largura=8.0, qualidade=0.8, valor=1.20
    )

    usuario_exemplo.registrar_residuo(residuo)
    historico = usuario_exemplo.conta.historico_transacoes

    assert len(historico) == 1
    assert "PET" in historico[0]['descricao']
    assert historico[0]['valor'] == 1.20


# --- TESTES DE ALGORITMOS (Módulo 01) ---

def test_ordenacao_residuos():
    """Valida a lógica de ordenação por valor implementada em utils.py."""
    dados_sujos = [
        {"material": "PET", "valor": 1.50},
        {"material": "Alumínio", "valor": 8.00},
        {"material": "Papel", "valor": 0.50}
    ]

    ordenados = ordenar_residuos_por_valor(dados_sujos, decrescente=True)

    assert ordenados[0]['material'] == "Alumínio"
    assert ordenados[-1]['material'] == "Papel"


def test_estatisticas_vazias():
    """Garante que o cálculo de estatísticas não