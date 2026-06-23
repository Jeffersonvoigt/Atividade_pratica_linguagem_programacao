import pygame

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 375
        self.y = 500
        self.speed = 5

        #  imagem do player
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
