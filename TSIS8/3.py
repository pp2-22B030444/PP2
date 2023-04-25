import pygame

pygame.init()

# Размер окна
WINDOW_SIZE = (800, 600)

# Создаем окно
screen = pygame.display.set_mode(WINDOW_SIZE)

# Цвет экрана
BACKGROUND_COLOR = (255, 255, 255)

# Шрифт и размер текста
font = pygame.font.Font(None, 36)

# Начальный текст
text = ""

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Добавляем нажатые символы к тексту
            text += event.unicode

    # Очищаем экран
    screen.fill(BACKGROUND_COLOR)

    # Создаем поверхность с текстом
    text_surface = font.render(text, True, (0, 0, 0))

    # Рисуем поверхность на экране
    screen.blit(text_surface, (50, 50))

    # Обновляем экран
    pygame.display.flip()

# Выходим из pygame
pygame.quit()
