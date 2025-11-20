## AWS Lambda Webhook Notifier

Python Lambda function to send Webhooks triggered by SQS messages

![Alt text](lambda_webhooks.png?raw=true "Diagram")


### Requisitos:

* [Serverless Framework](https://www.serverless.com/framework/docs/getting-started/)
* Node.js LTS (recomendado usar [nvm](https://github.com/nvm-sh/nvm))
* Python 3.12+
* AWS CLI configurado com credenciais válidas


### Deploy:

1 - Crie uma fila SQS com configurações padrão no console AWS

2 - Copie o ARN da fila e atualize o arquivo `serverless.yml`

3 - Faça o deploy do projeto alterando a região de acordo com as configurações da sua conta AWS:

```bash
$ sls deploy --region us-east-2 --verbose
```

### Teste Local

1 - Configure um ambiente virtual e instale as dependências:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

2 - Copie "Your unique URL" do https://webhook.site/ e altere no arquivo `notifier_payload.json`

3 - Execute o script `send_webhooks.py` passando a URL da fila SQS e o número de webhooks a serem enviados:

```bash
$ ./send_webhooks.py -q "https://sqs.us-east-2.amazonaws.com/XXXXX/webhooks" -n 10
```

### Estrutura do Projeto

```
├── notifier.py              # Função Lambda principal
├── send_webhooks.py         # Script de teste para enviar mensagens SQS
├── generate_payload.py      # Gerador de payload para testes
├── notifier_payload.json    # Template do payload de teste
├── serverless.yml           # Configuração do Serverless Framework
├── requirements.txt         # Dependências Python
└── README.md
```

### Configuração

A função Lambda está configurada para:
- Runtime: Python 3.12
- Timeout: 10 segundos
- Trigger: Fila SQS com batch size de 1 mensagem
- Dead Letter Queue (DLQ): Para mensagens com falha no processamento

### Monitoramento

Logs da função Lambda podem ser visualizados no CloudWatch:
```bash
$ sls logs -f Webhook --tail
```