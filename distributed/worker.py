from celery import Celery
import time

# Configuração do Celery (Módulo 03)
# Em produção, o 'broker' seria uma URL do Redis ou RabbitMQ
app_celery = Celery('eco_tasks', broker='redis://localhost:6379/0')


@app_celery.task
def processar_imagem_ia(residuo_id, caminho_imagem):
    """
    Simula o processamento pesado de Visão Computacional.
    Esta função roda em um processo separado ou até em outro servidor.
    """
    print(f"🤖 Iniciando análise da imagem para o resíduo {residuo_id}...")

    # Simula o tempo que a IA leva para detectar o objeto (3 segundos)
    time.sleep(3)

    resultado = {
        "detectado": "Garrafa PET",
        "confianca": 0.98,
        "status": "Processado"
    }

    print(f"✅ Análise concluída: {resultado['detectado']}")
    return resultado