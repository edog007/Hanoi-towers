import pygame
pygame.init()

import random

screen = pygame.display.set_mode((1500, 600))


class Pole:
    def __init__(self, x, name):
        self.discs = []
        self.x = x
        self.name = name

    def add_disc(self, size, red, green, blue):
        self.discs.append(Disc(width=size*40, x=self.x - size * 20, y=len(self.discs) * -40 + 500,
                               color=(red, green, blue)))

    def move_disc_to(self, target):
        disc = self.discs.pop()
        target.add_disc(disc.width/40, disc.color[0], disc.color[1], disc.color[2])

    def draw(self):
        for d in self.discs:
            d.draw()


class Disc:
    def __init__(self, width, x, y, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = 40
        self.color = color
        self.rec = pygame.rect.Rect((self.x, self.y), (self.width, self.height))

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rec)


def main(n):
    a = Pole(250, 'a')
    b = Pole(750, 'b')
    c = Pole(1250, 'c')

    for i in range(n, 0, -1):
         a.add_disc(i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill((0, 0, 0))

    hanoi(n, a, b, c)

    pygame.display.update()


def hanoi(n, source, via, target):
    # print(n, source.name, via.name, target.name)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    if n > 0:
        hanoi(n - 1, source, target, via)
        # print(n, source.name, "->", target.name)
        source.move_disc_to(target)
        pygame.display.update()
        screen.fill((0, 0, 0))

        source.draw()
        via.draw()
        target.draw()

        pygame.time.wait(500)
        hanoi(n - 1, via, source, target)



main(5)

