from pathlib import Path
#from enum import Enum

class Section():
    def __init__(self, name, level=1, page_feed="<<<"):
        self.name = name
        self.sections = [Section]
        self.body = ["\n\n", page_feed, "\n\n" f"{'='*(level+1)} {name}", "\n\n"]

    def add_paragraph(self, text:str):
        self.body.append(text)






