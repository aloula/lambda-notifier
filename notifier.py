import urllib3, json, sys

# Init sender
http = urllib3.PoolManager() 

# Lambda function 
def send_webhook(event, context):
    for record in event['Records']:
        print("Received Message:", record)
        payload = (record['body'])
        data_json = json.loads(payload)
        url = (data_json['receiverUrl'])
        resp = http.request('POST', url, body=payload)
        status_code = resp.status
        print({"message": payload, "status_code": status_code, "response": resp.data})
        assert status_code == 200, "Webhook NOT delivered!"
        print ("Webhook delivered!")
        

