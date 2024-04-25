from paho.mqtt import client as mqtt_client

from Application.Services.Events.SaveEventService import SaveEventService
from Domain.Interfaces.Services.PubSub.IPubSubService import IPubSubService


class ClientMqtt(IPubSubService):
    SaveEventService = SaveEventService()
    TopicToPublish = "VehiKey/Subscribe"
    TopicToSubscribe = "VehiKey/Publish/#"
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
            serialNumber = msg.topic.split("/")[-1]
            self.SaveEventService.SaveEvent(msg.payload.decode(), serialNumber)

        client.subscribe(self.TopicToSubscribe)
        client.on_message = on_message

    def Publish(self, message: str, topic_suffix: str):
        topicToPublishJoined = f"{self.TopicToPublish}/{topic_suffix}"
        result = self.Client.publish(topicToPublishJoined, message)
        status = result[0]
        if status == 0:
            print(f"Send {message} to topic `{topicToPublishJoined}`")
        else:
            print(f"Failed to send message to topic {topicToPublishJoined}")

    def Start(self):
        print('Starting MQTT...')
        self.Client = self.ConnectMqtt()
        self.Client.loop_start()
        self.Subscribe(self.Client)


clientPubSub = ClientMqtt()
