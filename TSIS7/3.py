import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 0))
pygame.display.flip()
#pygame.draw.circle(screen,'Black',(300,200),40)
running = True
while running:
    pygame.draw.circle(screen,'Green',(300,200),40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()