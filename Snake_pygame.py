import pygame
import random
pygame.init()

#Osnovne nastavitve
window_height = 800
window_width = 800

canvas = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Snake pygame')
exit = False

#Deli telesa, jabolko
#glava = pygame.Rect(400, 300, 25, 25)
#telo = pygame.Rect()
#jabolko = pygame.Rect(random.randint(50, 750), random.randint(50, 550), 13, 13)

#Spremenljivke
barve = [(0, 0, 0),(0, 128, 0), (210, 4, 45), (150, 75, 0), (92, 64, 51), (34, 139, 34)]
block_size = 32
clock = pygame.time.Clock()
FPS = 10

#Mreza ekrana
def draw_grid(block_size):
    for x in range(block_size, window_width, block_size):
        pygame.draw.line(canvas, barve[4], (x, 0), (x, window_height))
    for y in range(block_size, window_height, block_size):
        pygame.draw.line(canvas, barve[4], (0, y), (window_height, y))

#Risanje kace
class Kaca:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.image = pygame.Surface((block_size, block_size))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

        self.hitrost = 1
        self.dx = self.hitrost
        self.dy = 0

    def update(self):
        self.image.fill(self.color)

        self.rect.x = self.x * block_size
        self.rect.y = self.y * block_size

        canvas.blit(self.image, self.rect)

    def premik(self):
        self.x += self.dx
        self.y += self.dy

kaca = Kaca(0, 0, barve[5])

#Glavna zanka
while not exit:
    canvas.fill(barve[3])
    draw_grid(block_size)

    kaca.update()
    kaca.premik()

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                kaca.dx = kaca.hitrost
                kaca.dy = 0

            elif event.key == pygame.K_a:
                kaca.dx = -kaca.hitrost
                kaca.dy = 0

            elif event.key == pygame.K_w:
                kaca.dx = 0
                kaca.dy = -kaca.hitrost

            elif event.key == pygame.K_s:
                kaca.dx = 0
                kaca.dy = kaca.hitrost

    pygame.display.update()