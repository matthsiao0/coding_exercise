import paho.mqtt.subscribe as subscribe
import json

msg = subscribe.simple("paho/test/topic", hostname="mqtt-broker")
print(f'{msg.topic}, {json.loads(msg.payload)}')