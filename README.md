## AWS Lambda Webhook Notifier

Python Lambda function to send Webhooks triggered by SQS messages

![Alt text](lambda_webhooks.png?raw=true "Diagram")


### Requisites:

* [Serverless Framework](https://www.serverless.com/framework/docs/getting-started/)


### Installation:

```Bash
$ sudo apt install python3 python3-pip python3-dev python3-venv
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```


### Deploy:

1 - Create SQS Queue with default settings

2 - Copy the ARN and update the `serverless.yml` file

3 - Copy "Your unique URL" from https://webhook.site/ and change it in `notifier_payload.json` file

4 - Deploy the project changing the region according to your AWS account settings

```bash
$ sls deploy --region us-east-2 --verbose
```

### Test

Execute the <send_webhooks.py> passing the URL and number of webhooks to be send

```Bash
$ ./send_webhooks.py -q "https://sqs.us-east-2.amazonaws.com/530234245000/hmg-lb-notifier" -n 10
```

### TODO:
- Ajustar <serverless.yml> para pegar o ARN da Queue como variável