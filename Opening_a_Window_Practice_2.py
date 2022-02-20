import pygame
pygame.init()

width = int(input("Please input the width "))
height = int(input("Please input the height "))

w = pygame.display.set_mode([width,height])

pygame.time.wait(5000)
