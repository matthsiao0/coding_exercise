import paho.mqtt.publish as publish

publish.single("paho/test/topic", b'{"name": "test"}', hostname="mqtt-broker")