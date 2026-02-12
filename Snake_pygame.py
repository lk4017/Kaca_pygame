import pygame
import random
pygame.init()

#Osnovne nastavitve
window_height = 800
window_width = 800

canvas = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Snake_pygame')
exit = False

#Deli telesa, jabolko
glava = pygame.Rect(400, 300, 25, 25)
#telo = pygame.Rect()
jabolko = pygame.Rect(random.randint(50, 750), random.randint(50, 550), 13, 13)

#Spremenljivke
barve = [(0, 0, 0),(0, 128, 0), (210, 4, 45), (150, 75, 0), (92, 64, 51)]
hitrost = (5, 0)
block_size = 32
clock = pygame.time.Clock()

#Mreza ekrana
def draw_grid(block_size):
    for x in range(block_size, window_width, block_size):
        pygame.draw.line(canvas, barve[4], (x, 0), (x, window_height))
    for y in range(block_size, window_height, block_size):
        pygame.draw.line(canvas, barve[4], (0, y), (window_height, y))

#Glavna zanka
while not exit:
    canvas.fill(barve[3])
    draw_grid(block_size)
    clock.tick(20)
    #casova_razlika = clock.tick(60)/100

    glava.x += hitrost[0]
    glava.y += hitrost[1]

    pygame.draw.rect(canvas, barve[2], jabolko)
    pygame.draw.rect(canvas, barve[0] , glava)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                hitrost = (5, 0)

            if event.key == pygame.K_a:
                hitrost = (-5, 0)

            if event.key == pygame.K_w:
                hitrost = (0, -5)

            if event.key == pygame.K_s:
                hitrost = (0, 5)

#poglej kko ima ucitelj narejeno
    pygame.display.update()