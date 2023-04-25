import pygame
import time
import random, re
import sys
import os
import psycopg2

conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = 'adminkbtu')
cur = conn.cursor()
cur.execute('''
CREATE TABLE snake-list(
    id INTEGER PRIMARY KEY,
    player VARCHAR(255) NOT NULL
);
''')

conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = 'adminkbtu')
cur = conn.cursor()
cur.execute('''
INSERT INTO snake-list (player) VALUES(%s)
);
''')
pygame.init()
# цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gr = (100, 200, 100)
dis_width = 800
dis_height = 800
snake_List = []
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Просто змейка')
clock = pygame.time.Clock()
snake_block = 25
snake_speed = 4
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 30)
sound = pygame.mixer.Sound('./musics/song.mp3')
block=pygame.image.load("./img/wall1.png")

# Функция которая счетает счет
def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, gr)
    display.blit(value, [30, 20])
# фукция рисует змею
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, yellow, [x[0], x[1], snake_block, snake_block])
# функция выводит текст
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width / 10, dis_height / 1.2])
def Your_level(lavel):
    valu = score_font.render("Уровень: " + str(lavel), True, gr)
    display.blit(valu, [35, 50])   
class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        display.blit(block, (self.x, self.y))
def game_loop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    levels=0
    cnt=10
    snake_speed = 7
    snake_List = []
    length_of_snake = 1
    food_timer = pygame.time.get_ticks() + 6000
    food_timer1 = pygame.time.get_ticks() + 6000
    food_timer3 = pygame.time.get_ticks() + 6000
    foodx = round(random.randrange(2, 31)) * 25.0
    foody = round(random.randrange(2, 31)) * 25.0
    foodx1 = round(random.randrange(2, 31)) * 25.0
    foody1 = round(random.randrange(2, 31)) * 25.0
    foodx2 = round(random.randrange(2, 31)) * 25.0
    foody2 = round(random.randrange(2, 31)) * 25.0
    image = pygame.image.load("./img/food.png")
    image1 = pygame.image.load("./img/food1.png")
    image2 = pygame.image.load("./img/food2.png")
    re = image.get_rect()
    re1 = image1.get_rect()
    re2 = image2.get_rect()
    background = pygame.image.load("./img/back.png")
    background = pygame.transform.scale(background, (800, 800))
    background1 = pygame.image.load("./img/lost1.jpg")
    background1 = pygame.transform.scale(background1, (800,800))
    sound.play()

    # цикл работает пока игра не закончится
    while not game_over:
        # цикл когда игра законцится и начать снова
        while game_close == True:
            # sound.play()
            display.blit(background1, (0,0))
            # display.fill(yellow)
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры!", white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False                       
                    elif event.key == pygame.K_c:
                        sound.stop()                       
                        #sound.play()
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        # Обновление экрана
        pygame.display.update()            
        if y1 >= 25 and x1 <= 25 or y1<=25 and x1>=25:
            game_close = True
        if x1<=750 and y1>=750 or x1>=750 and y1<=750:
            game_close = True

        x1 += x1_change
        y1 += y1_change
       
        display.blit(background, (0, 0))
        # рисуем еду      
        display.blit(image,[foodx, foody, snake_block,snake_block])
        display.blit(image1, [foodx1, foody1, snake_block, snake_block])
        display.blit(image2, [foodx2, foody2, snake_block, snake_block])
        # pygame.display.update()
        # pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
        # pygame.draw.rect(display, yellow, [foodx1, foody1, snake_block, snake_block])
        # pygame.draw.rect(display, black, [foodx2, foody2, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        print(snake_List)
        
        if len(snake_List) > length_of_snake:
            del snake_List[0]
        # если змея столкнется с хвостом
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(length_of_snake - 1)
        Your_level(levels)       
        # если змея столкнется с яблоком
        if x1 == foodx and y1 == foody:
            pygame.mixer.Sound('./musics/nam.mp3').play()
            length_of_snake += 2
            foodx = round(random.randrange(2, 31)) * 25.0
            foody = round(random.randrange(2, 31)) * 25.0
            food_timer = pygame.time.get_ticks() + 6000
            
            #pygame.display.update()
        if pygame.time.get_ticks() >= food_timer:
            foodx = round(random.randrange(2, 31)) * 25.0
            foody = round(random.randrange(2, 31)) * 25.0
            food_timer = pygame.time.get_ticks() + 6000
            # если змея столкнется с вишней
        if x1 == foodx1 and y1 == foody1:
            pygame.mixer.Sound('./musics/nam.mp3').play()
            length_of_snake += 3
            foodx1 = round(random.randrange(2, 31)) * 25.0
            foody1 = round(random.randrange(2, 31)) * 25.0
            food_timer1 = pygame.time.get_ticks() + 6000
            #pygame.display.update()
        if pygame.time.get_ticks() >= food_timer1:
            foodx1 = round(random.randrange(2, 31)) * 25.0
            foody1 = round(random.randrange(2, 31)) * 25.0
            food_timer1 = pygame.time.get_ticks() + 6000
            # если змея столкнется с зеленой едой
        if x1 == foodx2 and y1 == foody2:
            pygame.mixer.Sound('./musics/pah.mp3').play()
            length_of_snake = length_of_snake - 2
            if length_of_snake > 1:
                snake_List.pop(0)
                snake_List.pop(0)
            foodx2 = round(random.randrange(2, 31)) * 25.0
            foody2 = round(random.randrange(2, 31)) * 25.0
            food_timer3 = pygame.time.get_ticks() + 6000

        if pygame.time.get_ticks() >= food_timer3:
            foodx2 = round(random.randrange(2, 31)) * 25.0
            foody2 = round(random.randrange(2, 31)) * 25.0
            food_timer3 = pygame.time.get_ticks() + 6000
        if [foodx, foody] in snake_List:
            foodx = round(random.randrange(2, 31)) * 25.0
            foody = round(random.randrange(2, 31)) * 25.0
        if [foodx1, foody1] in snake_List:
            foodx1 = round(random.randrange(2, 31)) * 25.0
            foody1 = round(random.randrange(2, 31)) * 25.0
        if [foodx2, foody2] in snake_List:
            foodx2 = round(random.randrange(2, 31)) * 25.0
            foody2 = round(random.randrange(2, 31)) * 25.0
                
        file = open(f'./img/{levels}.txt', 'r').readlines()
        walls = []
        for i , line in enumerate(file):
            for j , each in enumerate(line):
                if each == '+':
                    walls.append(Wall(j*25, i*25))

        for wall in walls:
            wall.draw()
            if snake_List[len(snake_List)-1][0] == wall.x and snake_List[len(snake_List)-1][1] == wall.y:
                game_close = True
            if wall.x==foodx and wall.y==foody:
                foodx = round(random.randrange(2, 31)) * 25.0
                foody = round(random.randrange(2, 31)) * 25.0
            if wall.x==foodx1 and wall.y==foody1:
                foodx1 = round(random.randrange(2, 31)) * 25.0
                foody1 = round(random.randrange(2, 31)) * 25.0    
            if wall.x==foodx2 and wall.y==foody2:
                foodx2 = round(random.randrange(2, 31)) * 25.0
                foody2 = round(random.randrange(2, 31)) * 25.0
            
        # если длинна змеи меньше 0
        if length_of_snake <= 0:
            game_close = True
        if length_of_snake> cnt:
            levels+=1
            levels%=4
            cnt+=10
        elif length_of_snake >= 10:
            snake_speed += 0.001

        clock.tick(snake_speed)
        #pygame.display.update()
        # time.sleep(1)
    pygame.quit()
    quit()
game_loop()