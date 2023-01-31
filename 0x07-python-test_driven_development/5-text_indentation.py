#!/usr/bin/python3
"""
This file manage the text-identation function
Written by: daorejuela1
"""


def text_indentation(text):
    """
    This function automatically ident text.

    Args:
        param1: text to ident.

    Returns:
        Nothing.

    Raises:
        TypeError: if text is not strings.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    special_characters = [".", "?", ":"]
    last_printed = 0
    for i in range(0, len(text)):
        try:
            while (text[last_printed] == " "):
                last_printed = last_printed + 1
        except IndexError:
            pass
        if (text[i] in special_characters):
            print(text[last_printed: i + 1])
            print()
            last_printed = i + 1
            try:
                while (text[last_printed] == " "):
                    last_printed = last_printed + 1
            except IndexError:
                pass

        if (last_printed != len(text) - 1 and i == len(text) - 1):
            print(text[last_printed:], end="")
