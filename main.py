import pygame
import time
import sys
from pygame.locals import *
from ball import Ball

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
pygame.display.set_caption('Agar')
swidth=800
sheight=600
clock = pygame.time.Clock()
disp=pygame.display.set_mode([swidth,sheight],0,32)
disp.fill(WHITE)
for i in range(2):
	b=Ball(4,BLACK,disp)
while True:
	for event in pygame.event.get() : 
				if event.type == QUIT :
					pygame.quit()
					sys.exit()
	pygame.display.update()