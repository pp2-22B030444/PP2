import pygame
import time
import random

pygame.init()
# цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gr = (100, 200, 100)
# Цвет экрана
BACKGROUND_COLOR = (255, 255, 255)
dis_width = 700
dis_height = 600
snake_List = []
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Просто змейка')
clock = pygame.time.Clock()
snake_block = 25
snake_speed = 4
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 25)
sound = pygame.mixer.Sound('./musics/song.mp3')
# Шрифт и размер текста
font = pygame.font.Font(None, 36)

# Начальный текст
text = ""

# sound.play()
# Функция которая счетает счет
def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    display.blit(value, [2, 0])

# фукция рисует змею
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block], 2)

# функция выводит текст
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width / 14, dis_height / 1.1])
def name(msg, color):
    mesg = font.render(msg, True, color)
    display.blit(mesg, [140, 250])

def Your_level(lavel):
    valu = score_font.render("Уровень: " + str(lavel), True, yellow)
    display.blit(valu, [2, 30])

def generate_food(snake_list):
    while True:
        # генерируем случайное положение для еды
        food_position = [round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0,
                         round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0]
        # проверяем, не находится ли еда внутри змеи
        if food_position not in snake_list:
            return food_position
def game_loop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_speed = 7
    snake_List = []
    length_of_snake = 1
    food_timer = pygame.time.get_ticks() + 5000
    food_timer1 = pygame.time.get_ticks() + 5000
    food_timer3 = pygame.time.get_ticks() + 5000
    food_position = generate_food(snake_List)
    foodx = food_position[0]
    foody = food_position[1]
    foodx = round(random.randrange(1, 28)) * 25.0
    foody = round(random.randrange(1, 24)) * 25.0
    foodx1 = round(random.randrange(1, 28)) * 25.0
    foody1 = round(random.randrange(1, 24)) * 25.0
    foodx2 = round(random.randrange(1, 28)) * 25.0
    foody2 = round(random.randrange(1, 24)) * 25.0
    image = pygame.image.load("./img/food.png")
    image1 = pygame.image.load("./img/food1.png")
    image2 = pygame.image.load("./img/food2.png")
    rect = image.get_rect()
    text = ""
    running = True
    background = pygame.image.load("./img/snake3.jpg")
    background1 = pygame.image.load("./img/lost4.jpg")
    back = pygame.image.load("./img/fill.png")
    back = pygame.transform.scale(back, (700,600))
    sound.play()
    while running:
        name("Вы проиграли! Нажмите Q для выхода или C для повторной игры!", black)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    running = False    
            if event.type == pygame.KEYDOWN :
                # # Добавляем нажатые символы к тексту
                text += event.unicode
            
        # Очищаем экран
        display.fill(BACKGROUND_COLOR)
        display.blit(back, (0,0))
        name("Чтобы начать игру введите свое имя:", black)
        # Создаем поверхность с текстом
        text_surface = font.render(text, True, (111, 0, 0))

        # Рисуем поверхность на экране
        display.blit(text_surface, (260, 300))
        #display.blit(back, (0,0))
        # Обновляем экран
        pygame.display.flip()         
    # цикл работает пока игра не закончится
    while not game_over:
        # цикл когда игра законцится и начать снова
        while game_close == True:
            # sound.play()
            display.blit(background1, (-280, -60))
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры!", white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        sound.stop()
                    elif event.key == pygame.K_c:
                        sound.play()
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
    
        # Обновляем экран
        #pygame.display.flip()
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        
        display.blit(background, (0, 0))
        # рисуем еду

        display.blit(image, [foodx, foody, snake_block, snake_block])
        display.blit(image1, [foodx1, foody1, snake_block, snake_block])
        display.blit(image2, [foodx2, foody2, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]
        # если змея столкнется с хвостом
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(length_of_snake - 1)
        Your_level(length_of_snake - 1)
        #pygame.display.update()
        # если змея столкнется с яблоком едой
        if x1 == foodx and y1 == foody:
            pygame.mixer.Sound('./musics/nam.mp3').play()
            foodx = round(random.randrange(1, 28)) * 25.0
            foody = round(random.randrange(1, 24)) * 25.0
            food_timer = pygame.time.get_ticks() + 5000
            length_of_snake += 0.5
            pygame.display.update()
        if pygame.time.get_ticks() >= food_timer:
            foodx = round(random.randrange(1, 28)) * 25.0
            foody = round(random.randrange(1, 24)) * 25.0
            food_timer = pygame.time.get_ticks() + 5000
            # если змея столкнется с вишней
        if x1 == foodx1 and y1 == foody1:
            pygame.mixer.Sound('./musics/nam.mp3').play()
            foodx1 = round(random.randrange(1, 28)) * 25.0
            foody1 = round(random.randrange(1, 24)) * 25.0
            food_timer1 = pygame.time.get_ticks() + 5000
            length_of_snake += 2
            pygame.display.update()
        if pygame.time.get_ticks() >= food_timer1:
            foodx1 = round(random.randrange(1, 28)) * 25.0
            foody1 = round(random.randrange(1, 24)) * 25.0
            food_timer1 = pygame.time.get_ticks() + 5000
        # если змея столкнется с зеленой едой
        if x1 == foodx2 and y1 == foody2:
            pygame.mixer.Sound('./musics/pah.mp3').play()
            foodx2 = round(random.randrange(1, 28)) * 25.0
            foody2 = round(random.randrange(1, 24)) * 25.0
            food_timer3 = pygame.time.get_ticks() + 5000
            length_of_snake = length_of_snake - 2
            if length_of_snake > 1:
                snake_List.pop(0)
                snake_List.pop(0)
            pygame.display.update()
        if pygame.time.get_ticks() >= food_timer3:
            foodx2 = round(random.randrange(1, 28)) * 25.0
            foody2 = round(random.randrange(1, 24)) * 25.0
            food_timer3 = pygame.time.get_ticks() + 5000
        # если длинна змеи меньше 0
        if length_of_snake <= 0:
            game_close = True
        elif length_of_snake >= 10:
            snake_speed += 0.0001
        clock.tick(snake_speed)
        pygame.display.update()
        # time.sleep(1)
    pygame.quit()
    quit()
game_loop()