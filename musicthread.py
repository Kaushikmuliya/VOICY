import os
import threading
import pygame

pygame.mixer.init()
def play_music(file_path):

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print("Pygame error:", e)


def stop_music():
    pygame.mixer.music.stop()


