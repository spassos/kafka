from confluent_kafka import Producer
import sys
from faker import Faker
from model.conta import Conta
from serializer.class_serializer import ClassEncoder
import json
import uuid

if __name__ == '__main__':

    # Producer configuration
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    conf = {'bootstrap.servers': 'localhost:29092'}

    # Create Producer instance
    p = Producer(**conf)

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print('Message failed delivery {0}'.format(0))
        else:
            print('Message delivered to {0} [{1}] @ {2}'.format(msg.topic(), msg.partition(), msg.offset()))

    # Read lines from stdin, produce each line to Kafka
    try:
        faker = Faker(['pt-BR'])
        c = Conta(cliente = faker.name(), agencia = 1, conta=faker.random_number(digits=10), data_abertura=faker.date(),
                  saldo=50.0, ativo=True)
        message =  json.dumps(c.repr_json(), cls=ClassEncoder).encode('utf-8')
        key = str(uuid.uuid4())

        p.produce('topico-demo-python', key=key, value=message, callback=delivery_callback)

    except BufferError:
        print('Local producer queue is full ({0} messages awaiting delivery): try again.'.format(len(p)))
    # Serve delivery callback queue.
    # NOTE: Since produce() is an asynchronous API this poll() call
    #       will most likely not serve the delivery callback for the
    #       last produce()d message.
    p.poll(0)

    # Wait until all messages have been delivered
    print('Waiting for {0} deliveries.'.format(len(p)))
    p.flush()