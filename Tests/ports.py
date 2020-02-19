import sys, pygame, pygame.midi

# set up pygame
pygame.init()
pygame.midi.init()

# list all midi devices
for x in range(0, pygame.midi.get_count()):
    print pygame.midi.get_default_output_id(x)
