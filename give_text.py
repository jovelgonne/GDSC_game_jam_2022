with open('script.txt') as f:
    script = f.read()
    text = script.split("\n\n")
    

def current_text(line_number):
    return text[line_number]