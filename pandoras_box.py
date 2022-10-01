# Constants
# ----------------------------------------------------------
CAFETERIA = 12
CAFE = CAFETERIA + 20
RAIN = CAFE + 36
CLIFF = RAIN + 17

tony_happy = 0
tony_neutral = 1
tony_angry = 2
tony_blush = 3
tony_jojo = 4
tony_cafe = 5
sonia_smirk = 6
sonia_neutral = 7 
player = 8


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
    if line_number == (CAFETERIA+13):
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
    elif line_number == (CAFETERIA+3):
        current_character = sonia_smirk
    
    if current_character == -1:
        return old_character
    else:
        return characters[current_character]