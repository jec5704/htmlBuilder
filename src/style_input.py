"""
file: style_input.py
author: Julio Cuello
description: gets the user input for style
language: python3
"""
from dataclasses import dataclass
import turtle

@dataclass
class Style:
    back_color: str
    head_color: str
    font: str
    font_color: str


color_set = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen',
             'lawngreen', 'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen',
             'chocolate', 'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat', 'mediumvioletred',
             'bisque', 'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred ', 'antiquewhite', 'royalblue', 'yellow',
             'indigo ', 'lightcoral', 'darkslategrey', 'sienna', 'lightslategray', 'mediumblue', 'red', 'khaki',
             'darkviolet', 'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise', 'lightyellow', 'grey', 'whitesmoke',
             'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise', 'coral', 'forestgreen', 'gainsboro',
             'darkorange', 'cornflowerblue', 'lightsteelblue', 'plum', 'lavender', 'palegreen', 'darkred', 'dimgray',
             'floralwhite', 'orangered', 'oldlace', 'darksalmon', 'lavenderblush', 'darkslategray', 'tan', 'cadetblue',
             'silver', 'tomato', 'darkkhaki', 'slategray', 'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson',
             'mistyrose', 'lime', 'saddlebrown', 'blanchedalmond', 'black', 'snow', 'seashell', 'darkcyan', 'gold',
             'midnightblue', 'darkgoldenrod', 'palevioletred', 'fuchsia', 'teal', 'lightpink', 'darkgrey',
             'mediumspringgreen', 'aquamarine', 'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood', 'rosybrown',
             'springgreen', 'purple', 'olivedrab', 'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine', 'navy',
             'salmon', 'rebeccapurple', 'darkmagenta', 'limegreen', 'deepskyblue', 'pink', 'mediumpurple', 'skyblue',
             'aqua', 'blue', 'slategrey', 'darkslateblue', 'honeydew', 'darkseagreen', 'paleturquoise', 'brown',
             'thistle', 'lemonchiffon', 'peru', 'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow',
             'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey', 'beige', 'palegoldenrod', 'darkgray', 'white',
             'ghostwhite', 'dodgerblue', 'greenyellow', 'dimgrey', 'darkorchid'}

hex_set= {"0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F",}

font_names=("Arial", "Verdana", "Times New Roman", "Tahoma", "Comic Sans MS", "Helvetica", "Lucida Grande")


def get_background_color():
    """
    this function gets the color of the background of the website and checks if the color is a valid one
    :return: color of background
    """
    print("Background color")
    background_color = str(input("Choose the name of a color or #XXXXXX: "))
    if background_color[0] == "#":
        checker = is_hexadecimal(background_color)
        if checker is True:
            return background_color
        else:
            print("Illegal format")
            return get_background_color()

    elif background_color.lower() in color_set:
        return background_color
    else:
        print("Illegal format")
        return get_background_color()


def get_text_color():
    """
    this function goes through the user input for the paragraph text color and depending on the user
    input it returns the name of the color or a string with the hexadecimal color or it makes the user input
    another number if it were false
    :return: color
    """
    print("paragraph color")
    text_color = str(input("Choose the name of a color or #XXXXXX: "))
    if text_color== None:
        return get_text_color()
    if text_color[0] == "#":
        checker = is_hexadecimal(text_color)
        if checker is True:
            return text_color
        else:
            print("Illegal format")
            return get_text_color()

    elif text_color.lower() in color_set:
        return text_color
    else:
        print("Illegal format")
        return get_text_color()


def get_heading_color():
    """
    this function goes through the user input and depending on the user input it returns the name of the color
    or a string with the hexadecimal color or it makes the user input another number if it were false
    :return: color
    """
    print("Heading color")
    heading_color = str(input("Choose the name of a color or #XXXXXX: "))
    if heading_color[0] == "#":
        checker = is_hexadecimal(heading_color)
        if checker is True:
            return heading_color
        else:
            print("Illegal format")
            return get_heading_color()

    else:
        if heading_color.lower() in color_set:
            return heading_color
        else:
            print("Illegal format")
            return get_heading_color()


def is_hexadecimal(color):
    """
    this function takes a parameter which is input by the user and this function reads through the
    input and if it matches the criteria for a hexadecimal color or the name of a color in html
    it returns true or if it does not match the criteria it returns false
    :param color: color input by the user
    :return: true or false
    """
    for ch in color:
        if ch == "#":
            continue
        if ch in hex_set:
            continue
        else:
            return False
    return True


def font_style():
    """
    this function takes user input to determine if it will write the fonts in a turtle window
    then takes the input from a user to determine from a set of keys in a dictionary which font the user wants
    :return: font name
    """
    user= input("Do you want to see the fonts? [yes]")
    if user == "yes" or user == "":
        turtle.setup(300, 275)
        for font in font_names:
            turtle.write(font, False, align="center", font =(font, 14, "normal"))
            turtle.penup()
            turtle.right(90)
            turtle.forward(20)
            turtle.left(90)
            turtle.pendown()
        turtle.done()
        i = 0
        dict_font = {}
        for font in font_names:
            print(i, ":", font, ",", "font 14")
            dict_font[i] = font
            i += 1
        decision = int(input("Choose a font by its number: "))
        if decision in dict_font:
            return dict_font[decision]
    else:
        i = 0
        dict_font = {}
        for font in font_names:
            print(i, ":", font, ",", "font 14")
            dict_font[i]= font
            i += 1
        decision = int(input("Choose a font by its number: "))
        if decision in dict_font:
            return dict_font[decision]
