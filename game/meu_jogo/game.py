import pygame
from player import Player
from enemy import Enemy
from menu import Menu
import time

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Dodge Survival")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("assets/bg_game.jpg")
        self.background = pygame.transform.scale(self.background, (800, 600))

    def run(self):
        menu = Menu(self.screen)
        if not menu.run():
            pygame.quit()
            return

        player = Player()
        enemies = []

        spawn_timer = 0
        start_time = time.time()
        game_over = False
        win = False

        while True:
            self.screen.blit(self.background, (0, 0))

            if not game_over:
                elapsed_time = time.time() - start_time

                # Condição de vitória (30 segundos)
                if elapsed_time >= 30:
                    win = True
                    game_over = True

                keys = pygame.key.get_pressed()
                player.move(keys)

                # Spawn de inimigos
                spawn_timer += 1
                if spawn_timer > 30:
                    enemies.append(Enemy())
                    spawn_timer = 0

                # Atualizar inimigos
                for enemy in enemies:
                    enemy.update()

                    # Colisão → derrota
                    if player.rect.colliderect(enemy.rect):
                        game_over = True

                # Desenhar
                player.draw(self.screen)
                for enemy in enemies:
                    enemy.draw(self.screen)

                # Score (tempo)
                font = pygame.font.SysFont(None, 30)
                score_text = font.render(f"Tempo: {int(elapsed_time)}s", True, (255,255,255))
                self.screen.blit(score_text, (10, 10))

            else:
                font = pygame.font.SysFont(None, 50)
                if win:
                    text = font.render("VOCÊ VENCEU!", True, (0, 255, 0))
                else:
                    text = font.render("GAME OVER", True, (255, 0, 0))

                self.screen.blit(text, (250, 250))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.clock.tick(60)
