import datetime
import json
from time import sleep

from django.core.management.base import BaseCommand
from paho.mqtt.client import Client

from app.models import Data


class Command(BaseCommand):
    help = "Fetch data from MQTT broker"
    MQTT_ADDR = "broker.hivemq.com"  # DNS of the public MQTT broker
    MQTT_PORT = 1883

    MQTT_TOPIC_5 = "uos/cet235-0Marti0/data/value"  # Topic name for all data

    def __init__(self):
        super().__init__()
        # create MQTT client instance
        self.mqtt_client = Client()

    def on_message(self, mqttc, obj, msg):
        self.mqtt_callback(msg.topic, msg.payload)

    def mqtt_callback(self, topic: str, msg: bytes):
        """
        MQTT callback method, note how the topic is checked to determine how the received
        message from the MQTT broker should be handled, you could also base the operation
        of this callback method on the value of the received message, either way is
        acceptable
        """
        # Note: msg is a list of bytes so you need to convert these into a proper string
        # using the .decode("utf-8") method
        msg = msg.decode("utf-8")
        if topic == self.MQTT_TOPIC_5:
            data = json.loads(msg)
            print(f"Data reading: {data}")
            dt = datetime.datetime.strptime(data["date"] + " " + data["time"], "%a %d-%m-%Y %H:%M:%S")

            data_record = Data()
            data_record.temperature = data["temperature"]
            data_record.humidity = data["humidity"]
            data_record.timestamp = dt
            data_record.save()

            self.stdout.write(
                self.style.SUCCESS(f'New data reading saved: "{data_record}"')
            )

    def handle(self, *args, **options):
        # assign on_message method for handling messages from MQTT
        self.mqtt_client.on_message = self.on_message

        # connect to MQTT broker
        self.mqtt_client.connect(self.MQTT_ADDR, self.MQTT_PORT, keepalive=60)

        # Subscribe to topic "uos/cet235-0Marti0/data/value"
        self.mqtt_client.subscribe(self.MQTT_TOPIC_5)

        # start threaded client
        self.mqtt_client.loop_start()

        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            print("handled in except clause")
            self.mqtt_client.loop_stop()
