from pathlib import Path
from jinja2 import Environment, BaseLoader, Template

def load_jinja2_template(Path):
    with open(Path) as file_:
        template = Template(file_.read())
    template.render(name='John')
    return True
