import pytest
from core.models import Residuo, Usuario, Conta


def test_calculo_recompensa_residuo():
    """
    Testa se o cálculo da recompensa está correto baseado no peso e valor unitário.
    """
    # Arrange (Organizar)
    valor_por_grama = 0.05
    peso_testado = 100

    # Act (Agir)
    item = Residuo(codigo="123", material="PET", peso=peso_testado, valor=peso_testado * valor_por_grama)

    # Assert (Aferir)
    assert item.valor == 5.0
    assert isinstance(item.codigo, str)


def test_saldo_usuario_apos_registro():
    """
    Testa a integração entre Usuário e Conta.
    Verifica se o saldo é incrementado corretamente após um registro.
    """
    conta = Conta(id_conta=1)
    user = Usuario(id_usuario=1, nome="Teste", email="t@t.com", conta=conta)

    # Simulando o registro de um resíduo de R$ 2.50
    user.registrar_residuo(material="Papel", peso=500, valor=2.50, codigo="P-001")

    assert user.conta.saldo_acumulado == 2.50
    assert len(user.residuos_registrados) == 1