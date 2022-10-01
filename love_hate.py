def update_bar(love_hate_meter, option_number, option_selected):
    exceptions = [0,2]
    if option_number in exceptions:
        pass
    elif option_selected == False: 
        love_hate_meter -= 1
    else:
        love_hate_meter += 1
    
    if love_hate_meter < 0:
        love_hate_meter = 0
    elif love_hate_meter > 10:
        love_hate_meter = 10

    return love_hate_meter 