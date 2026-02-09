"""
API Principal Reverti - Projeto Pós UTFPR
Focado no Módulo 05: Desenvolvimento Web Back-end.
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
import os

# Importando a lógica do Reverti
from core.models import Usuario, Conta, Residuo
from data_viz.generator import gerar_dashboard_usuario

app = FastAPI(title="Reverti API - Sistema de Reciclagem Inteligente")

# --- SIMULAÇÃO DE BANCO DE DADOS (Módulo 04) ---
# Em um ambiente real, usaríamos SQLAlchemy ou Motor (MongoDB)
banco_usuarios = {}

# --- SCHEMAS DE ENTRADA (Validação Pydantic) ---
class RegistroResiduoInput(BaseModel):
    usuario_id: int
    material: str
    peso: float
    valor: float
    codigo: str
    altura: float
    largura: float
    qualidade: float

# --- ROTAS DA API ---

@app.on_event("startup")
async def startup_event():
    """Inicializa um usuário de teste ao subir a API."""
    conta_inicial = Conta(id_conta=1001)
    user_teste = Usuario(id_usuario=1, nome="João Silva", email="joao@utfpr.edu.br", conta=conta_inicial)
    banco_usuarios[1] = user_teste

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao ecossistema Reverti", "status": "online"}

@app.post("/api/v1/registrar-residuo")
async def api_registrar(entrada: RegistroResiduoInput, background_tasks: BackgroundTasks):
    """
    Rota principal para registro de resíduos escaneados via Mobile (Módulo 06).
    Usa BackgroundTasks para não travar a resposta enquanto gera o gráfico.
    """
    user = banco_usuarios.get(entrada