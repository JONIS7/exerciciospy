import pygame
pygame.init()
pygame.mixer.init()
mp3_file = r'C:\Users\55869\Downloads/01 - Pior e Te Perder - Luan Estilizado Pra Tomar Cachaca 2.mp3'
pygame.mixer.music.load(mp3_file)
print('ouça um forrozao bolado!')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
pygame.mixer.quit()