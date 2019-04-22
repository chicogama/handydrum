#

# sudo python handydrum-03-esp-mega 

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



import pygame

import serial, time 



arduino = serial.Serial( '/dev/ttyACM0', 115200 )



#give the connection a second to settle

time.sleep(1) 

pygame.init()



display_width = 600

display_height = 400



gameDisplay = pygame.display.set_mode( (display_width, display_height) )

pygame.display.set_caption('----- Conga -----')



black = (0,0,0)

white = (255,255,255)



clock = pygame.time.Clock()

congAr_1_1_close = pygame.mixer.Sound("congAr_1_1_close.ogg")

congAr_2_1_close = pygame.mixer.Sound("congAr_2_1_close.ogg")

congAr_1_2_open = pygame.mixer.Sound("congAr_1_2_open.ogg")

congAr_2_2_open = pygame.mixer.Sound("congAr_2_2_open.ogg")



congImg = pygame.image.load('conga_0.png')

maod2Img = pygame.image.load('mao_direita2.png')

maodImg = pygame.image.load('mao_direita1.png')

maoeImg = pygame.image.load('mao_esquerda1.png')

maoe2Img = pygame.image.load('mao_esquerda2.png')

maosImg = pygame.image.load('maos.png')

maos2Img = pygame.image.load('maos2.png')

maosaltImg = pygame.image.load('maosalt.png')

maosalt2Img = pygame.image.load('maosalt2.png')

def cong( x, y ):
	gameDisplay.blit( congImg, (x,y) )

def maoD2( x, y ):
	gameDisplay.blit( maod2Img, (x,y) )

def maoD( x, y ):
	gameDisplay.blit( maodImg, (x,y) )

def maoE( x, y ):
	gameDisplay.blit( maoeImg, (x,y) )

def maoE2( x, y ):
	gameDisplay.blit( maoe2Img, (x,y) )

def maos( x, y ):
	gameDisplay.blit( maosImg, (x,y) )

def maos2( x, y ):
	gameDisplay.blit( maos2Img, (x,y) )

def maosalt( x, y ):
	gameDisplay.blit( maosaltImg, (x,y) )

def maosalt2( x, y ):
	gameDisplay.blit( maosalt2Img, (x,y) )



def loop():

	x =  (display_width * 0.30)

	y = (display_height * 0.45)

	car_width = 10	#quantidade de pixels horizontais

	car_height = 90

	crashed = False

	while not crashed:


		# recebe valor de distancia dos sensores no formato: 10.01 9.288
	
		data = arduino.readline()
		 
		print( data )
		
		sensors_dt = data
			
			 
		# array que retira os 'espacos' da variavel 'data' 
		
		sensors_dt = map(float, sensors_dt.split(' ') )
		
	
		if sensors_dt[0] >= 10.0 and sensors_dt[0] <= 20.0 and sensors_dt[1] < 5.0 :
			print("Sensor maior 1")
			maoD2(x,y)
			congAr_1_2_open.play()   
			pygame.display.update()
			time.sleep(1)


		if sensors_dt[0] >= 5.0 and sensors_dt[0] <= 9.0 and sensors_dt[1] < 5.0:
			print("Sensor menor 1")
			maoD(x,y)
			congAr_1_1_close.play()   
			pygame.display.update()
			time.sleep(1)


		if sensors_dt[1] >= 10.0 and sensors_dt[1] <= 20.0 and sensors_dt[0] < 5.0:
			print("Sensor maior 2 audio")
			maoE2(x,y)
			congAr_1_2_open.play() 
			pygame.display.update()  
			time.sleep(1)
		

		if sensors_dt[1] >= 5.0 and sensors_dt[1] <= 9.0 and sensors_dt[0] < 5.0 :
			print("Sensor menor 2")
			maoE(x,y)
			congAr_2_1_close.play()
			pygame.display.update()   
			time.sleep(1)

		if sensors_dt[0] >= 10.0 and sensors_dt[0] <= 20.0 and sensors_dt[1] >= 10.0 and sensors_dt[1] <= 20.0 :
			print("Sensor maior 1 + Sensor maior 2")
			maos(x,y)	
			congAr_1_2_open.play()
			congAr_1_2_open.play()
			pygame.display.update()   
			time.sleep(1)

		if sensors_dt[0] >= 5.0 and sensors_dt[0] <= 9.0 and sensors_dt[1] >= 5.0 and sensors_dt[1] <= 9.0:
			print("Sensor menor 1 + Sensor menor 2")
			maos2(x,y)
			congAr_1_1_close.play()
			congAr_2_1_close.play()	
			pygame.display.update()   
			time.sleep(1)

		if sensors_dt[0] >= 5.0 and sensors_dt[0] <= 9.0 and sensors_dt[1] >= 10.0 and sensors_dt[1] <= 20.0:
			print("Sensor menor 1 + Sensor maior 2")
			maosalt(x,y)
			congAr_1_1_close.play()
			congAr_1_2_open.play()	
			pygame.display.update()   
			time.sleep(1)

		if sensors_dt[0] >= 10.0 and sensors_dt[0] <= 20.0 and sensors_dt[1] >= 5.0 and sensors_dt[1] <= 9.0:
			print("Sensor maior 1 + Sensor menor 2")
			maosalt2(x,y)
			congAr_1_2_open.play()
			congAr_2_1_close.play()                    	
			pygame.display.update()   
			time.sleep(1)

		
		
		crashed = False
		

			    ##########################

		white = (y%255,255,x%255) #atualiza de cor de fundo

		gameDisplay.fill(white)
		
		clock.tick(60)
		
		cong(x,y)
		pygame.display.update()




loop()

pygame.quit()

quit()


