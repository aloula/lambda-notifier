#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Simple test script to generate SQS msgs 
# Usage: python send_webhooks.py -q <queue_url> -n <webhooks>
# Author: Alexsander Loula - 2021/9/10

# dependencies
import boto3, sys, argparse
from datetime import datetime
from generate_payload import update_payload

# create SQS client
sqs = boto3.client('sqs', region_name='us-east-2')
# boto3.setup_default_session(profile_name='retro')

# send message to SQS queue
def send_to_queue():
    payload = update_payload()
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=payload,
        MessageAttributes={
            'from': {
            'StringValue': '2021-09-10',
            'DataType': 'String'
            }
        }
        )
    print("Message ID:", response['MessageId'])


# main
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--queue_url")
    parser.add_argument("-n", "--webhooks")
    args = parser.parse_args()
    if args.queue_url:
        queue_url = args.queue_url
    if args.webhooks:        
        webhooks_input = int(args.webhooks)
        count = 1
        start = datetime.now()
        start_string = start.strftime("%H:%M:%S")    
        while count <= webhooks_input:
            print('Sending webhook ' + str(count) + ' from ' + str(webhooks_input) + '...')
            send_to_queue()
            count+=1
        end = datetime.now()
        end_string = end.strftime("%H:%M:%S") 
        print("Start:", start_string)
        print("End:", end_string)  
        total = end - start
        delta_sec = round(total.total_seconds(),2)
        webhooks_per_sec = round(webhooks_input/total.total_seconds(),2)
        print('Sent Webhooks:', webhooks_input)
        print('Total Time(sec):', delta_sec) 
        print('Webhooks/Sec:', webhooks_per_sec)

    else:
        print ('Usage: ./send_webhooks.py -q <queue_url> -n <webhooks>')
        print ('Example: ./send_webhooks.py -q "https://sqs.us-east-2.amazonaws.com/XXX/lambda-notifier" -n 100')
        sys.exit(2) 
sys.exit(0)