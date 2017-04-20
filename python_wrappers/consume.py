from kafka import KafkaConsumer, KafkaProducer

#documentation
#http://kafka-python.readthedocs.io/en/master/index.html

#mkvirtualenv -p python3
#pip install pip install kafka-python

topic = "test1"
server='localhost:9092'

def consume():
    consumer = KafkaConsumer(topic, bootstrap_servers=server)
    for msg in consumer:
        print(msg)

consume()
