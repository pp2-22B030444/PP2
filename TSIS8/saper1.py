
import pygame
import sys

pygame.init()
width = 750
height = 400
white = (255, 255, 255)
black = (0, 0, 0)

game_over = False
game_close = False
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Minesweeper')
clock = pygame.time.Clock()

block_size = 25
num_columns = width // block_size
num_rows = height // block_size

grid = [[0 for _ in range(num_columns)] for _ in range(num_rows)]


def draw_grid():
    for row in range(num_rows):
        for col in range(num_columns):
            x = col * block_size
            y = row * block_size
            pygame.draw.rect(display, white, [x, y, block_size, block_size], 1)


def draw_numbers():
    for row in range(num_rows):
        for col in range(num_columns):
            x = col * block_size
            y = row * block_size
            if grid[row][col] != -1:
                count = count_adjacent_mines(row, col)
                if count != 0:
                    font = pygame.font.Font(None, 20)
                    text = font.render(str(count), True, black)
                    text_rect = text.get_rect(center=(x + block_size // 2, y + block_size // 2))
                    display.blit(text, text_rect)


def count_adjacent_mines(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if row + i >= 0 and row + i < num_rows and col + j >= 0 and col + j < num_columns:
                if grid[row + i][col + j] == -1:
                    count += 1
    return count


def reveal_adjacent_cells(row, col):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if row + i >= 0 and row + i < num_rows and col + j >= 0 and col + j < num_columns:
                if grid[row + i][col + j] == 0:
                    grid[row + i][col + j] = -2
                    reveal_adjacent_cells(row + i, col + j)


def game_over_screen():
    display.fill(white)
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, black)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    display.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)


def game_loop():
    global game_over
    global game_close

    while not game_over:
        while game_close:
            game_over_screen()
            game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Левая кнопка мыши
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // block_size
                    row = pos[1] // block_size

                    if grid[row][col] == -1:
                        game_close = True
                    else:
                        grid[row][col] = -2
                        reveal_adjacent_cells(row, col)
                elif event.button == 3:
                    # Правая кнопка мыши
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // block_size
                    row = pos[1] // block_size

                    if grid[row][col] == 0:
                        grid[row][col] = -1
                    elif grid[row][col] == -1:
                        grid[row][col] = 0

        display.fill(white)
        draw_grid()
        draw_numbers()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
