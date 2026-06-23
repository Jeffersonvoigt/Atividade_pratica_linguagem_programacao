import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 40)

        #  Carrega UMA vez
        self.background = pygame.image.load("assets/bg_menu.jpg")
        self.background = pygame.transform.scale(self.background, (800, 600))

    def run(self):
        while True:
            #  Desenha o fundo
            self.screen.blit(self.background, (0, 0))

            # textos
            title = self.font.render("DODGE SURVIVAL", True, (255, 0, 0))
            start = self.font.render("Pressione ENTER para jogar", True, (255, 0, 0))
            controls = self.font.render("Use as teclas: W A S D - mover", True, (255, 0, 0))

            self.screen.blit(title, (250, 150))
            self.screen.blit(start, (200, 250))
            self.screen.blit(controls, (200, 350))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
