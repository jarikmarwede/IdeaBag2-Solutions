#!/usr/bin/env python3
"""Convert Text to HTML

Title:
Text to HTML Generator

Description:
Come up with a simple program
that will allow a user to enter in various bits of text data.
Have it then generate the HTML equivalent
or create a HTML page based on the data.
The idea here is to give the user the option of writing simple text data
and it would generate the code afterward.
For instance, if the user enters in a title and few paragraphs,
the program would generate the necessary <h1>, <p>, <quote>, bulleting tags
needed to format that text on the web.
"""


def generate_from_file(file_path: str) -> str:
    """Return HTML code for file
    """
    with open(file_path, "r") as file:
        text = file.read()
    html = generate_html(text)
    return html


def generate_html(text: str) -> str:
    """Return HTML code for text
    """
    lines = []
    for line in text.split("\n"):
        lines.append(line)

    html = "<!DOCTYPE html><html>"
    for index, line in enumerate(lines):
        # add headings
        if check_heading(index, line, lines, html) is True:
            html += "<h3>" + line + "</h3>"
        # add paragraphs
        elif check_paragraph(index, line, lines) is True:
            html += "<p>" + line
            for line in lines[index + 1:]:
                if line != "":
                    html += "<br>" + line
                else:
                    break
            html += "</p>"
    html += "</html>"
    return html


def check_heading(index: int, line: str, lines: list, html: str) -> bool:
    """Return True if line specified is a heading
    """
    signs = (".", ",", ";", ":", "!", "?")
    if index == len(lines) - 1:
        if (line != "" and
                lines[index - 1] == ""):
            for sign in signs:
                return bool(line.find(sign) == -1)
        else:
            return False
    elif (line != "" and
          (lines[index - 1] == "" or html == "") and
          lines[index + 1] == ""):
        for sign in signs:
            return bool(line.find(sign) == -1)
    else:
        return False


def check_paragraph(index: int, line: str, lines: list) -> bool:
    """Return True if line specified is a paragraph
    """
    if index == 0:
        return bool(line != "")
    elif line != "" and lines[index - 1] == "":
        return True
    return False


def create_website(file_name: str, html: str):
    """Create html file for html
    """
    if not file_name.endswith(".html"):
        file_name += ".html"
    with open(file_name, "w") as file:
        file.write(html)


if __name__ == "__main__":
    FILE = input("Please input the path to the file "
                 "you want to convert to HTML: ")
    FILE_NAME = input("How should the new HTML file be called: ")
    HTML = generate_from_file(FILE)
    create_website(FILE_NAME, HTML)
