import pygame
import sys
pygame.init()
width = 750
height = 400
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))
game_over = False
game_close = False
display= pygame.display.set_mode((width,height))
pygame.display.set_caption('Minesweeper')
clock=pygame.time.Clock()
block=pygame.image.load("./img/empty.png")
block=pygame.transform.scale(block,(25,25))
block1=pygame.image.load("./img/one.png")
block1=pygame.transform.scale(block1,(25,25))
block2=pygame.image.load("./img/two.png")
block2=pygame.transform.scale(block2,(25,25))
block3=pygame.image.load("./img/three.png")
block3=pygame.transform.scale(block3,(25,25))
block4=pygame.image.load("./img/four.png")
block4=pygame.transform.scale(block4,(25,25))
block5=pygame.image.load("./img/five.png")
block6=pygame.image.load("./img/six.png")
block7=pygame.image.load("./img/seven.png")
block8=pygame.image.load("./img/eight.png")
block9=pygame.image.load("./img/mine.png")
block9=pygame.transform.scale(block9,(25,25))
block10=pygame.image.load("./img/blockk.png")
block10=pygame.transform.scale(block10,(25,25))
# создаем группу спрайтов для всех блоков на экране

class Zero:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block,(self.x,self.y))
class One:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block1,(self.x,self.y))        
class Two:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block2,(self.x,self.y))
class Three:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block3,(self.x,self.y))
class Four:
    def __init__(self,x,y):
           
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block4,(self.x,self.y)) 
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()  
        
        self.image = block10
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
        #self.image = pygame.Surface([x, y])
        #self.rect = self.image.get_rect()
        
        
    def draw(self):
        display.blit(block10,(self.rect.x,self.rect.y))  
class Mine:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block9,(self.x,self.y))                         
class Five:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block,(self.x,self.y)) 
class Six:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block,(self.x,self.y))
class Seven:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block,(self.x,self.y))        
class Eight:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        display.blit(block,(self.x,self.y)) 
B=Block()              
all_blocks = pygame.sprite.Group()

all_blocks.add(B)  
       
while not game_over:
    #Циклически просматривает все происходящие события
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            
            if event.button == 1:
                m_pos = pygame.mouse.get_pos()
                
            
            # проверяем, находится ли на этом месте какой-нибудь блок
                block_hit_list = [b for b in all_blocks if b.rect.collidepoint(m_pos)]
            
                # если есть хотя бы один блок, удаляем его
                if len(block_hit_list) > 0:
                    block = block_hit_list[0]
                    block.kill()
            # что-то выполняется при нажатии левой кнопки мыши
                print("Левая кнопка мыши нажата")
            
    
    file = open(f'./img/{11}.txt', 'r').readlines()
    walls = []
    for i , line in enumerate(file):
        for j , each in enumerate(line):
            if each == '1':
                walls.append(Zero(j*25, i*25))
            if each == '2':
                walls.append(Two(j*25, i*25))
            if each == '3':
                walls.append(Three(j*25, i*25))
            if each == '4':
                walls.append(Four(j*25, i*25))           
            if each == '-':
                walls.append(Zero(j*25, i*25))      
            if each == '+':
                walls.append(Mine(j*25, i*25))
                
    for i , line in enumerate(file):
        for j , each in enumerate(line):                  
            if each =='1' or each == '2' or each == '3' or each == '4' or each == '-' or each == '+':
                walls.append(Block(j*25, i*25))
                
    for wall in walls:
        wall.draw()
    # очищаем экран и отрисовываем все блоки
    #display.fill((255, 255, 255))
    all_blocks.draw(display)
    # обновляем экран
    pygame.display.flip()

pygame.quit()
quit()            