from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from conf import config

tup = []
for key, value in config.cfg['kafka'].items():
    tup.append(key + "=" + value)

kafka_producer = KafkaProducer(','.join(tup))


def send(msg):
    kafka_producer.send()
