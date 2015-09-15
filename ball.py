import pygame
import random
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
	def __init__(self,r,color,disp):
		pygame.sprite.Sprite.__init__(self)
		self.radius = r
		self.color = color
		x=random.randrange(0,800)
		y=random.randrange(0,600)
		pygame.draw.circle(disp,self.color,(x,y),self.radius,0)		