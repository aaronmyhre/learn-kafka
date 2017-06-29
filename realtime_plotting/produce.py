from kafka import KafkaProducer
import time
import random
import datetime
import json

#documentation
#http://kafka-python.readthedocs.io/en/master/index.html

#mkvirtualenv -p python3
#pip install pip install kafka-python

topic = "test3"
server='localhost:9092'

producer = KafkaProducer(bootstrap_servers=server,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8')
                         )

while True:
    orderAmount = random.randint(0, 100)
    orderType = "purchase"
    orderDateTime = str(datetime.datetime.now())

    order = {
        "orderAmount": orderAmount,
        "orderType": orderType,
        "orderDateTime": orderDateTime
    }
    print(order)

    #producer.send(topic, b'1')
    #producer.send(topic, order)
    producer.send(topic, order)
    time.sleep(.05)
