from imports import pygame

pygame.mixer.init()

def play_on_loading(sound_path):
    try:
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Ошибка при воспроизведении звука: {e}")