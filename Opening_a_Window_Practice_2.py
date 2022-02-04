# Import and initialize pygame
import pygame
pygame.init()


# Get the width and height from the user
width = int(input("Please input the width "))
height = int(input("Please input the height "))

# Open the window
w = pygame.display.set_mode([width,height])

# Wait 5 seconds
pygame.time.wait(5000)
