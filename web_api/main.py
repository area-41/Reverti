from distributed.worker import processar_imagem_ia


@app.post("/scan-foto/")
async def scan_foto(usuario_id: int):
    # .delay() envia a tarefa para a fila distribuída imediatamente
    task = processar_imagem_ia.delay(usuario_id, "caminho/da/foto.jpg")

    return {
        "mensagem": "Foto recebida! Estamos analisando em segundo plano.",
        "task_id": task.id
    }