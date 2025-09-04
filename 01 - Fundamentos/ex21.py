#Faça um programa que abra e reproduza um aúdio MP3.
import pygame

pygame.init()

pygame.mixer.music.load('assets/BomteEncontrar-EX21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()