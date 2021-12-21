from pathlib import Path
from jinja2 import Environment, BaseLoader, Template
import math

def load_jinja2_template(path:Path):
    with open(str(path)) as file_:
        template_render = Template(file_.read()).render()
        return template_render


def get_forecast_period(df, date_field):
    date_min = df[date_field].min()
    date_max = df[date_field].max()

    delta = date_max - date_min

    forecast_period = int(delta.days / 10)

    return forecast_period


def round_decimals_up(number:float, decimals:int=2):
    """
    Returns a value rounded up to a specific number of decimal places.
    """

    log10 = -int(math.log10(number))
    res = round(number, log10 + 2)
    return res
