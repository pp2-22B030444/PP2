
#Imports
import pygame, sys
from pygame.locals import *
import random, time
# Для случайного размещения монет
from random import randint

# Для поиска ресурсов
from pathlib import Path

#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Как часто должны генерироваться монеты (мс)
coin_countdown = 2500
coin_interval = 100

# Сколько монет должно быть на экране, чтобы игра закончилась
COIN_COUNT = 10 
#Other Variables for use in the program
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("  Game Over", True, BLACK)
 
background = pygame.image.load("./img/road.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((500,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./img/carr.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./img/my.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
              
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
# Определяем спрайт для монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        """Инициализирует спрайт монеты"""
        super(Coin, self).__init__()

        # Получаем изображение монеты
        coin_image = str(Path.cwd()  / "img" / "bit.png")

        # Загружаем изображение, настраиваем альфа канал для прозрачности
        self.surf = pygame.image.load(coin_image).convert_alpha()

        # Задаем стартовую позицию, сгенерированную случайным образом
        self.rect = self.surf.get_rect(
            center=(
                randint(10, SCREEN_WIDTH - 10),
                randint(10, SCREEN_HEIGHT - 10),
            )
        )       

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
# Создаем событие для добавления монеты
ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, coin_countdown)

# Настраиваем список монет
coin_list = pygame.sprite.Group()

# Инициализируем счет
score = 0

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Определяем, нужно ли добавлять новую монету
        elif event.type == ADDCOIN:
            # Добавляем новую монету
            new_coin = Coin()
            coin_list.add(new_coin)

            # Ускоряем игру, если на экранее менее 3 монет
            if len(coin_list) < 3:
                coin_countdown -= coin_interval
            # Ограничиваем скорость
            if coin_countdown < 100:
                coin_countdown = 100

            # Останавливаем предыдущий таймер
            pygame.time.set_timer(ADDCOIN, 0)

            # Запускаем новый таймер
            pygame.time.set_timer(ADDCOIN, coin_countdown)
    # Обновляем позицию персонажа
    P1.update(pygame.mouse.get_pos())
          

    # Проверяем, столкнулся ли игрок с монетой и удаляем, если это так
    coins_collected = pygame.sprite.spritecollide(
        sprite=P1, group=coin_list, dokill=True
    )
    for coin in coins_collected:
        # Каждая монета стоит 10 очков
        score += 10
        # Воспроизводим звук для монеты
        #coin_pickup_sound.play()

    # Проверяем, не слишком ли много монет
    if len(coin_list) >= COIN_COUNT:
        # Если монет много, останавливаем игру
        running = False

    # Рисуем следующие монеты
    for coin in coin_list:
        DISPLAYSURF.blit(coin.surf, coin.rect)

    # Отрисовываем персонажа
    DISPLAYSURF.blit(P1.image, P1.rect)

    # Выводим текущий счет
    score_font = pygame.font.SysFont("any_font", 36)
    score_block = score_font.render(f"Score: {score}", False, (0, 0, 0))
    DISPLAYSURF.blit(score_block, (50, SCREEN_HEIGHT - 50))

    # Отображаем всё на экране
    pygame.display.flip()

    


    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(background, (0,0))
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('./musics/crash.mp3').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
       
        pygame.display.update()
        for entity in all_sprites:
                entity.kill() 
        time.sleep(2)
        print(f"Game over! Final score: {score}")
        pygame.quit()

        sys.exit()        
         
    pygame.display.update()
    
    FramePerSec.tick(FPS)