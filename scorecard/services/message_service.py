"""Message service module."""

import json
import os

import pika
from itsdangerous import URLSafeSerializer

user = os.getenv("RABBITMQ_DEFAULT_USER")
password = os.getenv("RABBITMQ_DEFAULT_PASS")
host = os.getenv("RABBITMQ_HOST")
port = os.getenv("RABBITMQ_PORT")


class MessageService:
    """Serializes and sends messages to a Rabbit message queue."""

    serializer = URLSafeSerializer(os.getenv("SECRET_KEY"), salt=os.getenv("HASH_SALT"))

    def send_invitation(self, player):
        token = self.serializer.dumps(json.dumps({"email": player.email, "roles": ["player"]}))
        url = f"{os.getenv('USER_REGISTRATION_URL')}/{token}"
        message = json.dumps(
            {"first_name": player.first_name, "last_name": player.last_name, "email": player.email, "url": url}
        )

        self._send("player_invitations", message)

    def _send(self, queue, message):
        credentials = pika.PlainCredentials(user, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, "/", credentials))
        channel = connection.channel()

        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange="", routing_key=queue, body=message)
        connection.close()
