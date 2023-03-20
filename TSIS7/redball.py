import pygame

pygame.init()
screen = pygame.display.set_mode((390, 390))
done = False
x = 25
y = 25
clock = pygame.time.Clock()

while not done:
        screen.fill((255, 255, 255))
        color = red = (255, 0, 0)
        pygame.draw.circle(screen, color,(x,y),25)  
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
                if y>25:
                        y -= 20
        if pressed[pygame.K_DOWN]:
                if y<365:
                        y += 20
        if pressed[pygame.K_LEFT]: 
                if x>25:
                        x -= 20
        if pressed[pygame.K_RIGHT]:                 
                if x<365:
                        x += 20
        
        pygame.display.flip()
        clock.tick(20)