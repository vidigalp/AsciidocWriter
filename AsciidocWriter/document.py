# -*- coding: utf-8 -*-
"""
This module implements the class that deals with the full document.
    :copyright: (c) 2021 by Pedro Vidigal.
    :license: MIT, see License for more details.
"""
from loguru import logger
from .section import Section

class Document():
    """
    Asciidoc Document

    """
    def __init__(self, name:str, author:str, description:str):
        """

        @param name:
        @param author:
        @param description:
        """
        self.name = name
        self.author = author
        self.description = description
        self.sections = [Section]


    def set_document_title(self):
        pass


    def add_section(self, section:Section):
        """

        @param section:
        """
        self.sections.append(section)
