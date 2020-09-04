"""
file: html_input.py
author: Julio Cuello
description: gets the user input for the title of the website, the title of the paragrphs of the website and
the images for the website
language: python3
"""
from dataclasses import dataclass

@dataclass
class Webpage:
    title: str
    body: list

@dataclass
class Paragraph:
    title: str
    content: str
    image: list


def get_title():
    """
    gets the title of the website
    :return:string of the title
    """
    title = str(input("What is the title of your website?"))
    return title


def title_paragraph():
    """
    gets the title of the paragraph
    """
    return str(input("Title of your paragraph"))


def content_paragraph():
    """
    recieves one line content of the paragraph
    """
    return str(input("content of your paragraph (single line)"))


def more_paragraphs():
    """
    this function makes a loop where the user is repeatedly asked for input until it says no
    and this returns the paragraph class with all the images and paragraph attributes
    in a list of paragraphs
    """
    paragraphs = [Paragraph(title_paragraph(),content_paragraph(),get_images())]
    add_more = input("Do you want to add another paragraph? [yes]")
    if add_more == "yes" or add_more == "":
        while add_more == "yes" or add_more == "":
            new_paragraph = Paragraph(title_paragraph(),content_paragraph(),get_images())
            paragraphs.append(new_paragraph)
            add_more = input("Do you want to add another paragraph? [yes]")
    return paragraphs


def get_images():
    """
    this function returns all the images for the html file in a list
    :return:
    """
    images= []
    image = input("Do you want to add images? [yes]")
    if image == "yes" or image == "":
        image_add = input("Image file name: ")
        images.append(image_add)
        add_more = input("Do you want to add another image? [yes]")
        while add_more == "yes" or add_more == "":
            new_image = input("Image file name: ")
            add_more = input("Do you want to add another image? [yes]")
            images.append(new_image)
    return images

