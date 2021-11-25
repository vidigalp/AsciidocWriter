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
    def __init__(self):
        self.sections[Section] = []

    def section(self, title:str):
        """
        
        """
        logger.info(f"SECTION -> {title}")
        pass
    