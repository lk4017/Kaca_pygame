import pygame
import random
pygame.init()

#Osnovne nastavitve
window_height = 400
window_width = 400

canvas = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Snake pygame')
exit = False

#Barve
barve = [(0, 0, 0),
         #Crna,
         (0, 128, 0),
         #Zelena,
         (210, 4, 45),
         #Rdeca,
         (150, 75, 0),
         #Rjava,
         (92, 64, 51),
         #Temno rjava,
         (34, 139, 34),
         #Temno zelena
         ]

#Spremenljivke
block_size = 25
barva_kace = (34, 139, 34)
clock = pygame.time.Clock()
FPS = 30
odziv = 150
zadnji_premik = pygame.time.get_ticks()
velikost_jabolka = 15
jabolko_pos = (random.randint(0, window_width // block_size -1 ),
               random.randint(0, window_height // block_size -1))
odmik =  (block_size - velikost_jabolka) // 2
Konec_igre = False

#Mreza ekrana
def draw_grid(block_size):
    for x in range(block_size, window_width, block_size):
        pygame.draw.line(canvas, barve[4], (x, 0), (x, window_height))
    for y in range(block_size, window_height, block_size):
        pygame.draw.line(canvas, barve[4], (0, y), (window_width, y))

#Risanje kace
class Kaca:
    def __init__(self, x, y, color):
        self.body = [(x, y)]
        self.color = color
        self.image = pygame.Surface((block_size, block_size))
        self.grow = False

        self.hitrost = 1
        self.dx = self.hitrost
        self.dy = 0

    def update(self):
        for part in self.body:
            rect = pygame.Rect(part[0] * block_size, part[1] * block_size, block_size, block_size)
            pygame.draw.rect(canvas, self.color, rect)

    def premik(self):
        glava_x, glava_y = self.body[0]
        nova_glava = (glava_x + self.dx, glava_y + self.dy)

        if (nova_glava[0] < 0 or
            nova_glava[0] >= window_width // block_size or
            nova_glava[1] < 0 or
            nova_glava[1] >= window_height // block_size or
            nova_glava in self.body
        ):
            return "Konec_igre"

        self.body.insert(0, nova_glava)

        if self.grow == False:
            self.body.pop()
        else:
            self.grow = False

    def sprememba_barve(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

kaca = Kaca(0, 0, barva_kace)

#Glavna zanka
while not exit:
    canvas.fill(barve[3])
    draw_grid(block_size)
    jabolko = pygame.Rect(jabolko_pos[0] * block_size + odmik, jabolko_pos[1] * block_size + odmik, velikost_jabolka, velikost_jabolka)
    pygame.draw.rect(canvas, barve[2], jabolko)
    kaca.update()
    clock.tick(FPS)

    trenutni_cas = pygame.time.get_ticks() #mora biti tu notri, da ima ves cas izvajanja glavne zanke sedanji cas

    if trenutni_cas - zadnji_premik > odziv:
        rezultat = kaca.premik()
        if rezultat == "Konec_igre":
            Konec_igre = True

        zadnji_premik = trenutni_cas

    if Konec_igre:
        exit = True

    if kaca.body[0] == jabolko_pos:
        kaca.grow = True
        jabolko_pos = (random.randint(0, window_width // block_size -1 ),
                       random.randint(0, window_height // block_size -1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and kaca.dx == 0:
                kaca.dx = kaca.hitrost
                kaca.dy = 0

            elif event.key == pygame.K_a and kaca.dx == 0:
                kaca.dx = -kaca.hitrost
                kaca.dy = 0

            elif event.key == pygame.K_w and kaca.dy == 0:
                kaca.dx = 0
                kaca.dy = -kaca.hitrost

            elif event.key == pygame.K_s and kaca.dy == 0:
                kaca.dx = 0
                kaca.dy = kaca.hitrost

            elif event.key == pygame.K_SPACE:
                kaca.sprememba_barve()



    pygame.display.update()

pygame.quit()