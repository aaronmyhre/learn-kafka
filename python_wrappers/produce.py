from kafka import KafkaProducer
import time

#documentation
#http://kafka-python.readthedocs.io/en/master/index.html

#mkvirtualenv -p python3
#pip install pip install kafka-python

topic = "test"
server='localhost:9092'


producer = KafkaProducer(bootstrap_servers=server)
while True:
    producer.send('foobar', b'some_message_bytes')
    print('asd')
    time.sleep(1)
