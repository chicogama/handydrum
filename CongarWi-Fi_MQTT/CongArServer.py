# -*- coding: utf-8 -*-
# Para instalar o paho-mqtt use o comando pip install paho-mqtt
import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("tempmonitor")


# Callback responável por receber uma mensagem publicada no tópico acima
def on_message(client, userdata, msg):
    print(str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Seta um usuário e senha para o Broker, se não tem, não use esta linha
#client.username_pw_set("USUARIO", password="SENHA")
# Conecta no MQTT Broker, no meu caso, o Mosquitto
client.connect("mqtt.eclipse.org", 1883, 60)
# Inicia o loop
client.loop_forever()
