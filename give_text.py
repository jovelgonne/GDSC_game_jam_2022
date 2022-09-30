with open('script.txt') as f:
    script = f.read()
    text = script.split("\n\n")
    print(text)
    

def current_text(line_number):
    # text = script[line_number]
    # print(text)

    return text[line_number]