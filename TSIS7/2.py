import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
#is_red = True
x = 50
y = 50
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        #is_red = not is_red        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((255, 255, 255))
        #if is_red: 
        color = red = (255, 0, 0)
        #else: color = (255, 100, 0)
        pygame.draw.circle(screen, color,(x,y),25)  
        #pygame.draw.circle(screen, color,[250, 250], 50,) 
        pygame.display.flip()
        clock.tick(20)