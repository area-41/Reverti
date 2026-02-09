"""
Schemas de Validação - Projeto Reverti (Pós UTFPR)
Focado no Módulo 05: Validação de Dados e Tipagem com Pydantic.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime

class ResiduoBase(BaseModel):
    """Atributos básicos de um resíduo compartilhados entre criação e leitura."""
    material: str = Field(..., example="Alumínio", description="Tipo de material detectado")
    peso: float = Field(..., gt=0, example=150.5, description="Peso em gramas (deve ser maior que zero)")
    qualidade: float = Field(..., ge=0, le=1, example=0.95, description="Grau de pureza/estado de 0 a 1")

class ResiduoCreate(ResiduoBase):
    """Dados enviados pelo App Mobile ao registrar um novo resíduo."""
    usuario_id: int
    codigo: str = Field(..., example="SCAN-9982")
    altura: float
    largura: float
    valor: float

class ResiduoRead(ResiduoBase):
    """Dados retornados pela API ao consultar o histórico."""
    codigo: str
    valor: float
    data: datetime

    class Config:
        orm_mode = True # Permite que o Pydantic leia dados de objetos da classe Residuo

class ContaRead(BaseModel):
    """Schema para visualização do saldo e histórico financeiro."""
    saldo_acumulado: float
    historico_transacoes: List[dict]

class UsuarioRead(BaseModel):
    """Dados públicos do perfil do usuário Reverti."""
    id_usuario: int
    nome: str
    email: EmailStr
    conta: ContaRead

    class Config:
        orm_mode = True