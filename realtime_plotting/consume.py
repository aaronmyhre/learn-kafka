from kafka import KafkaConsumer, KafkaProducer
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import json

#documentation
#http://kafka-python.readthedocs.io/en/master/index.html

#mkvirtualenv -p python3
#pip install pip install kafka-python

topic = "test3"
server='localhost:9092'

def consume():
    plt.ion()
    consumer = KafkaConsumer(topic,
                            bootstrap_servers=server,
                            auto_offset_reset='latest',
                            enable_auto_commit=False,
                            group_id=5
                            #value_deserializer=msgpack.loads
                            )
    for msg in consumer:
        print(msg)
        msgDecode = json.loads(msg.value.decode('utf-8'))
        amount = msgDecode['orderAmount']
        xMax = int(str(msg.timestamp)[7:11])
        print(amount)
        print(xMax)

        plt.axis([xMax - 100, xMax,0, 100])
        plt.scatter(xMax, amount)
        plt.pause(.1)


consume()
