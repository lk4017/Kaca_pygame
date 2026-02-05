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
hitrost = (3, 0)

while not exit:
    canvas.fill(color)
    clock.tick(20)
    #casova_razlika = clock.tick(60)/100

    glava.x += hitrost[0]
    glava.y += hitrost[1]


    pygame.draw.rect(canvas, barve[0] , glava)
    pygame.draw.rect(canvas, barve[2] , jabolko)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                hitrost = (3, 0)

            if event.key == pygame.K_a:
                hitrost = (-3, 0)

            if event.key == pygame.K_w:
                hitrost = (0, -3)

            if event.key == pygame.K_s:
                hitrost = (0, 3)

    pygame.display.update()