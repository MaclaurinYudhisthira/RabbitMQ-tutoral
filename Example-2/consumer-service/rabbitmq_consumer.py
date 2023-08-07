import pika
import json

class RabbitMQConsumer:
    def __init__(self, message_queue_host:str, message_queue_name:str, username: str, password:str) -> None:
        
        self.message_queue_name = message_queue_name
        self.message_queue_host = message_queue_host
        
        self.credentials = pika.PlainCredentials(username, password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.message_queue_host,credentials=self.credentials))
        self.channel = self.connection.channel()
        
        self.channel.queue_declare(queue=self.message_queue_name)
    
    def __repr__(self) -> str:
        return f'RabbitMQConsumer("{self.message_queue_host}", "{self.message_queue_name}"'

    @staticmethod
    def callback(ch, method, properties, body) -> None:
        payload = json.loads(body)
        processed_payload = proc(payload)
        print("Received:", processed_payload)

        # Notify the REST API here

        # Acknowledge the message to remove it from the queue
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_listening(self) -> None:
        self.channel.basic_consume(queue=self.message_queue_name, on_message_callback=self.callback)
        print("Waiting for messages...")
        self.channel.start_consuming()
    

def proc(payload):
    # Simulate some processing operation
    print("Processing payload")
    payload['processed'] = True
    return payload