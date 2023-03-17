import pygame
from pygame.locals import *
from mutagen.mp3 import MP3
import os

pygame.init()
win = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")
music_dir = "D:\Music"
music_list = os.listdir(music_dir)
music_dict = {}
for file in music_list:
    if file.endswith(".mp3"):
        filepath = os.path.join(music_dir, file)
        title = MP3(filepath).tags["TIT2"].text[0]
        music_dict[title] = filepath
def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    current_file = pygame.mixer.music.get_busy()
    current_index = music_list.index(current_file)
    if current_index == len(music_list) - 1:
        next_file = music_list[0]
    else:
        next_file = music_list[current_index + 1]
    next_file_path = os.path.join(music_dir, next_file)
    play_music(next_file_path)

def prev_music():
    current_file = pygame.mixer.music.get_busy()
    current_index = music_list.index(current_file)
    if current_index == 0:
        prev_file = music_list[len(music_list) - 1]
    else:
        prev_file = music_list[current_index - 1]
    prev_file_path = os.path.join(music_dir, prev_file)
    play_music(prev_file_path)
def handle_events():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN:
            if event.key == K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music(music_dict[list(music_dict.keys())[0]])
            elif event.key == K_n:
                next_music()
            elif event.key == K_p:
                prev_music()
        elif event.type == QUIT:
            pygame.quit()
            #sys.exit()
while True:
    handle_events()
    if __name__ == "__main__":
        pygame.mixer.init()
    while True:
        handle_events()