"""
Módulo de Modelos - Projeto Reverti (Pós UTFPR)
Focado no Módulo 02: Orientação a Objetos e Modelagem de Dados.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Conta:
    """
    Gerecia os créditos acumulados pelo usuário no sistema Reverti.
    """
    id_conta: int
    saldo_acumulado: float = 0.0
    historico_transacoes: List[dict] = field(default_factory=list)

    def creditar(self, valor: float, descricao: str):
        """Adiciona saldo à conta e registra a transação."""
        self.saldo_acumulado += round(valor, 2)
        self.historico_transacoes.append({
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "valor": valor,
            "descricao": descricao
        })


@dataclass
class InstituicaoDestinacao:
    """
    Representa o ponto de coleta ou empresa de reciclagem parceira.
    """
    id_inst: int
    nome_fantasia: str
    cnpj: str
    endereco: str
    materiais_aceitos: List[str]


@dataclass
class Residuo:
    """
    Classe principal que define um resíduo identificado pelo sistema Reverti.
    """
    codigo: str
    material: str
    peso: float  # em gramas
    altura: float  # em cm
    largura: float  # em cm
    qualidade: float  # 0.0 a 1.0
    valor: float
    data: datetime = field(default_factory=datetime.now)
    usuario_id: Optional[int] = None
    destino_id: Optional[int] = None


@dataclass
class Usuario:
    """
    Representa o utilizador final do aplicativo Reverti.
    Aplica o conceito de composição ao possuir uma 'Conta'.
    """
    id_usuario: int
    nome: str
    email: str
    conta: Conta
    residuos_registrados: List[Residuo] = field(default_factory=list)

    def registrar_residuo(self, residuo: Residuo):
        """
        Vincula um resíduo ao usuário e atualiza o saldo da conta.

        Este método centraliza a lógica de negócio necessária para o 
        aprendizado do Módulo 02 e 06.
        """
        residuo.usuario_id = self.id_usuario
        self.residuos_registrados.append(residuo)

        # Crédito automático na conta Reverti
        descricao = f"Reciclagem de {residuo.material} ({residuo.peso}g)"
        self.conta.creditar(residuo.valor, descricao)

        print(f"[Reverti Log] {residuo.material} registrado para {self.nome}.")