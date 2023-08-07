import os
from dotenv import load_dotenv
from rabbitmq_consumer import RabbitMQConsumer

load_dotenv()

QUEUE_NAME=os.getenv('QUEUE_NAME')
QUEUE_HOST=os.getenv('QUEUE_HOST')
QUEUE_USERNAME=os.getenv('QUEUE_USERNAME')
QUEUE_PASSWORD=os.getenv('QUEUE_PASSWORD')


rabbit_mq = RabbitMQConsumer(
    message_queue_host=QUEUE_HOST,
    message_queue_name=QUEUE_NAME,
    username=QUEUE_USERNAME,
    password=QUEUE_PASSWORD
)
