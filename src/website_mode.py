"""
file: website_mode.py
author: Julio Cuello
description: takes user input and argument from command line to create website
language: python3
"""

from style_input import *
import sys

@dataclass
class Webpage:
    title: str
    body: list


@dataclass
class Image:
    source: str
    width: str

@dataclass
class Paragraph:
    title: list
    content: list
    image: list

def command_input(filename):
    paragraph_list= []
    text_list= []
    images_list= []
    with open(filename) as file:
        title= file.readline().strip()
        for line in file:
            line= line.strip()
            line2= line.split()
            if line != "" and line2[0] == "!title":
                paragraph_title= line2[1:]
            elif line != "" and line2[0][0] != "!":
                 text_list.append(line)
            elif line != "" and line2[0] == "!image":
                if len(line) == 3:
                    images_list.append(Image(line2[1], line[2]))
                else:
                    images_list.append(Image(line2[1], ""))
            elif line == "":
                paragraph= Paragraph(paragraph_title,text_list,images_list)
                paragraph_list.append(paragraph)
                text_list= []
                images_list = []
        paragraph = Paragraph(paragraph_title, text_list, images_list)
        paragraph_list.append(paragraph)
    return Webpage(title, paragraph_list)

def names_of_titles(filename):
    f= open(filename)
    name= f.readline()
    f.close()
    return name



def create():
    dict_files= {}
    style = Style(get_background_color(), get_heading_color(), font_style(), get_text_color())
    for i in range(1,len(sys.argv)):
        arg = sys.argv[i].split(".")
        filename = arg[0] + ".html"
        dict_files[names_of_titles(sys.argv[i])] = filename
    for i in range(1,len(sys.argv)):
        result= command_input(sys.argv[i])
        arg= sys.argv[i].split(".")
        filename= arg[0] + ".html"
        with open(filename, "w") as index:
            index.write("<!DOCTYPE html>\n")
            index.write("<html>\n")
            index.write("<head>\n")
            index.write("<title>\n")
            index.write(result.title)
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
            index.write("<hr/>\n")
            index.write("<p align=" + '"' + "center" + '"' + ">\n")
            for i in dict_files:
                index.write("<a href=" + '"' + dict_files[i] + '"' + ">" + '"' + i + "</a>---")
            for paragraph in result.body:
                index.write("<h2>")
                for word in paragraph.title:
                    index.write(word + " ")
                index.write("</h2>\n")
                index.write("<p>")
                for word in paragraph.content:
                    index.write(word)
                index.write("</p>")
                for image in paragraph.image:
                    if image.width == "":
                        index.write("<img src = " + '"' + image.source + '"' + "class = center>\n")
                    else:
                        index.write("<img src = " + '"' + image.source + '"'+ 'width=' + '"' + image.width + '"' + "class = center>\n")
                index.write("</body>")
                index.write("</html>")