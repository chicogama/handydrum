"""
    # sudo python testeGame1.1-esp.py
    #
    # movimentacao de imagens
    # python 2
    # sudo apt-get install python-pygame
    #
    # python3
    # sudo apt-get install python3-setuptools
    # sudo easy_install3 pip
    # sudo pip3.5 install pygame
    # install:  python -m pip install pyserial
    #
    @author: claudiorogerio, josemar, joelden

    TO DO:
        Documentacao
        Split arquivos
        Midi local                                      OK
        Midi via ethernet por arduinos
            Comunicacao ethernet
            Enviar dados ethernet
            Enviar dados midi ethernet
            Configurar servidor de dados midi
"""

import pygame
import pygame.midi
import serial, time

##arduino = serial.Serial( '/dev/ttyUSB0', 9600 )

#give the connection a second to settle
time.sleep(1)

pygame.init()
# setup midi
pygame.midi.init()

print pygame.midi.get_default_output_id()
print pygame.midi.get_device_info(0)

player1 = pygame.midi.Output(0)

player1.set_instrument(0)

print 'Setup alsa server...'

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('----- CongAr -----')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

carImg = pygame.image.load('bola.jpg')


def car(x,y):
    gameDisplay.blit( carImg, (x, y) )


def loop():
    x =  (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0 #mudanca horizontal
    y_change = 0 #mudanca vertical
    car_speed = 0 #velocidade
    car_width = 73	#quantidade de pixels horizontais
    car_height = 90
    crashed = False

    while not crashed:


        # recebe valor de distancia dos sensores no formato: 10.01 9.288
        ##		data = arduino.readline()
        ##		print(data)
        ##		sensors_dt=data
        # array que retira os 'espacos' da variavel 'data'
        ##		sensors_dt = map(float, sensors_dt.split(' ') )

        ##		if sensors_dt[0] >= 10.0 and sensors_dt[0] <= 20.0 :
        ##			x_change = 5
        ##			print("Sensor maior 1")
        ##		if sensors_dt[0] >= 5.0 and sensors_dt[0] <= 9.0 :
        ##			x_change = -5
        ##			print("Sensor menor 1")

        ##		if sensors_dt[1] >= 10.0 and sensors_dt[1] <= 20.0 :
        ##			y_change = 5
        ##			print("Sensor maior 2")
        ##		if sensors_dt[1] >= 5.0 and sensors_dt[1] <= 9.0 :
        ##			y_change = -5
        ##			print("Sensor menor 2")

        #variavel de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

                ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    player1.note_on(60,127,1)
                    #time.sleep(0.5)
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    player1.note_off(60,127,1)
                elif event.key == pygame.K_UP:
                    y_change = -5
                    player1.note_on(62,127,1)
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                    player1.note_off(62,127,1)
                    #        if event.type == pygame.KEYUP:  #evita loop direcional
                    #			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #				x_change = 0
                    #			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    #				y_change = 0
                    ######################

        x += x_change
        y += y_change

        if x > display_width - car_width or x <= 0:
            x -= x_change	# n add a mudanca
        if y > display_height - car_height or y <= 0:
            y -= y_change	# n add a mudanca
            #crashed = True

                    ##
        white = (y%255,255,x%255) #atualiza de cor de fundo
        gameDisplay.fill(white)
        car(x,y)

        pygame.display.update()
        clock.tick(60)

loop()
pygame.quit()
quit()
