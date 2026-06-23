import pygame
import random

class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = random.randint(0, 760)
        self.y = -40
        self.speed = random.randint(3, 7)

        #  imagem do inimigo
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
