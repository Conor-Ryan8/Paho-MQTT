import paho.mqtt.client as mqtt

broker = "127.0.0.1"
port = 1883

username = "user"
password = "password"

def onConnect(mqttc, obj, flags, rc):
  client.subscribe("#")
  print("Connected")
  
def onMessage(client, userdata, message):
  payload = str(message.payload.decode("utf-8"))
  topic = message.topic
  qos = message.qos
  retain = message.retain
  print(payload)


client = mqtt.Client("test-subscriber")
client.on_connect = onConnect
client.on_message = onMessage
client.username_pw_set(username, password)
client.connect(broker, port)
client.loop_forever()
