#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()

som = pygame.mixer.Sound('Kalimba.mp3')
som.play()

run = True
while run:
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  run = False