from pathlib import Path

class Section():
    def __init__(self, name, level=1):
        self.name = name
        self.sections[Section] = []
        self.body = []



