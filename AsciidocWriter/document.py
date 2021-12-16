# -*- coding: utf-8 -*-
"""
This module implements the class that deals with the full document.
    :copyright: (c) 2021 by Pedro Vidigal.
    :license: MIT, see License for more details.
"""
from typing import List
from loguru import logger
from .section import Section
import yaml
from pathlib import Path
import jinja2
from pathlib import Path

ROOT_DIR = Path.cwd().parent

class Document():
    """
    Asciidoc Document

    """
    def __init__(self, name:str, author:str, description:str=None, config_file:Path=None):
        """

        @param name:
        @param author:
        @param description:
        """
        self.name = name
        self.author = author
        self.description = description
        self.sections: List[Section] = []

        if config_file:
            with open(config_file) as f:
                self.config = yaml.load(f, Loader=yaml.FullLoader)

        data = {"title": "title",
                "author": self.config['header']['author'],
                "images_directory": self.config['header']['image_directory'],
                "image": self.config['header']['title-page-image']['image'],
                "background_image_width": self.config['header']['title-page-image']['width'],
                "background_image_height": self.config['header']['title-page-image']['height'],
                "fit": self.config['header']['title-page-image']['fit'],
                "opacity": self.config['header']['title-page-image']['opacity']}

        self.set_document_header(data=data)

    def set_document_header(self, data, template_path:Path=None):
        if not template_path:
            template_path = Path.joinpath(ROOT_DIR, 'templates')
        templateLoader = jinja2.FileSystemLoader(searchpath=str(template_path))

        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template("health_check_header.jinja2").render()

        self.header = template.render(data)




    def add_section(self, section:Section):
        """

        @param section:
        """
        self.sections.append(section)
