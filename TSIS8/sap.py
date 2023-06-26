import pygame

# инициализируем pygame
pygame.init()

# задаем размер экрана
screen_width = 800
screen_height = 600

# создаем окно с указанными размерами
screen = pygame.display.set_mode((screen_width, screen_height))

# создаем класс блока
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# создаем группу спрайтов для всех блоков на экране
all_blocks = pygame.sprite.Group()

# создаем блоки и добавляем их в группу 
block1 = Block((255, 0, 0), 50, 50)
block1.rect.x = 100
block1.rect.y = 100
all_blocks.add(block1)

block2 = Block((0, 255, 0), 50, 50)
block2.rect.x = 200
block2.rect.y = 200
all_blocks.add(block2)

# главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        
        # обработка события закрытия окна
        if event.type == pygame.QUIT:
            running = False
            
        # обработка нажатий клавиш
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # левая кнопка мыши
                
                # получаем координаты клика мыши
                mouse_pos = pygame.mouse.get_pos()
                
                # проверяем, находится ли на этом месте какой-нибудь блок
                block_hit_list = [b for b in all_blocks if b.rect.collidepoint(mouse_pos)]
                
                # если есть хотя бы один блок, удаляем его
                if len(block_hit_list) > 0:
                    block = block_hit_list[0]
                    block.kill()
    
    # очищаем экран и отрисовываем все блоки
    screen.fill((255, 255, 255))
    all_blocks.draw(screen)
    
    # обновляем экран
    pygame.display.flip()
    
# завершаем работу pygame
pygame.quit()
