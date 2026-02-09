"""
Worker Distribuído Reverti - Projeto Pós UTFPR
Focado no Módulo 03: Processamento Assíncrono e Filas de Tarefas.
"""

import time
import logging
from celery import Celery

# Configuração do Log para o Worker
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [Reverti Worker] - %(message)s')

# Instância do Celery
# 'broker': onde as mensagens ficam guardadas (ex: Redis ou RabbitMQ)
# 'backend': onde o resultado da tarefa é armazenado
app_worker = Celery(
    'reverti_tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)


@app_worker.task(name="tasks.processar_visao_computacional")
def processar_visao_computacional(imagem_id: str, usuario_id: int):
    """
    Simula o processamento pesado de Redes Neurais para identificação de resíduos.

    Em um cenário real de Módulo 03, este worker poderia estar rodando em 
    uma máquina com GPU enquanto a API roda em um servidor web comum.
    """
    logging.info(f"Iniciando análise de IA para imagem {imagem_id} do usuário {usuario_id}")

    # Simula o delay do processamento de Deep Learning (3 segundos)
    time.sleep(3)

    # Resultado simulado da detecção
    resultado = {
        "material": "Alumínio",
        "confianca": 0.992,
        "dimensoes": {"altura": 12.5, "largura": 6.5},
        "status": "sucesso"
    }

    logging.info(f"Análise finalizada para {imagem_id}: Identificado como {resultado['material']}")
    return resultado


@app_worker.task(name="tasks.gerar_relatorio_pdf")
def gerar_relatorio_pdf(usuario_id: int):
    """
    Simula a geração de um relatório PDF pesado com o histórico de sustentabilidade.
    """
    logging.info(f"Gerando relatório consolidado para o usuário {usuario_id}")
    time.sleep(5)
    return {"status": "Relatório pronto", "url": f"/downloads/relatorio_{usuario_id}.pdf"}