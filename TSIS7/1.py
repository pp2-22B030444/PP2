import pygame
pygame.init()
monitor=pygame.display.set_mode((600,400))
pygame.display.set_caption("PP2_Pygame")
pygame.display.set_icon(pygame.image.load("icon.png"))

check=True
square=pygame.Surface((200,200))
font=pygame.font.Font('font.ttf',25)
text=font.render('Pp2_Pygame',False,'Red')
image=pygame.image.load("./img/food.png")
#background=pygame.image.load("im.webp")
sound=pygame.mixer.Sound('music.mp3')
sound.play()
while check:
    monitor.fill((5,150,50))
    pygame.draw.circle(monitor,'Black',(300,200),40,5)
    #monitor.blit(square,(100,50))
    monitor.blit(text,(60,90))
    monitor.blit(image,(120,50))
    #monitor.blit(background,(100,60))
    pygame.display.update()
    for action in pygame.event.get():
        if action.type==pygame.QUIT:
            check=False
            pygame.quit()
