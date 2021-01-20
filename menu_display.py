import pygame
from pygame.locals import *
import screeninfo

screen_id = 0
screen = screeninfo.get_monitors()[screen_id]
W, H = screen.width, screen.height

print('width', W)
print('height', H)


pygame.init()
WIDTH = W
HEIGHT = H
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
img = pygame.image.load("imgs/5.png")
while True:
        events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        windowSurface.blit(img, (0, 0)) #Replace (0, 0) with desired coordinates
        pygame.display.flip()
