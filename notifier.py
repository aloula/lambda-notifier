import urllib3, json, logging
from es_log import send_log

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
        logging.info("Sending received msg to ES...")
        send_log(payload)
        data_json = json.loads(payload)
        url = (data_json['receiverUrl'])
        resp = http.request('POST',url, body=payload)
        receiver_resp = {"message": payload, "status_code": resp.status, "response": resp.data}
        logging.info(receiver_resp)
        send_log(receiver_resp)
