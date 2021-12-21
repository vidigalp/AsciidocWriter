import pytest
import pandas as pd
from AsciidocWriter.asciidoc_writer_utils import load_jinja2_template
from AsciidocWriter.asciidoc_writer_utils import get_forecast_period


def test_load_jinja2_template():
    assert load_jinja2_template(
        path='/Users/vidigalp/Code/AsciidocWriter/tests/test_templates/load_jinja2_template.jinja2') == 'hello world!'


def test_load_jinja2_template_multiple_lines():
    assert load_jinja2_template(
        path='/Users/vidigalp/Code/AsciidocWriter/tests/test_templates/load_jinja2_template_multiple_lines.jinja2') == 'hello world!\nhello again!'


def test_get_forecast_period():

    data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
          'age': [20, 19, 22, 21],
          'favorite_color': ['blue', 'red', 'yellow', "green"],
          'grade': [88, 92, 95, 70],
          'birth_date': ['01-02-1986', '08-05-1997', '04-28-1996', '12-16-1995']}

    df = pd.DataFrame(data)
    df['birth_date'] = pd.to_datetime(df['birth_date'])

    assert get_forecast_period(df=df, date_field='birth_date') == 423
