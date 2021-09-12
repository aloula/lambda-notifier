## AWS Lambda Webhook Notifier

Python Lambda function to send Webhooks triggered by SQS messages

![Alt text](lambda_webhooks.png?raw=true "Diagram")


### Requisites:

* [Serverless Framework](https://www.serverless.com/framework/docs/getting-started/)


### Deploy:

1 - Create SQS Queue with default settings

2 - Copy the ARN and update the `serverless.yml` file

3 - Deploy the project changing the region according to your AWS account settings

```bash
$ sls deploy --region us-east-2 --verbose
```

### Test

1 - Set a virtual env and install the dependencies:

```bash
$ sudo apt install python3 python3-pip python3-dev python3-venv
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

2 - Copy "Your unique URL" from https://webhook.site/ and change it in `notifier_payload.json` file

3 - Execute the <send_webhooks.py> passing the URL and number of webhooks to be send

```bash
$ ./send_webhooks.py -q "https://sqs.us-east-2.amazonaws.com/XXXXX/webhooks" -n 10
```