# -*- coding: utf-8 -*- 

import json, uuid
from random import randint

# Config
payload_file = open('notifier_payload.json', 'r')
payload_data = payload_file.read()
payload_file.close()

def generate_hash():
    hash =  uuid.uuid4().hex
    return str(hash)

def update_payload():
    data = json.loads(payload_data)
    data['body']['msg_hash']= generate_hash()
    payload_update = json.dumps(data)
    return payload_update
