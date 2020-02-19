# -*- coding: utf-8 -*-
# testar com vetor midi instrumento
# fazer função global para tocar midi
# testar verificando o cliente ip
# player[i].note_on
#
# mqtt
# thread python
# aconnect
# modprobe

import socket
import paho.mqtt.client as mqtt
import pygame
import pygame.midi
import serial, time

time.sleep(1)
pygame.init()

pygame.midi.init()

print(pygame.midi.get_default_output_id())
print(pygame.midi.get_device_info(0))

print('Setup alsa server...')

display_width = 600
display_height = 400

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('----- CongAr -----')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()

congImg = pygame.image.load('img/conga_0.png')
maod2Img = pygame.image.load('img/mao_direita2.png')
maodImg = pygame.image.load('img/mao_direita1.png')
maoeImg = pygame.image.load('img/mao_esquerda1.png')
maoe2Img = pygame.image.load('img/mao_esquerda2.png')
maosImg = pygame.image.load('img/maos.png')
maos2Img = pygame.image.load('img/maos2.png')
maosaltImg = pygame.image.load('img/maosalt.png')
maosalt2Img = pygame.image.load('img/maosalt2.png')


def cong(x, y):
    gameDisplay.blit(congImg, (x, y))


def maoD2(x, y):
    gameDisplay.blit(maod2Img, (x, y))


def maoD(x, y):
    gameDisplay.blit(maodImg, (x, y))


def maoE(x, y):
    gameDisplay.blit(maoeImg, (x, y))


def maoE2(x, y):
    gameDisplay.blit(maoe2Img, (x, y))


def maos(x, y):
    gameDisplay.blit(maosImg, (x, y))


def maos2(x, y):
    gameDisplay.blit(maos2Img, (x, y))


def maosalt(x, y):
    gameDisplay.blit(maosaltImg, (x, y))


def maosalt2(x, y):
    gameDisplay.blit(maosalt2Img, (x, y))


def on_connect(client, userdata, flags, rc):
    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("tempmonitor")


# Callback responável por receber uma mensagem publicada no tópico acima
def on_message(client, userdata, msg):
    #print(str(msg.payload))
    x = (display_width * 0.30)
    y = (display_height * 0.45)

    while True:
        msg = msg.payload
        data = msg
        sensors_dt = data

        # array que retira os 'espacos' da variavel 'data'
        sensors_dt = map(float, sensors_dt.split(' '))
        id = int(sensors_dt[0] + 3)
        print(id, sensors_dt[1], sensors_dt[2])
        player1 = pygame.midi.Output(id)
        player1.set_instrument(0)

        if sensors_dt[1] >= 10.0 and sensors_dt[1] <= 20.0 and sensors_dt[
                2] > 20.0:
            maoD2(x, y)
            print("Sensor maior 1")
            player1.note_on(60, 127, 1)
            player1.note_off(60, 127, 1)
            pygame.display.update()

        if sensors_dt[1] >= 5.0 and sensors_dt[1] <= 9.0 and sensors_dt[
                2] > 20.0:
            maoD(x, y)
            print("Sensor menor 1")
            player1.note_on(61, 127, 1)
            player1.note_off(61, 127, 1)
            pygame.display.update()

        if sensors_dt[2] >= 10.0 and sensors_dt[2] <= 20.0 and sensors_dt[
                1] > 20.0:
            maoE2(x, y)
            print("Sensor maior 2 audio")
            player1.note_on(62, 127, 1)
            player1.note_off(62, 127, 1)
            pygame.display.update()

        if sensors_dt[2] >= 5.0 and sensors_dt[2] <= 9.0 and sensors_dt[
                1] > 20.0:
            maoE(x, y)
            print("Sensor menor 2")
            player1.note_on(63, 127, 1)
            player1.note_off(63, 127, 1)
            pygame.display.update()

        if sensors_dt[1] >= 10.0 and sensors_dt[1] <= 20.0 and sensors_dt[
                2] >= 10.0 and sensors_dt[2] <= 20.0:
            maos(x, y)
            print("Sensor maior 1 + Sensor maior 2")
            player1.note_on(64, 127, 1)
            player1.note_off(64, 127, 1)
            pygame.display.update()

        if sensors_dt[1] >= 5.0 and sensors_dt[1] <= 9.0 and sensors_dt[
                2] >= 5.0 and sensors_dt[2] <= 9.0:
            maos2(x, y)
            print("Sensor menor 1 + Sensor menor 2")
            player1.note_on(65, 127, 1)
            player1.note_off(65, 127, 1)
            pygame.display.update()

        if sensors_dt[1] >= 5.0 and sensors_dt[1] <= 9.0 and sensors_dt[
                2] >= 10.0 and sensors_dt[2] <= 20.0:
            maosalt(x, y)
            print("Sensor menor 1 + Sensor maior 2")
            player1.note_on(66, 127, 1)
            player1.note_off(66, 127, 1)
            pygame.display.update()

        if sensors_dt[1] >= 10.0 and sensors_dt[1] <= 20.0 and sensors_dt[
                2] >= 5.0 and sensors_dt[2] <= 9.0:
            maosalt2(x, y)
            print("Sensor maior 1 + Sensor menor 2")
            player1.note_on(67, 127, 1)
            player1.note_off(67, 127, 1)
            pygame.display.update()

        white = (y % 255, 255, x % 255)  #atualiza de cor de fundo

        gameDisplay.fill(white)

        clock.tick(60)
        cong(x, y)
        pygame.display.update()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Seta um usuário e senha para o Broker, se não tem, não use esta linha
#client.username_pw_set("USUARIO", password="SENHA")
# Conecta no MQTT Broker, no meu caso, o Mosquitto
client.connect("mqtt.eclipse.org", 1883, 60)
# Inicia o loop
client.loop_forever()

pygame.quit()

quit()
