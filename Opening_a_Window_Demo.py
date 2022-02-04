import random
import pygame
pygame.init()
w = pygame.display.set_mode([400,300])
w.fill((255,255,255))

rand1 = random.randint(0,300)
rand2 = random.randint(0,300)

pygame.draw.line(w, (0,0,0), (50, rand1), (350, rand2), 10)

pygame.display.flip()
