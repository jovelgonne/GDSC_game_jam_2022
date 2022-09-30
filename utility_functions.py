# Function used for scrolling text char-by-char
def shorten_string(text, frames_since_space):
    length_of_text = len(text)
    if length_of_text > (frames_since_space):      
        text = text[:frames_since_space]
        space_pressed = 1
    else:
        space_pressed = 0                         # Reset the space button after all text displayed

    return [text, space_pressed]