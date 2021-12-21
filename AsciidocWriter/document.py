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
from jinja2 import Template
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

        :param name:
        :param author:
        :param description:
        :param config_file:
        """

        self.name = name
        self.author = author
        self.description = description
        self.sections: List[Section] = []

        if config_file:
            with open(config_file) as f:
                self.config = yaml.load(f, Loader=yaml.FullLoader)

        if self.config:
            data = {"title": "title",
                    "version": self.config['header']['version'],
                    "author": self.config['header']['author'],
                    "images_directory": self.config['header']['image_directory'],
                    "image": self.config['header']['title-page-image']['image'],
                    "background_image_width": self.config['header']['title-page-image']['width'],
                    "background_image_height": self.config['header']['title-page-image']['height'],
                    "fit": self.config['header']['title-page-image']['fit'],
                    "xrefstyle": "short",
                    "opacity": self.config['header']['title-page-image']['opacity'],
                    "doc_uuid": str(uuid.uuid1())}

            self.generate_header(data=data)

    def generate_header(self, data, template_path:Path=None):
        """ Generate AsciiDoctor document header

        @param data:
        @param template_path:
        """
        with open(Path.joinpath(Path(__file__).resolve().parent.parent, 'templates', 'header.jinja2')) as file_:
            template = Template(file_.read())

        self.header = template.render(data)





    def add_section(self, section:Section):
        """

        @param section:
        """
        self.sections.append(section)
