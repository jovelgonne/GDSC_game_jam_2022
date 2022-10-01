from pickle import FALSE, TRUE
import sys
import pygame
from pygame import mixer
from pygame.locals import *

import give_text
import love_hate
import utility_functions
import pandoras_box

pygame.init()

# Important Variables
# ----------------------------------------------------
# Timing
fps = 60
fpsClock = pygame.time.Clock()
 
# Screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Tony')
width, height = screen.get_size()

# Main Menu
game_started = 0
ending_scene = False

# Love/Hate Meters
love_hate_meter = 5
meter_max = 10

# Text
dialogue_font = pygame.font.Font('font/game_over.ttf', 64)
instructions_font = pygame.font.Font('font/comicsans.ttf', 48)
line_number = -1
space_pressed = 0
frames_since_space = 0

is_option = False
option_selected = False             # False if option 1, true if option 2
display_option_response = False 
option_number = 0                  # Keeps track of which option we're on

# Constants
# ----------------------------------------------------------
CAFETERIA = 12
CAFE = CAFETERIA + 19
RAIN = CAFE + 36
CLIFF = RAIN + 17
CLIFF2 = CLIFF + 0
CREDIT = CLIFF2 + 0

# Colors
# ----------------------------------------------------------
PINK = (255,182,193)
WHITE = (255,255,255)
BRONZE = (205,127,50)
BLACK = (0,0,0)
GREY = (47,79,79)
BLUE = (197,207,252)
MUTED_PINK = (229,180,193)
MAGENTA = (255,0,255)

# Music and Audio
# ---------------------------------------------------------
#Instantiate mixer
mixer.init()

#Load audio file
mixer.music.load('audio/Oh_Tony.mp3')

#Set preferred volume
mixer.music.set_volume(0.1)

#Play the music
# mixer.Channel(0).play(pygame.mixer.Sound('audio/Oh_Tony.mp3'), loops=-1)


# Graphics
# ---------------------------------------------------------

# Title card
title = pygame.image.load("images/title.png").convert_alpha()
title = pygame.transform.rotozoom(title,0,2)

# Characters
player = pygame.image.load("images/Player.png").convert_alpha()
player = pygame.transform.rotozoom(player,0,0.4)
tony_happy = pygame.image.load("images/happy.png").convert_alpha()
tony_happy = pygame.transform.rotozoom(tony_happy,0,0.4)
tony_neutral = pygame.image.load("images/neutral.png").convert_alpha()
tony_neutral = pygame.transform.rotozoom(tony_neutral,0,0.4)
tony_angry = pygame.image.load("images/angry.png").convert_alpha()
tony_angry = pygame.transform.rotozoom(tony_angry,0,0.4)
tony_blush = pygame.image.load("images/blush.png").convert_alpha()
tony_blush = pygame.transform.rotozoom(tony_blush,0,0.4)
tony_jojo = pygame.image.load("images/Opening pose.png").convert_alpha()
tony_jojo = pygame.transform.rotozoom(tony_jojo,0,0.55)
tony_cafe = pygame.image.load("images/cafe.png").convert_alpha()
tony_cafe = pygame.transform.rotozoom(tony_cafe,0,0.48)
sonia_neutral = pygame.image.load("images/sonia neutral.png").convert_alpha()
sonia_neutral = pygame.transform.rotozoom(sonia_neutral,0,0.55)
sonia_smirk = pygame.image.load("images/sonia smirk.png").convert_alpha()
sonia_smirk = pygame.transform.rotozoom(sonia_smirk,0,0.55)
sonia_weak = pygame.image.load("images/sonia weak.png").convert_alpha()
sonia_weak = pygame.transform.rotozoom(sonia_weak,0,0.5)
tony_wet = pygame.image.load("images/drenched.png").convert_alpha()
tony_wet = pygame.transform.rotozoom(tony_wet,0,0.5)
tony_dead = pygame.image.load("images/bad ending.png").convert_alpha()
tony_dead = pygame.transform.rotozoom(tony_dead,0,0.5)
tony_good = pygame.image.load("images/happy ending.png").convert_alpha()
tony_good = pygame.transform.rotozoom(tony_good,0,0.5)
pooh = pygame.image.load("images/Poohwee.png").convert_alpha()
pooh = pygame.transform.rotozoom(pooh,0,0.7)
characters = [tony_happy,tony_neutral,tony_angry,tony_blush,tony_jojo,tony_cafe,sonia_smirk,sonia_neutral,player,sonia_weak,tony_wet,tony_dead,tony_good,pooh]

# Backgrounds
office = pygame.image.load("images/backgrounds/office.png").convert()
office = pygame.transform.scale(office, (width, height))
cafeteria = pygame.image.load("images/backgrounds/cafeteria.png").convert()
cafeteria = pygame.transform.scale(cafeteria, (width, height))
cafe = pygame.image.load("images/backgrounds/cafe.png").convert()
cafe = pygame.transform.scale(cafe, (width, height))
rain = pygame.image.load("images/backgrounds/rain.png").convert()
rain = pygame.transform.scale(rain, (width, height))
cliff = pygame.image.load("images/backgrounds/cliff.png").convert()
cliff = pygame.transform.scale(cliff, (width, height))
cliff_bad = pygame.image.load("images/backgrounds/cliff_bad.png").convert()
cliff_bad = pygame.transform.scale(cliff_bad, (width, height))
backgrounds = [office, cafeteria, cafe, rain, cliff, cliff_bad]

# Dialogue Box
dialog_box = pygame.image.load("images/textbox.png").convert()
dialog_box = pygame.transform.scale(office, (width, height))

current_character = tony_jojo
current_background = 0

[character_width, character_height] = current_character.get_size()

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

            # TEMPORARY SKIP BUTTON
            if event.key == pygame.K_6:
                line_number += 10
                print("hey")

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
                        if display_option_response == True:
                            is_option = False
                            line_number += 1
                        else:
                            love_hate_meter = love_hate.update_bar(love_hate_meter, option_number, option_selected)  
                            # Counter
                            option_number += 1 

                            # ADD CHOICE STUFF HERE
                            current_character = pandoras_box.options(line_number, characters, current_character, option_selected)

                        
                        display_option_response = not display_option_response

                    else:
                        # Update next line of text if all previous text already displayed 
                        line_number += 1

                    if (line_number == CLIFF):
                        if ending_scene == False:
                            if love_hate_meter <= 5:
                                ending_scene = True
                            else:
                                line_number = CLIFF2
                                ending_scene = True
                        else:
                            line_number = CREDIT
                    
                    
                    # CHANGE MUSIC HERE MIGGY
                    # if line_number == CAFETERIA:
                    #     mixer.music.stop()
                    #     mixer.music.load('audio/Astral_Wind.mp3')
                    #     mixer.Channel(0).play(pygame.mixer.Sound('audio/Astral_Wind.mp3'), loops=-1)

                    # CHANGE ANY IMAGES HERE
                    [current_character,current_background] = pandoras_box.open(line_number, current_background, characters, current_character)  

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                option_selected = not option_selected

    # Update frame count if adding text to screen
    if space_pressed == 1:
        frames_since_space+= 1

    # Draw Background
    screen.blit(backgrounds[current_background], (0, 0))

    # Draw Title/Character
    if game_started == 0:
        # Setup and Draw Dialog Box
        text_padding = 60
        instructions_width_pad = 300
        instructions_height_pad = 500
        row_offset = 40

        screen.blit(title, (0, -450))
        instructions_text = ["Instructions:","","* Press Space to Progress","* Up and Down keys to scroll dialogue options","* Your decisions influence the final events!"]
        for row_number, row_content in enumerate(instructions_text):
            text_render = instructions_font.render(row_content, True, BLACK)
            screen.blit(text_render, (instructions_width_pad,instructions_height_pad+row_number*row_offset))
    else:
        screen.blit(current_character, (0.5*(width-character_width), 0))

    # Might work on this later
    # # Pause/Unpause Button 
    # button_padding = 50
    # button_width = 50
    # pygame.draw.rect(screen, PINK, pygame.Rect(screen.get_width()-button_padding-button_width, button_padding, button_width, button_width),5,5,5,5)





    if game_started == 1:

        # Setup and Draw Dialog Box
        dialog_box_padding = 40
        text_padding = 60
        text_offset = 20
        row_offset = 40
        pygame.draw.rect(screen, color=PINK, rect=pygame.Rect(dialog_box_padding, 0.75*height, width-2*dialog_box_padding, 0.25*height-dialog_box_padding))
        # screen.blit(dialog_box, (0, 0))

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


        # Draw Love and Hate Meters
        meter_width = 150
        meter_height = 40
        pygame.draw.rect(screen, color=MUTED_PINK, rect=pygame.Rect(text_padding, text_padding, ((10-love_hate_meter)/meter_max)*meter_width, meter_height))
        pygame.draw.rect(screen, color=BLUE, rect=pygame.Rect(width-text_padding-meter_width, text_padding, (love_hate_meter/meter_max)*meter_width, meter_height))

        pygame.draw.rect(screen, color=BLACK, rect=pygame.Rect(text_padding, text_padding, meter_width, meter_height), width=3)
        pygame.draw.rect(screen, color=BLACK, rect=pygame.Rect(width-text_padding-meter_width, text_padding, meter_width, meter_height), width=3)

        # Temporary Labels
        text_render = dialogue_font.render("Love", True, BLACK)                # Make text scroll in
        screen.blit(text_render, (text_padding+10, text_padding))
        text_render = dialogue_font.render("Spite", True, BLACK)                # Make text scroll in
        screen.blit(text_render, (width-text_padding-meter_width+10, text_padding))
    
    


    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    fpsClock.tick(fps)