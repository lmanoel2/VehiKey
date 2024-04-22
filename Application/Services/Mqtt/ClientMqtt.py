from paho.mqtt import client as mqtt_client

from Domain.Interfaces.Services.PubSub.IPubSubService import IPubSubService


class ClientMqtt(IPubSubService):
    TopicToPublish = "VehiKey/Subscribe"
    TopicToSubscribe = "VehiKey/Publish"
    Broker = 'broker.emqx.io'
    Port = 1883
    ClientId = 'python-mqtt-23123123122'

    def ConnectMqtt(self):
        def onConnect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, self.ClientId)

        client.on_connect = onConnect
        client.connect(self.Broker, self.Port)
        return client

    def Subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        client.subscribe(self.TopicToSubscribe)
        client.on_message = on_message

    def Publish(self, message: str):
        result = self.Client.publish(self.TopicToPublish, message)
        status = result[0]
        if status == 0:
            print(f"Send {message} to topic `{self.TopicToPublish}`")
        else:
            print(f"Failed to send message to topic {self.TopicToPublish}")

    def Start(self):
        print('Starting MQTT...')
        self.Client = self.ConnectMqtt()
        self.Client.loop_start()
        self.Subscribe(self.Client)


clientPubSub = ClientMqtt()
