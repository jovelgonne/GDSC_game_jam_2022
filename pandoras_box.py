# Constants
# ----------------------------------------------------------
CAFETERIA = 12
CAFE = CAFETERIA + 19
RAIN = CAFE + 35
CLIFF = RAIN + 16
CLIFF2 = CLIFF + 20
CREDIT = CLIFF2 + 20

tony_happy = 0
tony_neutral = 1
tony_angry = 2
tony_blush = 3
tony_jojo = 4
tony_cafe = 5
sonia_smirk = 6
sonia_neutral = 7 
player = 8
sonia_weak = 9
tony_wet = 10
tony_dead = 11
tony_good = 12
pooh = 13

def open(line_number, current_background, characters, old_character):
    current_character = -1

    if line_number == 1:
        current_character = tony_happy
    if line_number == 2:
        current_character = tony_neutral
    if line_number == 6:
        current_character = player
    if line_number == 7:
        current_character = tony_happy
    
    if line_number == (CAFETERIA):
        current_character = player
        current_background += 1
    if line_number == (CAFETERIA+1): # This is for line 2, even though it's +1
        current_character = sonia_smirk
    if line_number == (CAFETERIA+2):
        current_character = sonia_neutral
    if line_number == (CAFETERIA+4):
        current_character = tony_cafe
    if line_number == (CAFETERIA+6):
        current_character = sonia_neutral
    if line_number == (CAFETERIA+7):
        current_character = tony_happy
    if line_number == (CAFETERIA+8):
        current_character = sonia_neutral
    if line_number == (CAFETERIA+9):
        current_character = tony_angry
    if line_number == (CAFETERIA+10):
        current_character = tony_neutral
    if line_number == (CAFETERIA+11):
        current_character = sonia_neutral
    if line_number == (CAFETERIA+12):
        current_character = tony_neutral
    if line_number == (CAFETERIA+14):
        current_character = player
    if line_number == (CAFETERIA+15):
        current_character = sonia_neutral
    if line_number == (CAFETERIA+16):
        current_character = sonia_smirk
    if line_number == (CAFETERIA+18):
        current_character = player

    if line_number == CAFE:
        current_character = player
        current_background += 1
    if line_number == (CAFE+1): # For line 2
        current_character = tony_happy
    if line_number == (CAFE+3):
        current_character = tony_neutral
    if line_number == (CAFE+5):
        current_character = tony_happy
    if line_number == (CAFE+6):
        current_character = player
    if line_number == (CAFE+7):
        current_character = tony_happy
    if line_number == (CAFE+10):
        current_character = player
    if line_number == (CAFE+11):
        current_character = pooh
    if line_number == (CAFE+12):
        current_character = tony_happy
    if line_number == (CAFE+13):
        current_character = tony_blush
    if line_number == (CAFE+14):
        current_character = player
    if line_number == (CAFE+15):
        current_character = pooh
    if line_number == (CAFE+16):
        current_character = player
    if line_number == (CAFE+17):
        current_character = pooh
    if line_number == (CAFE+18):
        current_character = player
    if line_number == (CAFE+19):
        current_character = pooh
    if line_number == (CAFE+23):
        current_character = tony_angry
    if line_number == (CAFE+24):
        current_character = pooh
    if line_number == (CAFE+25):
        current_character = tony_angry
    if line_number == (CAFE+26):
        current_character = pooh
    if line_number == (CAFE+27):
        current_character = tony_angry
    if line_number == (CAFE+28):
        current_character = pooh
    if line_number == (CAFE+29):
        current_character = player
    if line_number == (CAFE+30):
        current_character = pooh
    if line_number == (CAFE+32):
        current_character = tony_angry
    if line_number == (CAFE+34):
        current_character = player
    
    if current_character == -1:
        return[old_character,current_background]
    else:
        return[characters[current_character],current_background]


def options(line_number, characters, old_character, option_selected):
    current_character = -1

    if line_number == 10:
        if option_selected == False:
            current_character = tony_happy
        if option_selected == True:
            current_character = tony_neutral

    if line_number == (CAFETERIA+2):
        current_character = sonia_smirk
    if line_number == (CAFETERIA+13):
        if option_selected == False:
            current_character = tony_happy
        if option_selected == True:
            current_character = tony_neutral
    if line_number == (CAFETERIA+17):
        if option_selected == False:
            current_character = sonia_neutral
        if option_selected == True:
            current_character = sonia_smirk

    if line_number == (CAFE+2):
        if option_selected == False:
            current_character = tony_blush
        if option_selected == True:
            current_character = tony_neutral
    if line_number == (CAFE+9):
        if option_selected == False:
            current_character = tony_blush
        if option_selected == True:
            current_character = tony_angry

    if current_character == -1:
        return old_character
    else:
        return characters[current_character]