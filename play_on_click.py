from imports import pygame

pygame.mixer.init()

def play_sound_on_click(sound_path):
    sound = pygame.mixer.Sound(sound_path)
    sound.play()