"""
file: html_builder.py
author: Julio Cuello
description: page builder that takes input to create html webpages
language: python3
"""
import sys
from html_input import *
from style_input import *
from website_mode import create
@dataclass
class Webpage:
    title: str
    body: list

@dataclass
class Paragraph:
    title: str
    content: str
    image: list


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


def final_result():
    """
    This function builds the website out of the user input, this function gets all the paragraph
    images, and title of paragraphs along with the website title and stores them in a Webpage class
    :return: Webpage class with all its required inputs
    """
    title= get_title()
    paragraphs= more_paragraphs()
    return Webpage(title, paragraphs)

def create_html():
    """
    this function stores the results for the style inputs and the other inputs
    in variables in order to call them respectively throughout the write functions where
    the program writes the file in html format with its respective tags
    this function gives as a result an html file with the user inputs
    """
    result= final_result()
    filename= "project.html"
    style= Style(get_background_color(), get_heading_color(), font_style(), get_text_color())
    with open(filename, "w") as index:
        index.write("<!DOCTYPE html>\n")
        index.write("<html>\n")
        index.write("<head>\n")
        index.write("<title>\n")
        index.write(result.title + "\n")
        index.write("</title>\n")
        file = open("style_template.txt")
        for line in file:
            line = line.replace("@BACKCOLOR", style.back_color)
            line = line.replace("@HEADCOLOR", style.head_color)
            line = line.replace("@FONTSTYLE", style.font)
            line = line.replace("@FONTCOLOR", style.font_color)
            index.write(line)
        index.write("</head>\n")
        index.write("<body>\n")
        index.write("<h1>\n" + result.title + "\n" + "</h1>\n")

        for paragraph in result.body:
            index.write("<h2>\n" + paragraph.title +"\n" + "</h2>\n")
            index.write("<p>\n" + paragraph.content + "\n" + "</p>\n")
            if paragraph.image != [None]:
                for image in paragraph.image:
                    index.write("<img src = " + '"' + image + '"' + "class = center>\n")
        index.write("</body>")
        index.write("</html>")
        print("your website has been saved to: "+ filename)

def web_or_wiz():
    """
    this function checks wether there is an argument on the command line and if there
    is, then it runs website mode, else it would run wizard mode
    :return:
    """
    if len(sys.argv) == 1:
        create_html()
    else:
        create()

if __name__ == '__main__':
    web_or_wiz()