from kafka import KafkaConsumer, KafkaProducer

#documentation
#http://kafka-python.readthedocs.io/en/master/index.html

#mkvirtualenv -p python3
#pip install pip install kafka-python

topic = "test"
server='localhost:9092'

def consume():
    consumer = KafkaConsumer(topic, bootstrap_servers=server)
    print('b')
    for msg in consumer:
        print(msg)

    print('asd')

def produce():
    producer = KafkaProducer(bootstrap_servers=server)
    for _ in range(100):
        producer.send('foo', b'bar')

#consume()
produce()
