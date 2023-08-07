import pika
import json

class RabbitMQSender:
    def __init__(self, message_queue_host:str, message_queue_name:str, username: str, password:str, exchange:str = '') -> None:
        
        self.message_queue_name = message_queue_name
        self.message_queue_host = message_queue_host
        self.exchange = exchange
        
        self.credentials = pika.PlainCredentials(username, password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.message_queue_host, credentials=self.credentials))
        self.channel = self.connection.channel()
        
        self.channel.queue_declare(queue=self.message_queue_name)

    def __repr__(self) -> str:
        return f'RabbitMQSender("{self.message_queue_host}", "{self.message_queue_name}", "{self.exchange}")'

    def send_message(self, payload:dict = {}) -> None:
        self.channel.basic_publish(exchange=self.exchange,routing_key=self.message_queue_name,body=json.dumps(payload))

    def close_conn(self) -> None:
        self.connection.close() 