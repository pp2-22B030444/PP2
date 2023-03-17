import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
x = 50
y = 50
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((255, 255, 255))
        color = red = (255, 0, 0)
        pygame.draw.circle(screen, color,(x,y),25)  
        pygame.display.flip()
        clock.tick(20)