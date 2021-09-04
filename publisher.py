import random
import time

from paho.mqtt import client as mqtt_client
from getmac import get_mac_address as gma

# IP Address of the MQTT Broker
broker = '192.168.29.156'
# Port of the MQTT Broker
port = 1883

# generate client ID with pub prefix randomly

# Client ID
client_id = f'publisher@massive-dynamics-in'

# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish_message(client, topic, message):
    result = client.publish(topic, message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Sent `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def one_time_publish_message(topic, message):
    client = connect_mqtt()
    publish_message(client, topic, message)

def publish(topic, client):
    msg_count = 0
    while True:
        time.sleep(5)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

# Receiver ID
receiver_id = 'subscriber@massive-dynamics-in'
message = 'Hello World'
one_time_publish_message(receiver_id, message)

# def run():
#     client = connect_mqtt()
#     client.loop_start()
#     publish("python/mqtt", client)


# if __name__ == '__main__':
#     run()