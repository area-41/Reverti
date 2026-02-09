## Guia de Teste: Interface Swagger (Reverti API)
Assim que você rodar o comando uvicorn web_api.main:app --reload, poderá acessar a documentação interativa.

1. Acessando a Documentação
Abra o navegador e digite o endereço:

http://127.0.0.1:8000/docs

2. Testando o Registro de Resíduo (POST)
Para simular o aplicativo mobile enviando um descarte:

Clique no endpoint POST /api/v1/registrar-residuo.

Clique no botão "Try it out".

No corpo do JSON, o Swagger já preencherá os campos baseados nos seus schemas.py. Você pode alterar os valores:

JSON
    {
      "usuario_id": 1,
      "material": "Alumínio",
      "peso": 350.5,
      "valor": 2.05,
      "codigo": "SCAN-UTFPR-2024",
      "altura": 12.0,
      "largura": 6.5,
      "qualidade": 0.95
    }
    
Clique em "Execute".

O que acontece por trás: O sistema instanciará a classe Residuo, creditará o valor na Conta do usuário e disparará a BackgroundTask para gerar o gráfico.

3. Visualizando o Dashboard (GET)
Após registrar um resíduo, teste o retorno visual:

Vá no endpoint GET /api/v1/dashboard/{usuario_id}.

Clique em "Try it out" e digite 1 no campo usuario_id.

Ao clicar em "Execute", o Swagger exibirá diretamente a imagem do gráfico gerado pelo Matplotlib na seção "Response body".
