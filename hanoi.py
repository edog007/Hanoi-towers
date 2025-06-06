import pygame
pygame.init()

import random

screen = pygame.display.set_mode((1500, 600))

def update_screen(poles, flying_disc=None):
    screen.fill((0, 0, 0))
    for pole in poles:
        pole.draw()
    if flying_disc:
        flying_disc.rec = pygame.Rect((flying_disc.x, flying_disc.y), (flying_disc.width, flying_disc.height))
        flying_disc.draw()
    pygame.display.update()
    pygame.time.wait(1)
    pygame.event.pump()


class Pole:
    def __init__(self, x, name):
        self.discs = []
        self.x = x
        self.name = name

    def add_disc(self, size, red, green, blue):
        self.discs.append(Disc(width=size*40, x=self.x - size * 20, y=len(self.discs) * -40 + 500,
                               color=(red, green, blue)))


    def move_disc_to(self, target, poles):
        step_size = 5
        disc = self.discs.pop()

        # Step 1: Move up
        while disc.y > 100:
            disc.y -= step_size
            update_screen(poles, disc)

        # Step 2: Move horizontally
        target_x = target.x - disc.width // 2
        step = step_size if disc.x < target_x else -step_size
        while abs(disc.x - target_x) > abs(step):
            disc.x += step
            update_screen(poles, disc)

        disc.x = target_x  # Align exactly

        # Step 3: Move down to correct height on target
        target_y = 500 - len(target.discs) * 40
        while disc.y < target_y:
            disc.y += step_size
            update_screen(poles, disc)
        disc.y = target_y

        # Final placement
        target.discs.append(disc)

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
    poles = [a, b, c]

    for i in range(n, 0, -1):
         a.add_disc(i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill((0, 0, 0))
    update_screen(poles)
    hanoi(n, a, b, c, poles)


def hanoi(n, source, via, target, poles):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    if n > 0:
        hanoi(n - 1, source, target, via, poles)
        source.move_disc_to(target, poles)
        hanoi(n - 1, via, source, target, poles)



main(5)

