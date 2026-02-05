import pygame
import random
pygame.init()

canvas = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Snake_pygame')
exit = False

color = (150, 75, 0)

clock = pygame.time.Clock()

exit = False

glava = pygame.Rect(400, 300, 25, 25)
#telo = pygame.Rect()
jabolko = pygame.Rect(random.randint(50, 750), random.randint(50, 550), 13, 13)

barve = [(0, 0, 0),(0, 128, 0), (210, 4, 45)]

while not exit:
    canvas.fill(color)


    pygame.draw.rect(canvas, barve[0] , glava)
    pygame.draw.rect(canvas, barve[2] , jabolko)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()