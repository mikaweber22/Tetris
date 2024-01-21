import pygame
import random
import logik
import test

RICHTUNG = "UNTEN"


BILDSCHIRM_BREITE = 600
BILDSCHRIM_HÖHE = 800

# Starte pygame
pygame.init

spiel_läuft = True
pygame.display.set_mode((BILDSCHIRM_BREITE, BILDSCHRIM_HÖHE))

uhr = pygame.time.Clock()


while spiel_läuft:
    pygame.display.flip()

    uhr.tick(20)
    
pygame.quit()
quit()


