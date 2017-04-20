from kafka import KafkaConsumer, KafkaProducer
import numpy as np
import matplotlib.pyplot as plt
import random
import time

#documentation
#http://kafka-python.readthedocs.io/en/master/index.html

#mkvirtualenv -p python3
#pip install pip install kafka-python

topic = "test2"
server='localhost:9092'

def consume():
    #plt.ion()
    consumer = KafkaConsumer(topic,
                            bootstrap_servers=server,
                            auto_offset_reset='latest',
                            enable_auto_commit=False,
                            group_id=2
                            #value_deserializer=msgpack.loads
                            )
    for msg in consumer:
        print(msg)
        time.sleep(.1)
        #print("a")
        #amount = int(msg.value.decode())
        #xMax = int(str(msg.timestamp)[7:11])
        #print(amount)
        #print(xMax)

        #plt.axis([xMax - 100, xMax,0, 100])
        #plt.scatter(xMax, amount)
        #plt.pause(0)

consume()
