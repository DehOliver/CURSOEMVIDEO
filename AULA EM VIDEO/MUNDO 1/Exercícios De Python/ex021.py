import pygame
pygame.init()

pygame.mixer.music.load('C:\Users\denne\Documents\CURSOEMVIDEO\AULA EM VIDEO\MUNDO 1\Exercícios De Python\ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

while pygame.mixer.music.get_busy():
    continue

pygame.quit()