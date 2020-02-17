import socket
import pygame
import pygame.midi
import serial
import time


time.sleep(1)

time.sleep(1) 
pygame.init()

pygame.midi.init()

print(pygame.midi.get_default_output_id())