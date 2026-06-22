
import pygame

print('setup Start')
pygame.init()
window = pygame.display.set_mode(size=(640, 480))
print('Setup End')

print('Loop Start')
while True:
    # check for all events (verificar todos os eventos)
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            print('Quitting...')
            pygame.quit() # Close window (fechar janela)
            quit() # end pygame (fim)
