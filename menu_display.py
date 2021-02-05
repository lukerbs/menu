import pygame
from pygame.locals import *
import screeninfo
import datetime
import time

screen_id = 0
screen = screeninfo.get_monitors()[screen_id]
W, H = screen.width, screen.height

print('width', W)
print('height', H)

pygame.init()
WIDTH = W
HEIGHT = H
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

weekday_menu = ['imgs/hotdog.png', 'imgs/nacho.png', 'imgs/potato.png', 'imgs/taco.png', 'imgs/menudo.png', 'imgs/pozole.png']
friday_menu = ['imgs/hotdog.png', 'imgs/nacho.png', 'imgs/potato.png', 'imgs/taco.png', 'imgs/menudo.png', 'imgs/pozole.png', 'imgs/chowder.png']
weekend_menu = ['imgs/hotdog.png', 'imgs/nacho.png', 'imgs/potato.png', 'imgs/taco.png', 'imgs/menudo.png', 'imgs/pozole.png', 'imgs/conchas.png']

while True:
	today = datetime.datetime.today().weekday()
	# 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
	if today == 4:
		menu = friday_menu
	if today == 5 or today == 6:
		menu = weekend_menu
	else:
		menu = weekday_menu
	for i in range(len(menu)):
		img = pygame.image.load(menu[i])
		events = pygame.event.get()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		windowSurface.blit(img, (0, 0)) #Replace (0, 0) with desired coordinates
		pygame.display.flip()
		time.sleep(5)
