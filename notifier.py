import urllib3, json, logging

# Log config
logging.basicConfig(level=logging.INFO, format="%(asctime)s : %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)

# Init sender
http = urllib3.PoolManager() 

# Lambda function 
def send_webhook(event, context):
    for record in event['Records']:
        logging.info("Received Message:", record)
        payload = (record['body'])
        data_json = json.loads(payload)
        url = (data_json['receiverUrl'])
        resp = http.request('POST',url, body=payload)
        logging.info({
            "message": payload, 
            "status_code": resp.status, 
            "response": resp.data
    })
