# -*- coding: utf-8 -*-
"""
This module implements the class that deals with the full document.
    :copyright: (c) 2021 by Pedro Vidigal.
    :license: MIT, see License for more details.
"""
import uuid
from pathlib import Path
from typing import List

import yaml
from jinja2 import Environment
from jinja2 import FileSystemLoader

from .section import Section

ROOT_DIR = Path(__file__).resolve().parent

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
                "xrefstyle": "short",
                "opacity": self.config['header']['title-page-image']['opacity'],
                "doc_uuid": str(uuid.uuid1())}

        self.set_document_header(data=data)

    def set_document_header(self, data, template_path:Path=None):
        path = Path.joinpath(Path(__file__).resolve().parent, 'templates')
        templateEnv = Environment(loader=FileSystemLoader(searchpath=path))
        template = templateEnv.get_template("health_check_header.jinja2").render()

        self.header = template.render(data)

        i =2




    def add_section(self, section:Section):
        """

        @param section:
        """
        self.sections.append(section)
