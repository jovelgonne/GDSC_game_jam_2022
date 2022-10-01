from pickle import FALSE, TRUE
import sys
import pygame
from pygame import mixer
from pygame.locals import *

import give_text
import utility_functions

pygame.init()

# Important Variables
# ----------------------------------------------------
# Timing
fps = 60
fpsClock = pygame.time.Clock()
 
# Screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Tony')

# Main Menu
game_started = 0

# Text
dialogue_font = pygame.font.Font('font/game_over.ttf', 64)
line_number = -1
space_pressed = 0
frames_since_space = 0

is_option = False
option_selected = False         # False if option 1, true if option 2
display_option_response = False
 
# Colors
PINK = (255,182,193)
WHITE = (255,255,255)
BRONZE = (205,127,50)
BLACK = (0,0,0)
GREY = (47,79,79)

# Music and Audio
# ---------------------------------------------------------
#Instantiate mixer
mixer.init()

#Load audio file
mixer.music.load('audio/Oh_Tony.mp3')

#Set preferred volume
mixer.music.set_volume(0.1)

#Play the music
mixer.Channel(0).play(pygame.mixer.Sound('audio/Oh_Tony.mp3'), loops=-1)


# Graphics
# ---------------------------------------------------------
# Characters
tony_jojo = pygame.image.load("images/Opening pose.png").convert_alpha()
tony_jojo = pygame.transform.rotozoom(tony_jojo,0,0.48)

tony_cafe = pygame.image.load("images/cafe.png").convert_alpha()
tony_cafe = pygame.transform.rotozoom(tony_cafe,0,0.48)

current_background = 0

# Backgrounds
office = pygame.image.load("images/backgrounds/office.png").convert()
office = pygame.transform.rotozoom(office,0,0.8)
cafeteria = pygame.image.load("images/backgrounds/cafeteria.png").convert()
cafeteria = pygame.transform.rotozoom(cafeteria,0,0.8)
cafe = pygame.image.load("images/backgrounds/cafe.png").convert()
cafe = pygame.transform.rotozoom(cafe,0,0.8)
rain = pygame.image.load("images/backgrounds/rain.png").convert()
rain = pygame.transform.rotozoom(rain,0,0.8)
cliff = pygame.image.load("images/backgrounds/cliff.png").convert()
cliff = pygame.transform.rotozoom(cliff,0,0.8)
backgrounds = [office, cafeteria, cafe, rain, cliff]

# Main Game loop
# ---------------------------------------------------------
while True:
    screen.fill(BLACK)
  
    for event in pygame.event.get():
        # Allow Quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Quit Condition
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        # Updates
            if event.key == pygame.K_SPACE:
                # Start Game if haven't already
                game_started = 1

                if space_pressed == 1:
                    frames_since_space = 500
                else:
                    space_pressed = 1
                    frames_since_space = 0
                    if is_option == True:
                        # ADD TO LOVE/HATE METER                     
                        if display_option_response == True:
                            is_option = False
                            line_number += 1
                        
                        display_option_response = not display_option_response

                    

                    else:
                        # Update next line of text if all previous text already displayed 
                        line_number += 1

                            # CHANGING MUSIC
                            # INSERT MUSIC HERE MIGGY (Just copy below 4 lines of code, change line_number and audio loaded in)
                        if line_number == 3:
                            mixer.music.stop()
                            mixer.music.load('audio/Astral_Wind.mp3')
                            mixer.Channel(0).play(pygame.mixer.Sound('audio/Astral_Wind.mp3'), loops=-1)

                            current_background += 1
        
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                option_selected = not option_selected

    # Update frame count if adding text to screen
    if space_pressed == 1:
        frames_since_space+= 1
    

    # Background
    screen.blit(backgrounds[current_background], (0, 0))

    # Character
    screen.blit(tony_jojo, (320, -140))

    # Pause/Unpause Button
    button_padding = 50
    button_width = 50
    pygame.draw.rect(screen, PINK, pygame.Rect(screen.get_width()-button_padding-button_width, button_padding, button_width, button_width),5,5,5,5)


    if game_started == 1:

        # Setup and Draw Dialog Box
        dialog_box_padding = 40
        text_padding = 60
        text_offset = 20
        row_offset = 40
        width, height = screen.get_size()
        pygame.draw.rect(screen, color=PINK, rect=pygame.Rect(dialog_box_padding, 0.75*height, width-2*dialog_box_padding, 0.25*height-dialog_box_padding))

        # Retrieve Text
        text = give_text.current_text(line_number)

        # Check if its a choice line
        is_option = (">" in text)

        # If it's not, proceed
        if is_option == False:
            # Text Scrolling In
            [text, space_pressed] = utility_functions.shorten_string(text, frames_since_space)

            # Split text into different lines and display
            text = text.split("\n")
            for row_number, row_content in enumerate(text):
                text_render = dialogue_font.render(row_content, True, BLACK)
                screen.blit(text_render, (text_padding,0.75*height+text_offset+row_number*row_offset))

        # If is a choice line, render with choice boxes
        elif is_option == True:                        # CHANGE THIS LATER SO THAT IT CAN BE MORE THAN ONE LINE
            text = text.split("\n")
            if display_option_response == False:    
                # Text Scrolling In
                [text[0], space_pressed] = utility_functions.shorten_string(text[0], frames_since_space)

                text_render = dialogue_font.render(text[0], True, BLACK)
                screen.blit(text_render, (text_padding,0.75*height+text_offset+row_offset))

                # Draw Option Boxes
                option_box_padding = 400
                selected_padding = 5

                # Highlight Selected Box
                if option_selected == False:
                    pygame.draw.rect(screen, color=GREY, rect=pygame.Rect(option_box_padding-selected_padding, 0.55*height-selected_padding, width-2*(option_box_padding-selected_padding), 0.1*height+2*selected_padding-dialog_box_padding))
                elif option_selected == True:
                    pygame.draw.rect(screen, color=GREY, rect=pygame.Rect(option_box_padding-selected_padding, 0.65*height-selected_padding, width-2*(option_box_padding-selected_padding), 0.1*height+2*selected_padding-dialog_box_padding))

                # Boxes
                pygame.draw.rect(screen, color=PINK, rect=pygame.Rect(option_box_padding, 0.65*height, width-2*option_box_padding, 0.1*height-dialog_box_padding))
                pygame.draw.rect(screen, color=PINK, rect=pygame.Rect(option_box_padding, 0.55*height, width-2*option_box_padding, 0.1*height-dialog_box_padding))

                # Add options text
                option1 = text[1]              
                option2 = text[2]
                option_text_offset = 400

                text_render = dialogue_font.render(option1, True, BLACK)
                screen.blit(text_render, (option_text_offset,0.53*height+text_offset))
                text_render = dialogue_font.render(option2, True, BLACK)
                screen.blit(text_render, (option_text_offset,0.63*height+text_offset))

            # Showing response to option chosen    
            if display_option_response == True:
                if option_selected == False:
                    response = text[3]
                else:
                    response = text[4]
                [response, space_pressed] = utility_functions.shorten_string(response, frames_since_space)
                text_render = dialogue_font.render(response, True, BLACK)                # Make text scroll in
                screen.blit(text_render, (text_padding,0.75*height+text_offset+row_offset))
        else:
            print("Error in is_option variable")




    
    


    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    fpsClock.tick(fps)