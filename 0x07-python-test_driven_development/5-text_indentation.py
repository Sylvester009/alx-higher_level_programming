#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""


def text_indentation(text):
    """prints a text with 2 new lines after characters: ., ? and :
    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    b = 0
    while b < len(text) and text[b] == ' ':
        b += 1

    while b < len(text):
        print(text[b], end="")
        if text[b] == "\n" or text[b] in ".?:":
            if text[b] in ".?:":
                print("\n")
            b += 1
            while c < len(text) and text[b] == ' ':
                b += 1
            continue
        b += 1
