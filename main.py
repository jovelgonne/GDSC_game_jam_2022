import sys
import pygame
from pygame.locals import *
import math

import give_text
 
pygame.init()

# Timing
fps = 60
fpsClock = pygame.time.Clock()
 
# Screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Dialogue Boxes')

# Text
dialogue_font = pygame.font.Font('font/game_over.ttf', 64)
line_number = -1
space_pressed = 0
frames_since_space = 0

 
# Color
PINK = (255,182,193)

# Game loop
while True:
    screen.fill((0, 0, 0))
  
    for event in pygame.event.get():
        # Allow Quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Quit Condition
        # if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        # Updates
            if event.key == pygame.K_SPACE:
                space_pressed = 1
                frames_since_space = 0
                line_number += 1
                print("space pressed")

    if space_pressed == 1:
        frames_since_space+= 1
    

    # Dialog box
    dialog_box_padding = 40
    text_padding = 60
    text_offset = 20
    row_offset = 40
    width, height = screen.get_size()
    pygame.draw.rect(screen, color=PINK, rect=pygame.Rect(dialog_box_padding, 0.75*height, width-2*dialog_box_padding, 0.25*height-dialog_box_padding))
    
    # Updating Text
    text = give_text.current_text(line_number)
    length_of_text = len(text)
    if space_pressed == 1:
        if length_of_text > (frames_since_space):      # Add text char-by-char
            text = text[:(frames_since_space)]
        else:
            space_pressed == 0                         # Reset the space button
        text = text.split("\n")
        for row_number, row_content in enumerate(text):
            text_render = dialogue_font.render(row_content, True, (0,0,0))
            screen.blit(text_render, (text_padding,0.75*height+text_offset+row_number*row_offset))


    # Drawing Shit
    
    


    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    fpsClock.tick(fps)