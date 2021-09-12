import os, logging, json
from dotenv import load_dotenv
from elasticsearch import Elasticsearch


# Load environment variables
load_dotenv()
user = str(os.environ.get('ES_USER'))
password = str(os.environ.get('ES_PASSWORD'))
host = str(os.environ.get('ES_HOST'))
port = os.environ.get('ES_PORT')

# Log config
logging.basicConfig(level=logging.INFO, format="%(asctime)s : %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger('elasticsearch').setLevel(logging.CRITICAL)

def logging_override(name: str, extra: dict):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    basic_dict = {"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}
    full_dict = {**basic_dict, **extra}
    stream_formatter = logging.Formatter(json.dumps(full_dict))
    stream_handler.setFormatter(stream_formatter)
    if not logger.handlers:
        logger.addHandler(stream_handler)
    logger.handlers[0] = stream_handler
    logger = logging.LoggerAdapter(logger, extra)
    return logger

# Create connection
def conn_es():
    es_conn = ("https://" + user + ":" + password + "@" + host + ":" + port)
    es = Elasticsearch([es_conn])
    return es

def send_log(doc):
    logging.basicConfig(level="INFO")
    logger = logging_override("json", doc)
    logging.info("Connecting to ES...")
    es = conn_es()
    res = es.index(index="test-index", id=1, body=doc)
    logging.info(res['result'])
    res = es.get(index="test-index", id=1)
    logging.info(res['_source'])
    es.indices.refresh(index="test-index")
    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    logging.info("Got %d Hits:" % res['hits']['total']['value'])
    for hit in res['hits']['hits']:
        print("%(app_name)s %(username)s" % hit["_source"])

# if __name__ == "__main__":
#     doc = {'app_name': 'lambda-webhook', 'username': 'Jack Sparrow'}
#     send_log(doc)