from imports import pygame

pygame.mixer.init()

def play_hover_sound(sound_path):
    try:
        hover_sound = pygame.mixer.Sound(sound_path)
        hover_sound.play()
    except pygame.error as e:
        print(f"Ошибка при воспроизведении звука при наведении: {e}")

def attach_hover_sound(button,sound_path):
    button.bind("<Enter>", lambda event: play_hover_sound(sound_path))