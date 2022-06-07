import paho.mqtt.client as mqtt
import time

broker = "127.0.0.1"
port = 1883

username = "user"
password = "password"

client = mqtt.Client("test-publisher")
client.username_pw_set(username, password)
client.connect(broker, port)

while True:

  client.publish("test","testing testing 123")
  time.sleep(1)
